import argparse
import pandas as pd
import anndata as ad
import lightning as L
from torch.utils.data import DataLoader
from torch.utils.data import WeightedRandomSampler
from lightning.pytorch.loggers import WandbLogger
from lightning.pytorch.callbacks import ModelCheckpoint
from lit_module import MesenchymalStates
from dataset import MesenchymeDataset

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # CLI parameters
    parser.add_argument('--adata_pth', type = str)
    parser.add_argument('--feat_pth', type = str)
    parser.add_argument('--species', type = str)
    parser.add_argument('--save_ckpt', action = 'store_true')
    parser.add_argument('--train_frac', type = float, default = .8)
    parser.add_argument('--hidden_dim', type = int, default = 64)
    parser.add_argument('--latent_dim', type = int, default = 2)
    parser.add_argument('--batch_size', type = int, default = 32)
    parser.add_argument('--learning_rate', type = float, default = 1e-3)
    parser.add_argument('--max_epochs', type = int, default = 1000)
    parser.add_argument('--val_log_freq', type = int, default = 100)
    parser.add_argument('--num_workers', type = int, default = 32)
    args = parser.parse_args()
    L.seed_everything(1)

    # load adata & select features
    g = pd.read_csv(args.feat_pth)[args.species]
    adata = ad.read_h5ad(args.adata_pth)[:, g]

    # compute weights (1/n)
    grp = adata.obs.groupby('source', observed = True)
    w_dict = (1 / grp.size()).to_dict()
    adata.obs['w'] = adata.obs.source.map(w_dict)

    # select training examples
    ix_train = grp.sample(frac = args.train_frac).index
    msk_train = adata.obs_names.isin(ix_train)
    adata.obs['training'] = msk_train.astype(str)

    # training/validation split
    adata_train = adata[msk_train].copy()
    adata_val = adata[~msk_train].copy()
    train_ds = MesenchymeDataset(adata_train, True)
    val_ds = MesenchymeDataset(adata_val, True)

    # training sampler
    sampler = WeightedRandomSampler(
        weights = adata_train.obs.w,
        num_samples = len(train_ds),
        replacement = True)

    # dataloaders
    train_dl = DataLoader(
        train_ds,
        batch_size = args.batch_size,
        sampler = sampler,
        num_workers = args.num_workers,
        pin_memory = True)
    val_dl = DataLoader(
        val_ds,
        batch_size = args.batch_size,
        shuffle = False,
        num_workers = args.num_workers,
        pin_memory = True)

    # custom autoencoder
    args.n_feature = adata.n_vars
    args.n_source = len(grp)
    model = MesenchymalStates(args)

    # wandb logger
    logger = WandbLogger(
        project = 'MesenCoder',
        log_model = args.save_ckpt)
    logger.watch(model, log = 'all')

    # checkpoints
    if args.save_ckpt:
        checkpoints = ModelCheckpoint(
            every_n_epochs = args.val_log_freq,
            save_top_k = -1,
            save_last = False,
            dirpath = 'checkpoints',
            filename = '{epoch:02d}')
    else: checkpoints = None

    # trainer
    trainer = L.Trainer(
        max_epochs = args.max_epochs,
        logger = logger,
        callbacks = checkpoints,
        accelerator = 'auto',
        devices = 'auto',
        num_sanity_val_steps = 0,
        log_every_n_steps = 4,
        enable_checkpointing = args.save_ckpt)

    # train
    trainer.fit(model, train_dl, val_dl)
