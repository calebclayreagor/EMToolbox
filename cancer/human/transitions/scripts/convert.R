#%%
library(Seurat)
library(zellkonverter)

name <- 'SKNSHm_NORtoMES_merge'

# convert RDS -> H5AD
obj <- readRDS(paste0(name, '.rds'))
DefaultAssay(obj) <- 'RNA'
obj[['SCT']] <- NULL
sce <- as.SingleCellExperiment(obj, assay = 'RNA')
writeH5AD(sce, paste0(name, '.h5ad'), X_name = 'counts')

#%%
