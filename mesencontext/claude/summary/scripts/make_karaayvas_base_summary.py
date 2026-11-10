import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Karaayvas2018_Breast"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Karaayvas2018_Breast"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Harmony(\u03b8=5) integrates all 5 patients: same-sample neighbour fraction 0.82 \u2192 0.28 (null 0.25), iLISI "
  "median 1.97 \u2192 4.12 of 5. One connected component (0 islands). Judged on the regenerated embedding + "
  "per-neighbourhood iLISI, not a scalar: samples intermix AND the manifold is continuous."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Non-branching case: a single pSom-origin \u2192 terminus developmental gradient. pSom falls along pseudotime "
  "(\u03c1 \u22120.41); Gast & Crest both rise to the terminal tip (\u03c1 +0.79 / +0.82; Crest decile pt=0.98). Joint "
  "pSom&Crest enrichment 0.37 (<1 = inverse terminal gradient, not a co-expression hub). FLAG (pass anyway): "
  "Crest co-enriches the Gast pole (smoothed Gast\u2194Crest r=+0.59), an inversion of the expected pSom-arm Crest "
  "\u2014 Gast, not pSom, tracks the neural-crest terminus here."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks, fold-free). No "
  "bifurcation, so the branching-only hub cross-repression test is not run (correlation / modules notebooks not "
  "produced, per spec)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Triple-negative breast cancer (Karaayvas et al., 2018), SmartSeq2 \u2014 360 malignant cells over 5 "
 "patients; single low-cycling body (~14% cycling), cell-cycle-free axis (pseudotime vs cycling \u03c1 \u22120.19).")
verdict=("Pattern reproduces in the non-branching form (Linear-pSom/Crest): one continuous somitogenesis-origin "
 "\u2192 neural-crest terminus axis. Gate 1 GO / Gate 2 GO / Gate 3 NA, with the Crest-arm inversion flagged (Crest "
 "tracks the Gast terminus). EMT-TFs FOXC1 (early/root) \u2192 SNAI1 (late).")
params=[
 ("Sample threshold","\u226512 (geom-mean of 31\u21925 cliff, ratio 6.2) \u2192 5/6 samples, 360 cells"),
 ("Overdispersed genes","51 (scFates find_overdispersed; sparse SmartSeq2)"),
 ("Integration","Harmony on sample, \u03b8=5 (mixing near null then flattens)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 1 component, 0 islands removed"),
 ("Geometry","Non-branching scFates curve N=20 \u03bb=0.3 \u03bc=100; 2 tips/0 forks, SA 2.91; corr(x,t)=0.97"),
 ("Root","tip 2 = Crest-low, pSom-high origin"),
 ("Module means (raw)","Gast \u22120.220 \u00b7 pSom +0.106 \u00b7 Crest \u22120.067 (Linear-pSom/Crest)"),
 ("EMT-TFs shown","FOXC1 (early/root, 33%) \u2194 SNAI1 (late/terminus); detection-gated"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Karaayvas 2018 TNBC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
