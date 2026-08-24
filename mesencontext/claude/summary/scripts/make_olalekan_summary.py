import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Ovarian/Olalekan2021_Ovarian"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Ovarian/Olalekan2021_Ovarian"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) integrates all 6 patients: same-sample neighbour fraction 0.96\u21920.38, iLISI median 1.00\u21923.99 "
  "of 6. One connected component (0 islands). Read on the regenerated embedding + per-neighbourhood iLISI, not a "
  "scalar: mixed AND continuous."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching case: a single (Gast/pSom)\u2192Crest developmental gradient. Gast & pSom co-vary (smoothed r=+0.80), "
  "both oppose Crest (pSom\u2194Crest r=\u22120.85, Gast\u2194Crest r=\u22120.72). Along pseudotime Gast/pSom fall (\u03c1 \u22120.77/\u22120.64), "
  "Crest rises to a terminal tip (decile pt=0.99). Joint pSom&Crest enrichment 0.35 (<1 = inverse gradient, not a "
  "co-expression hub)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks). No bifurcation, so the "
  "branching-only hub cross-repression test is not run (correlation / modules notebooks are not produced, per the "
  "deliverable spec)."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("HGSOC omental metastases (Olalekan 2021), Drop-seq, 4,125 malignant cells over 6 patients; single "
 "low-cycling body (~5% cycling).")
verdict=("Pattern reproduces in the non-branching form (Linear-pSom/Crest): one continuous gastrulation/somitogenesis "
 "\u2192 neural-crest axis, Crest terminal. G1 GO / G2 GO / G3 NA. EMT-TFs SNAI2 (early) \u2192 ZEB1 (terminus).")
params=[
 ("Sample threshold","\u2265100 cells (no dominant cliff, ratio 1.13); 6/6 samples, 4,125 cells"),
 ("Overdispersed genes","381 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample, \u03b8=10 (mixing plateau)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 0 islands removed"),
 ("Geometry","Non-branching; scFates curve N=20, \u03bb=0.3, \u03bc=100 (2 tips / 0 forks)"),
 ("Root","tip 0 = Gast/pSom-high, Crest-low (developmental origin)"),
 ("Module means (raw)","Gast +0.018 \u00b7 pSom +0.027 \u00b7 Crest \u22120.028 (Linear-pSom/Crest)"),
 ("EMT-TFs","SNAI2 (early/root) \u2194 ZEB1 (late/terminus); FOXC/PRRX in panel"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Olalekan 2021 HGSOC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
