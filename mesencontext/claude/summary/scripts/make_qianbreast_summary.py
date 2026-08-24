import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Qian2020_Breast-2"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Qian2020_Breast-2"
gates=[
 ("Gate 1 — mixing & continuity","NO-GO",RED,
  "Harmony on sample cannot integrate the compartment. Across \u03b8 2\u201320 (confirmatory to 50) \u00d7 n_pcs 20\u201340 the "
  "regenerated embedding keeps the dominant patient (sample 54, 65% of malignant cells) as a segregated territory: at "
  "low \u03b8 a literal disconnected component (2,675 vs 2,143 cells), at high \u03b8 a lobe the kNN graph merges only as a "
  "connectivity artifact. Per-neighbourhood iLISI stays \u22641.5 of 2.26; sample-54 cells keep 92% same-sample 30-NN "
  "(chance 65%). Dropping sample 54, the other 6 integrate well (iLISI 3.4/4.86) \u2014 the obstruction is the dominant "
  "patient, not a generic batch."),
 ("Gate 2 — module geography","NA",GREY,
  "Not reached. Gate 1 NO-GO stops the chain before a manifold/signatures are fit, so module geography is not "
  "evaluated (manifold / signatures / correlation / modules notebooks are not produced, per the deliverable spec)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not reached \u2014 no trajectory, hence no bifurcation and no hub cross-repression test."),
]
panels=[("Malignant manifold — samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (Qian 2020), 10x, 4,818 malignant cells over 7 patients; sample 54 alone is 65% of the "
 "malignant compartment (one dominant patient). No sample dropped (all 7 pass the 10-cell floor).")
verdict=("The embryonic pattern does NOT reproduce here \u2014 the malignant compartment cannot be integrated into a "
 "continuous manifold: a single dominant patient forms an irreconcilable segregated territory at every integration "
 "strength, so no cell-state trajectory is fit. Gate 1 NO-GO / Gate 2 NA / Gate 3 NA.")
params=[
 ("Sample threshold","\u226510 malignant cells/sample; all 7 pass \u2192 4,818 cells"),
 ("Overdispersed genes","1,225 (scFates find_overdispersed); no sc.pp.scale"),
 ("Integration","Harmony on sample; \u03b8 2/5/10/20 (+50); best mixing \u03b8=5"),
 ("Embedding","n_pcs swept 20/30/40 (committed 30); n_neighbors=30; spread=1.3"),
 ("Gate-1 metric","per-neighbourhood iLISI (max 2.26) + UMAP-radius-graph components"),
 ("Module means (raw)","Gast \u22120.020 \u00b7 pSom +0.031 \u00b7 Crest +0.013"),
 ("Geometry","NA \u2014 no trajectory fit (Gate 1 NO-GO)"),
 ("EMT-TFs shown","SNAI2 (11.3%) \u00b7 FOXC1 (10.4%); FOXC/PRRX in panel"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Qian 2020 breast cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
