import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Zhang2019_Hematologic"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Zhang2019_Hematologic"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Harmony(\u03b8=10) integrates the clonal FL batch: same-sample neighbour fraction 0.975 \u2192 0.453, iLISI median "
  "1.00 \u2192 2.26 of 4. One connected component (0 islands). \u03b8=2 leaves a per-patient archipelago; judged on the "
  "regenerated embedding + per-neighbourhood iLISI, not a scalar: mixed AND continuous."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Non-branching case: a single (Gast/pSom)\u2192Crest developmental gradient. Gast & pSom overlap at the origin "
  "(joint enrichment 1.00, smoothed r=\u22120.16), both oppose Crest (Gast\u2194Crest r=\u22120.55, pSom\u2194Crest "
  "r=\u22120.58). Along pseudotime Gast falls (\u03c1 \u22120.48), Crest rises to a terminal tip (decile pt=0.58). Joint "
  "pSom&Crest enrichment 0.23 (<1 = inverse gradient, not a co-expression hub)."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks). No bifurcation, so the "
  "branching-only hub cross-repression test is not run (correlation / modules notebooks not produced, per spec)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Follicular lymphoma malignant B-cell compartment (Zhang et al., 2019), 10x \u2014 5,645 malignant cells over "
 "4 samples / 2 patients (primary + progressed/transformed); single low-cycling body (~14% cycling).")
verdict=("Pattern reproduces in the non-branching form (Linear-Gast): one continuous gastrulation \u2192 neural-crest "
 "axis, Crest terminal, Gast globally strongest. Gate 1 GO / Gate 2 GO / Gate 3 NA. EMT-TFs ZEB2 & ZEB1 (both "
 "terminus-loaded, ZEB2 earlier).")
params=[
 ("Sample threshold","\u2265100 (floor; largest gap ratio 2.74, no dominant cliff) \u2192 4/4 samples, 5,645 cells"),
 ("Overdispersed genes","636 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample, \u03b8=10 (mixing improves monotonically; clonal FL patient batch)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 0 islands removed"),
 ("Geometry","Non-branching scFates curve N=20 \u03bb=0.3 \u03bc=100; 2 tips/0 forks, SA 2.96; pt vs cycling \u03c1=+0.29"),
 ("Root","tip 2 = Gast/pSom-high, Crest-low origin"),
 ("Module means (raw)","Gast +0.012 / pSom +0.006 / Crest +0.009 (Gast strongest \u2192 Linear-Gast)"),
 ("EMT-TFs shown","ZEB2 & ZEB1 (>3% detected; both terminus-loaded, ZEB2 earlier; no root-loaded TF)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Zhang 2019 Follicular Lymphoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
