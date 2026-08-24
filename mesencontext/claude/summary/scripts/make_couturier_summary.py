import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Brain/Couturier2020_Brain"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Couturier2020_Brain"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) on sample integrates 10 patient tumours: sample iLISI 1.16\u21924.43 of 10 (plateau; peaks at "
  "\u03b8=10). One connected component, 0 detached islands. Judged on the regenerated embedding + per-neighbourhood "
  "iLISI: malignant structure is mixed AND continuous."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching: a single Gast/pSom \u2192 Crest axis. Gast & pSom co-vary (smoothed r=+0.53), both oppose Crest "
  "(Gast\u2194Crest r=\u22120.73, pSom\u2194Crest r=\u22120.81). Along pseudotime Gast/pSom fall (\u03c1 \u22120.48 / \u22120.41), Crest rises to a "
  "terminal tip (Crest-high decile mean pseudotime = 0.94)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable: the manifold is non-branching (principal curve, 2 tips / 0 forks), so there is no Gast/pSom-opposed "
  "bifurcation to test. Branching-only correlation / modules notebooks are not produced (per spec section 6)."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Glioblastoma (Couturier et al., 2020), 10x \u2014 16,804 malignant cells (10 patient tumours). Non-branching "
 "Linear-pSom/Crest.")
verdict=("Pattern reproduces (non-branching, Linear-pSom/Crest): one continuous gastrulation/somitogenesis \u2192 "
 "neural-crest axis rooted at the Gast/pSom-high origin, Crest terminal. G1 GO / G2 GO / G3 NA. EMT-TFs ZEB1 + PRRX1 "
 "(both terminus-enriched; no root-end factor).")
params=[
 ("Sample threshold","\u2265418 cells (536\u2192327 gap, ratio 1.64); 10/29 samples, 16,804 cells"),
 ("Gene selection / PCA","scFates find_overdispersed = 2,963 genes; PCA 50 comps"),
 ("Integration","Harmony on sample \u03b8=10 (iLISI 1.16\u21924.43 plateau)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 0 islands removed"),
 ("Geometry","Non-branching; scFates curve N=20, \u03bb=0.3, \u03bc=100 (2 tips / 0 forks)"),
 ("Root node","curve tip 0 = Gast/pSom-high, Crest-low (developmental origin)"),
 ("Module means (raw)","Gast +0.004 \u00b7 pSom +0.077 \u00b7 Crest \u22120.044 (pSom strongest)"),
 ("EMT-TFs","ZEB1 + PRRX1 (both terminus-enriched, distinct families); no root factor"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Couturier 2020 GBM \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
