import torch
import torch.nn as nn

class MesenCoder(nn.Module):
    def __init__(self,
                 n_feature: int,
                 n_source: int,
                 hidden_dim: int,
                 latent_dim: int,
                 source_dim: int = 1,
                 activation: type[nn.Module] = nn.ReLU
                 ) -> None:
        super().__init__()
        self.activation = activation

        # vanilla encoder
        self.encoder = nn.Sequential(
            nn.Linear(n_feature, hidden_dim), activation(),
            nn.Linear(hidden_dim, latent_dim))
        
        # conditional decoder
        in_dim_dec = latent_dim + source_dim
        self.decoder = nn.Sequential(
            nn.Linear(in_dim_dec, hidden_dim), activation(),
            nn.Linear(hidden_dim, n_feature))

        # source embedding
        self.embed_src = nn.Embedding(
            num_embeddings = n_source,
            embedding_dim = source_dim)
        
        # init weights
        self._initialize_weights()
        nn.init.normal_(
            self.embed_src.weight,
            mean = 0., std = .05)

    def forward(self,
                x: torch.Tensor,
                src: torch.Tensor | None
                ) -> torch.Tensor | \
                     tuple[torch.Tensor,
                           torch.Tensor]:

        # encoder
        z = self.encoder(x)

        if src is not None:
            # source embedding
            v = self.embed_src(src)

            # decoder
            h = torch.cat((z, v), dim = -1)
            x_hat = self.decoder(h)
            return x_hat, z

        else:
            return z

    def _initialize_weights(self) -> None:
        if self.activation is nn.ReLU:
            nonlinearity = 'relu'
        for m in self.modules():
            if isinstance(m, nn.Linear):
                nn.init.kaiming_uniform_(
                    m.weight,
                    nonlinearity = nonlinearity)
                nn.init.zeros_(m.bias)
