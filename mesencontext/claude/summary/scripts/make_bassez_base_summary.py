import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Bassez2021_Breast"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Bassez2021_Breast"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Harmony(\u03b8=10) integrates all 41 samples: same-sample neighbour fraction 0.37 \u2192 0.21, iLISI median 5.51 "
  "\u2192 9.10 of 41. One connected component (45 cells / 27 specks removed). Read on the regenerated embedding + "
  "per-neighbourhood iLISI, not a scalar: mixed AND continuous."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Non-branching case: a single (Gast/pSom)\u2192Crest developmental gradient. Gast & pSom co-vary (smoothed "
  "r=\u22120.21), both oppose Crest (pSom\u2194Crest r=\u22120.82, Gast\u2194Crest r=\u22120.24). Along pseudotime "
  "Gast/pSom fall (\u03c1 \u22120.11/\u22120.32), Crest rises (\u03c1 +0.32) to the terminal lobe. Joint pSom&Crest "
  "enrichment 0.23 (<1 = inverse gradient, not a co-expression hub)."),
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
dataset=("Breast tumours (Bassez et al., 2021), 10x \u2014 65,837 malignant cells / 41 samples; single low-cycling "
 "body (2% cycling).")
verdict=("Pattern reproduces in the non-branching form (Linear-pSom/Crest): one continuous "
 "gastrulation/somitogenesis \u2192 neural-crest axis, Crest terminal. Gate 1 GO / Gate 2 GO / Gate 3 NA. "
 "EMT-TFs ZEB2 (root) \u2192 PRRX1 (terminus).")
params=[
 ("Sample threshold","geom-mean of 92\u21923 cliff = 16 (drops 3-cell BIOKEY_34) \u2192 41/42 samples"),
 ("Overdispersed genes","2,498 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample, \u03b8=10 (mixing flat across sweep)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 45 cells / 27 islands removed \u2192 65,837"),
 ("Geometry","Non-branching \u2192 scFates curve (ElPiGraph) N=20 \u03bb=0.3 \u03bc=100; 2 tips/0 forks, SA 2.53"),
 ("Root","tip 2 = Gast/pSom-high, Crest-low origin"),
 ("Module means (raw)","Gast \u22120.014 \u00b7 pSom +0.022 \u00b7 Crest \u22120.005 (Linear-pSom/Crest)"),
 ("EMT-TFs shown","ZEB2 (root, \u03c1 \u22120.07) \u2194 PRRX1 (terminus, \u03c1 +0.07); detection-gated"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Bassez 2021 Breast \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
