import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Skin/Ji2020_Skin"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Ji2020_Skin"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "8 patients share one continuous, sample-mixed manifold (Harmony \u03b8=10); detached islands removed."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Gast+pSom co-vary (r=+0.13) and both oppose Crest (Gast~Crest=\u22120.70, pSom~Crest=\u22120.64): one developmental "
  "axis with an inverse terminal Crest gradient (non-branching)."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Branching-only test; manifold is non-branching (principal curve: 2 tips, 0 forks) \u2014 not applicable."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Cutaneous Squamous-Cell Carcinoma (Ji et al., 2020) \u2014 10,531 malignant keratinocytes from 8 cSCC "
 "patients (published malignant calls; thin samples removed by a data-driven multiplicative-gap threshold). "
 "Harmony integration on patient (\u03b8=10), principal-curve trajectory (ElPiGraph) on the whole manifold. Module "
 "means: Gast \u22120.032, pSom +0.042, Crest +0.023 \u2014 pSom/Crest globally stronger than Gast.")
verdict=("Non-branching \u2014 Linear pSom/Crest. A single developmental axis: a Gast/pSom-high "
 "differentiating-keratinocyte body (trajectory root) grading into a neural-crest-high basal/TSK leading edge "
 "(terminus). Along pseudotime Gast (\u03c1=\u22120.51) and pSom (\u03c1=\u22120.44) fall while Crest (\u03c1=+0.37) rises. "
 "The axis is verified separable from proliferation (Gast/pSom\u2194Crest opposition survives partialling the "
 "cell-cycle score). Gate 1 GO, Gate 2 GO, Gate 3 NA. EMT-TFs FOXC1 (early) \u2192 SNAI2 (late).")
params=[
 ("Malignant cells","10,531 (8/10 patients kept)"),
 ("Sample threshold","multiplicative-gap geomean (drops P3, P5)"),
 ("Integration","Harmony on patient, \u03b8=10 (mixing-sweep selected)"),
 ("Embedding","PCA 20 PC \u00b7 neighbours 30 \u00b7 UMAP spread 1.3"),
 ("Trajectory","ElPiGraph curve \u00b7 Nodes=20 \u00b7 \u03bb=0.3 \u00b7 \u03bc=100"),
 ("Topology","2 tips, 0 forks \u00b7 fold-free (self-approach>1)"),
 ("Root","Gast/pSom-high, Crest-low tip (data-derived)"),
 ("Modules","Gast 76/81 \u00b7 pSom 88/98 \u00b7 Crest 101/104 genes"),
 ("EMT-TF pair","FOXC1 (early) \u2192 SNAI2 (late)"),
 ("Scope","whole manifold (holds low-cycling too)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Ji 2020 cSCC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
