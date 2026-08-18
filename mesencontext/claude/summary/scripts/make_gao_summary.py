import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Breast/Gao2021_Breast-3"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Breast/Gao2021_Breast-3"
gates=[
 ("Gate 1 — mixing & continuity","NO-GO",RED,
  "Breast malignant cells form a per-patient archipelago. After best-effort Harmony (\u03b8=10) the per-neighbourhood "
  "iLISI reaches only 1.6 of a 3.8 ceiling (42%), same-sample kNN stays 2.9\u00d7 the mixed baseline, and 4/5 tumours are "
  "self-segregated (3.5\u20135.1\u00d7). Not a sample-integrated manifold."),
 ("Gate 2 — module geography","N/A",GREY,
  "Not evaluated \u2014 Gate 1 NO-GO stops the chain. Module scores are flat and low-amplitude everywhere (Gast \u22120.024 / "
  "pSom +0.016 / Crest \u22120.042); no Gast/pSom hub, no arms."),
 ("Gate 3 — cross-repression","N/A",GREY,
  "Not evaluated \u2014 no trajectory is fit (branching-only gate)."),
]
panels=[("Malignant manifold — samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (Gao et al., 2021), 10x \u2014 6,411 malignant cells across 5 breast tumours (DCIS1, TNBC1\u20135) "
 "pooled from the /Breast and /Breast_and_thyroid leaves (inner-join 22,164 genes); 5 anaplastic-thyroid (ATC) "
 "samples dropped as a different cancer lineage.")
verdict=("The embryonic-program pattern does NOT reproduce. The breast malignant compartment is inter-patient CNV/clonal "
 "heterogeneity \u2014 a per-patient archipelago no integration strength resolves into one continuous, sample-mixed "
 "manifold \u2014 so no cell-state trajectory is fit (Gate 1 NO-GO). The only cross-patient axis is proliferation. This "
 "corrects prior attempts that forced a curve onto the over-integrated blob.")
params=[
 ("Scope","breast-only; 5 ATC samples dropped (different lineage)"),
 ("Sample threshold","\u2265347 cells (gap 618\u2192195, 3.17\u00d7); drops TNBC3 \u2192 5 samples"),
 ("Embedding","2,663 overdispersed; PCA n_pcs=30 (robust 20/30/40)"),
 ("Integration","Harmony on sample, \u03b8 swept 0/2/5/8/10/20; \u03b8=10 plateau"),
 ("Gate-1 read","per-neighbourhood iLISI / kNN / self-enrichment (not a global scalar)"),
 ("EMT-TFs shown","FOXC1 (28.5%) \u00b7 FOXC2 (16.5%); descriptive overlay (no pseudotime)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Gao 2021 breast cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
