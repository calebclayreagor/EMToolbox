#%%
library(Seurat)
library(zellkonverter)

name <- 'PDX63.strigentFilters_rmRibo_rmDoub'

# convert RDS -> H5AD
obj <- readRDS(paste0(name, '.rds'))
obj <- UpdateSeuratObject(obj)
DefaultAssay(obj) <- 'RNA'
obj[['SCT']] <- NULL
sce <- as.SingleCellExperiment(obj, assay = 'RNA')
writeH5AD(sce, paste0(name, '.h5ad'), X_name = 'counts')

#%%
