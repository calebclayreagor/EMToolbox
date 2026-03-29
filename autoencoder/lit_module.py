import argparse
import torch, wandb
import numpy as np
import scanpy as sc
import lightning as L
import torch.nn.functional as F
from torch.optim import Adam
from torch.optim import Optimizer
import matplotlib.pyplot as plt
from model import MesenCoder

class MesenchymalStates(L.LightningModule):
    def __init__(self, 
                 hparams: argparse.Namespace,
                 out_pth: str | None = None):
        super().__init__()
        self.save_hyperparameters(hparams)
        self.model = MesenCoder(
            n_feature = self.hparams.n_feature,
            n_source = self.hparams.n_source,
            hidden_dim = self.hparams.hidden_dim)
        self.out_pth = out_pth

    def forward(self,
                x: torch.Tensor,
                src: torch.Tensor | None,
                t: torch.Tensor | None
                ) -> torch.Tensor | \
                     tuple[torch.Tensor,
                           torch.Tensor]:
        return self.model(x, src, t)

    def custom_step(self,
                    batch: tuple[torch.Tensor,
                                 torch.Tensor | None,
                                 torch.Tensor | None,
                                 torch.Tensor]
                    ) -> torch.Tensor | \
                         tuple[torch.Tensor,
                               torch.Tensor]:
        X, src, t, _ = batch
        if src is not None:
            X_hat, z = self.forward(X, src, t)
            loss = F.mse_loss(X_hat, X)
            return loss, z
        else:
            z = self.forward(X, src, t)
            return z

    def training_step(self,
                      batch: tuple[torch.Tensor,
                                   torch.Tensor,
                                   torch.Tensor,
                                   torch.Tensor],
                      _) -> torch.Tensor:
        loss, _ = self.custom_step(batch)
        batch_size = batch[0].size(0)
        self.log(
            'train_loss', loss,
            on_step = False,
            on_epoch = True,
            batch_size = batch_size,
            sync_dist = True,
            add_dataloader_idx = False)
        return loss
    
    def validation_step(self,
                        batch: tuple[torch.Tensor,
                                     torch.Tensor,
                                     torch.Tensor,
                                     torch.Tensor],
                        _) -> None:
        _, _, _, ix = batch
        loss, z = self.custom_step(batch)
        batch_size = batch[0].size(0)
        self.log(
            'val_loss', loss,
            on_step = False,
            on_epoch = True,
            batch_size = batch_size,
            sync_dist = True,
            add_dataloader_idx = False)
        ix = ix.detach().cpu().numpy().squeeze()
        z = z.detach().cpu().numpy().squeeze()
        self.val_latent_z[ix] = z
        
    def predict_step(self,
                     batch: tuple[torch.Tensor,
                                  torch.Tensor],
                        _) -> None:
        batch = (batch[0], None, None, batch[1])
        _, _, _, ix = batch
        z = self.custom_step(batch)
        ix = ix.detach().cpu().numpy().squeeze()
        z = z.detach().cpu().numpy().squeeze()
        self.pred_latent_z[ix] = z

    def on_validation_epoch_start(self) -> None:
        if self.current_epoch > 0:
            self.val_latent_z_prev = self.val_latent_z.copy()
        self.val_latent_z = np.zeros(
            len(self.trainer.val_dataloaders.dataset),
            dtype = np.float32)
        
    def on_predict_epoch_start(self) -> None:
        self.pred_latent_z = np.zeros(
            len(self.trainer.predict_dataloaders.dataset),
            dtype = np.float32)

    def on_validation_epoch_end(self) -> None:
        if self.current_epoch > 0:
            diff = self.val_latent_z - self.val_latent_z_prev
            drift = np.mean(abs(diff))
            self.log(
                'val_drift_z', drift,
                on_step = False,
                on_epoch = True,
                batch_size = len(self.val_latent_z),
                sync_dist = True,
                add_dataloader_idx = False)
            
            if (self.current_epoch + 1) % self.hparams.val_log_freq == 0:
                adata = self.trainer.val_dataloaders.dataset.adata
                adata.obs['z'] = self.val_latent_z.copy()
                adata.obsm['X_mesencoder'] = adata.obs[['z', 't']].values
                
                fig, ax = plt.subplots(1, 1, figsize = (5, 5))
                sc.pl.embedding(adata, 'X_mesencoder', color = 'celltype',
                                size = 140, alpha = .7, legend_loc = 'on data',
                                legend_fontoutline = 1, show = False, ax = ax)

                label_dict = {
                    'Lateral Plate Mesoderm'     : 'LPM',
                    'nan'                        : '',
                    'Nascent Endothelium'        : 'NE',
                    'Neuromesodermal Progenitor' : '',
                    'Presomitic Mesoderm'        : 'PSM',
                    'Cranial Mesenchyme'         : 'CM',
                    'Migratory Neural Crest'     : 'mNC',
                    'Neuroglial Progenitors'     : 'NGP',
                    'Premigratory Neural Crest'  : 'pmNC'}

                for label in ax.texts:
                    _label_ = label.get_text()
                    if _label_ in label_dict:
                        label.set_text(label_dict[_label_])

                ax.invert_xaxis()
                ax.invert_yaxis()
                fig.tight_layout()
                self.logger.experiment.log({
                    'val_embedding' : wandb.Image(fig),
                    'epoch'        : self.current_epoch})
                plt.close(fig)

    def on_predict_epoch_end(self) -> None:
        adata = self.trainer.predict_dataloaders.dataset.adata
        adata.obs['z'] = self.pred_latent_z.copy()
        adata.obsm['X_mesencoder'] = adata.obs[['z', 't']].values
        adata.write(self.out_pth)

    def configure_optimizers(self) -> Optimizer:
        return Adam(self.parameters(), lr = self.hparams.learning_rate)
