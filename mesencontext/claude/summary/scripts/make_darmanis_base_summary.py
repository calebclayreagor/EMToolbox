import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Brain/Darmanis2017_Brain"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Darmanis2017_Brain"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "4 samples intermix per-neighbourhood (iLISI 1.09\u21922.89 of 4) on one continuous manifold (single kNN "
  "component, 0 islands); no per-patient islands."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.66) and both oppose Crest (\u22120.97 / \u22120.75): one developmental axis, Crest an "
  "inverse terminal gradient. Non-branching case."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "No bifurcation (curve: 2 tips, 0 forks, fold-free across params) \u2192 not tested."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Glioblastoma (Darmanis et al., 2017), SmartSeq2 (TPM) \u2014 1,091 malignant cells (4/4 samples).")
verdict=("The embryonic-program pattern REPRODUCES as the non-branching case: a single continuous "
 "gastrulation/somitogenesis \u2192 neural-crest developmental axis, rooted at the Gast/pSom-high pole with Crest "
 "as an inverse terminal gradient. No Gast\u2013pSom bifurcation. Gate 1 GO / Gate 2 GO / Gate 3 NA. "
 "Linear-pSom/Crest geometry (pSom \u03bc=+0.44 strongest). EMT-TFs ZEB2 (root-trending) \u2192 TWIST1 "
 "(terminus-trending).")
params=[
 ("Min-cell threshold","\u2265100 \u2192 4/4 samples, 1,091 cells (counts 531/268/163/129; ratios <2)"),
 ("Expression format","matrix pre-log-normalized (range 0.7\u201318.7); undo loader's 2nd log1p (expm1)"),
 ("Genes / embedding","139 overdispersed (GAM); n_pcs=20; Harmony \u03b8=10"),
 ("Islands removed","0 (single connected kNN component; radius-graph = 1 component)"),
 ("Geometry","Non-branching \u2014 scFates curve N=20 \u03bb=0.3 \u03bc=100; 2 tips, 0 forks, fold-free (2.68)"),
 ("Root","curve tip 0 \u2014 Gast/pSom-high, Crest-low origin (Crest late)"),
 ("EMT-TFs","ZEB2 (51%, root-trending) \u00b7 TWIST1 (18%, terminus-trending); Snail/FoxC near-absent"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Darmanis 2017 Glioblastoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
