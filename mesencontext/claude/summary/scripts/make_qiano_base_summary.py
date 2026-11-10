import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Ovarian/Qian2020_Ovarian"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Ovarian/Qian2020_Ovarian"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Harmony(\u03b8=20) interleaves all 4 patients: same-sample neighbour fraction 1.00 \u2192 0.63 (chance 0.35), "
  "iLISI median 1.00 \u2192 2.13 of 4. \u03b8=30 REVERSES mixing to 0.88 (over-integration fragments into per-sample "
  "lobes), so \u03b8=20 is the strongest integration on the plateau. 97 cells / 1 detached island removed \u2192 one "
  "connected component. Read on the regenerated embedding + iLISI: mixed AND continuous."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Non-branching case: a single (Gast/pSom)\u2192Crest developmental gradient. Gast & pSom co-express (joint "
  "enrichment 1.20 > 1; smoothed r=+0.14), and both oppose Crest (Gast\u2194Crest r=\u22120.28, pSom\u2194Crest "
  "r=\u22120.26; joint enrichment 0.58 / 0.63 < 1 = inverse, not a co-expression hub). Along pseudotime Gast/pSom "
  "fall (\u03c1 \u22120.46 / \u22120.55), Crest rises to a terminal tip (high-decile pt = 0.83)."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks, fold self-approach 2.41). "
  "No bifurcation, so the branching-only hub cross-repression test is not run (correlation / modules notebooks "
  "not produced, per spec)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Ovarian cancer (Qian et al., 2020), 10x \u2014 6,393 malignant cells over 4 treatment-naive patients; one "
 "continuous low-confound body (embryonic modules proliferation-independent).")
verdict=("Pattern reproduces in the non-branching form (Linear-pSom/Crest): one continuous "
 "gastrulation/somitogenesis \u2192 neural-crest axis, Crest terminal. Gate 1 GO / Gate 2 GO / Gate 3 NA. EMT-TFs "
 "PRRX1 (early/root) \u2192 PRRX2 (late/terminus).")
params=[
 ("Sample threshold","\u2265100 cells (floor; no dominant cliff, ratio 1.89) \u2192 4/4 samples, 6,490 cells"),
 ("Overdispersed genes","1,013 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample, \u03b8=20 (mixing plateau; \u03b8=30 over-integrates and fragments)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 97 cells / 1 island removed \u2192 6,393"),
 ("Geometry","Non-branching \u2192 scFates curve (ElPiGraph) N=20 \u03bb=0.3 \u03bc=100; 2 tips/0 forks, SA 2.41"),
 ("Root","tip 0 = Gast/pSom-high, Crest-low origin; corr(x_lin,pt)=+0.83"),
 ("Module means (raw)","Gast +0.042 \u00b7 pSom +0.065 \u00b7 Crest \u22120.019 (Linear-pSom/Crest)"),
 ("EMT-TFs shown","PRRX1 (early/root, \u03c1 \u22120.19) \u2194 PRRX2 (late/terminus, \u03c1 +0.00); detection-gated"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Qian 2020 Ovarian \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
