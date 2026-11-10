import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Lung/Chan2021_Lung"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Lung/Chan2021_Lung"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "24/34 samples pass the mult-gap threshold (\u226537 cells); 50,886 malignant cells share one continuous, "
  "isotropic manifold (UMAP aspect 1.04). Samples & SCLC-A/N/P subtypes intermix (\u03b8 sweep 0.83\u21920.22); "
  "cell-cycle confound regressed out (mean |corr| 0.32\u21920.01)."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Single monotone axis: Gast & pSom co-vary (r=+0.73) and decline from the root (\u03c1 \u22120.24/\u22120.45); Crest "
  "opposes both (r=\u22120.71/\u22120.88) and rises to a terminal readout (\u03c1 +0.24). No bifurcation."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Non-branching manifold has no bifurcation/hub, so the cross-repression test does not apply."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Small-cell lung cancer (Chan et al., 2021), 10x. Master scope 37 patients / 86,662 cells; malignant "
 "compartment 51,052 cells (SCLC-A/N/P + minor NSCLC); 50,886 across 24 samples enter the trajectory.")
verdict=("Pattern reproduces as the non-branching case (Gate 1 GO / Gate 2 GO / Gate 3 NA): a single monotone "
 "gastrulation/somitogenesis \u2192 terminal neural-crest gradient, not resolved into Puram\u2019s two competing "
 "arms. SCLC is intensely proliferative, so a raw-embedding curve tracks cell cycle (\u03c1 \u22120.79); regressing "
 "the cell-cycle scores out (post \u03c1=0.00) recovers developmental order. EMT SNAI1 \u2192 ZEB1.")
params=[
 ("Min cells/sample","\u226537 (mult-gap 92\u219215; keeps 24/34)"),
 ("Cell-cycle","G1S+G2M regressed out (0.32\u21920.01)"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Integration","Harmony \u03b8=5; PCA50\u219220; spread=1.3"),
 ("Trajectory","scFates curve N=30 \u03bb=0.3 \u03bc=100 (SA 2.06)"),
 ("EMT-TFs","SNAI1 (root) \u2192 ZEB1 (terminus)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Chan 2021 SCLC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
