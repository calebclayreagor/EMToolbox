import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Griffiths2021_Breast"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Griffiths2021_Breast"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Samples/patients intermix per-neighbourhood on ONE connected manifold. Harmony(sample) same-sample neighbour "
  "fraction 0.91 \u2192 0.17 (\u03b8=5); iLISI 1.0 \u2192 13.4 of 67 samples. ~1,100 detached cells (1.0%) removed as "
  "islands; largest component retained. Mixed AND continuous."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Single Gast/pSom \u2192 Crest axis, no hub diverging into two arms. Organized Gast\u2194pSom cross-repression "
  "(smoothed r=\u22120.42); Crest an inverse terminal gradient (Crest vs pSom r=\u22120.76; NC-high decile at "
  "pseudotime 0.77; joint pSom&Crest enrichment 0.31 < 1). Curve fits clean (2 tips, 0 forks, fold-free); PPT "
  "tree only over-fragments (5\u201313 forks). Crest does NOT enrich a Gast arm (no arms) \u2014 no flag."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "No bifurcation (non-branching geometry) \u2192 branching-only Gate 3 not evaluated; 04_correlation / 05_modules "
  "not produced (spec \u00a76)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (Griffiths et al., 2021), 10x + iCell8 \u2014 108,849 malignant cells on the trajectory "
 "(67/95 samples, 110,195 cells loaded; two technology leaves 10X 110,568 + iCell8 804, concatenated on 15,691 "
 "shared genes; a 246-cell iCell8/cycling lobe scoped out).")
verdict=("The embryonic-program pattern reproduces as the non-branching case: one continuous, sample-integrated "
 "gastrulation/somitogenesis \u2192 neural-crest axis with organized Gast\u2194pSom cross-repression and terminal "
 "Crest \u2014 no Gast/pSom hub bifurcating into two competing arms. Gate 1 GO / Gate 2 GO / Gate 3 NA. EMT-TFs "
 "ZEB1, ZEB2 expressed but flat along pseudotime (|\u03c1|<0.05); overlay the two most-expressed non-directionally.")
params=[
 ("Min-cell threshold","\u2265100 (depth-invariant floor; no dominant cliff) \u2192 67/95 samples, 110,195 cells"),
 ("Technology","10X 110,568 + iCell8 804 malignant, concatenated on 15,691 shared genes"),
 ("Embedding","n_pcs=30, Harmony(sample) \u03b8=5, spread=1.3, k=30"),
 ("Trajectory","scFates curve N=20, non-branching; fold self-approach 2.95 (fold-free)"),
 ("Compartment","246-cell lobe (100% iCell8, 70% cycling) scoped out as technology/cycling confound"),
 ("Root","curve tip 0 (Gast/pSom-high, Crest-low); axis cell-cycle-free (pt vs cycling r=\u22120.04)"),
 ("Geometry","Linear-pSom/Crest (global means Gast \u22120.021, pSom \u22120.052, Crest +0.021)"),
 ("EMT-TFs","ZEB1, ZEB2 expressed but flat (|\u03c1|<0.05); overlay non-directionally; VIM excluded"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Griffiths 2021 Breast \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
