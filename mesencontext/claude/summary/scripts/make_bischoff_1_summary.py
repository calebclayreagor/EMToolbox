import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, RED, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Lung/Bischoff2021_Lung-1"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Lung/Bischoff2021_Lung-1"
gates=[
 ("Gate 1 \u2014 mixing & continuity","NO-GO",RED,
  "MIXED (diff-sample kNN frac 0.02\u21920.47, ceiling 0.81; both lobes internally sample-mixed, tumours span both) "
  "but NOT CONTINUOUS \u2014 two islands: PAGA between-lobe 0.01 vs within 0.55; 0.18% of edges & 1.9% of cells "
  "bridge; bimodal diffusion axis (peak/valley 387\u00d7). Invariant across \u03b8 {0,2,5,10}, n_pcs {12,16,20} \u2014 not "
  "under-integration."),
 ("Gate 2 \u2014 module geography","NA",GREY,
  "Not evaluated \u2014 Gate 1 NO-GO (spec \u00a76). Lobe-identity fork: no lobe is a valid scope target \u2014 signatures "
  "near union-control baseline everywhere (Gast \u22120.04 / pSom +0.06 / Crest \u22120.03); the alveolar lobe shows the "
  "K\u00fcrten sign pattern but at baseline magnitude and is the DIFFERENTIATED pole (biologically backwards); the "
  "EMT/dediff lobe is incoherent (Gast~pSom \u22120.32)."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not evaluated \u2014 branching-only, and no trajectory exists."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Lung adenocarcinoma (Bischoff et al., 2021), 10x \u2014 13,382 malignant cells (10 tumour samples, "
 "44-cell threshold).")
verdict=("Embryonic pattern does NOT reproduce \u2014 malignant structure is two disconnected EMT/differentiation "
 "lobes, not one continuous manifold; no trajectory fit (Gate 1 NO-GO). No lobe is a valid scope target: "
 "signatures sit at union-control baseline, and the one lobe with the K\u00fcrten sign pattern (alveolar) is the "
 "differentiated pole. Descriptive EMT-TF overlay (no trajectory to polarize): SOX4 graded high on the "
 "EMT/dediff lobe; SOX9/TEAD1/FOXC1 patchier.")
params=[
 ("Min-cell threshold","44 (geom-mean of 127\u219215 gap, 8.5\u00d7) \u2192 10/19 samples"),
 ("Over-dispersed genes","1,976 (scFates GAM)"),
 ("n_pcs","16 (PCs > 0.5% variance; PC1 = 12.4%)"),
 ("Integration","Harmony on sample, \u03b8=2 (mixing plateaus by \u03b8=2)"),
 ("Embedding","k=15, UMAP spread=1.3, Leiden res=0.5 (12 clusters)"),
 ("Lobe split","diffusion-axis valley: Alveolar 6,100 / EMT-dediff 7,282"),
 ("Signatures","score_genes vs union pool (Gast 80 / pSom 95 / Crest 103 genes)"),
 ("EMT-TFs shown","SOX4 83%, SOX9 44%, TEAD1 44%, FOXC1 33% (\u22653% floor; VIM excluded)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Bischoff 2021 LUAD \u2014 analysis summary",gates,panels,dataset,verdict,params,
              run_label="run 2 of 3")
print("built")
