import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Karaayvas2018_Breast-1"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Karaayvas2018_Breast-1"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) on sample: per-neighbourhood same-sample fraction 0.82\u21920.27 (chance 0.20); iLISI 1.5\u21924.1 of 5 "
  "samples. One connected component, 0 detached islands. Five samples intermix across a single continuous cloud \u2014 GO."),
 ("Gate 2 — module geography","NO-GO",RED,
  "Module geography is ABSENT in the raw per-cell scores (Gast~pt \u03c1=\u22120.08, pSom +0.02, Crest \u22120.03) and appears only "
  "after graph-smoothing. A permutation null (360 cells) gives 95% CI \u00b10.9; every smoothed gradient is non-significant "
  "(p\u22650.26). Tell: smoothing FLIPS the sign of the one real raw signal (Crest\u2194Gast \u22120.43\u2192+0.44, Crest\u2194pSom "
  "\u22120.55\u2192+0.10) \u2014 fabricated, not latent. Pattern absent."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Non-branching topology (curve: 2 tips, 0 forks across N=15/20/30; PPT tree forks unstable 1\u20134 = spurious in a "
  "diffuse cloud). No bifurcation to test \u2014 NA."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (TNBC) (Karaayvas et al., 2018), SmartSeq2 \u2014 365 malignant cells (6 samples reported) \u2192 360 "
 "analysed (5 samples \u226510 cells). Sparse plate-based data. A trajectory is fit, but the module pattern is absent "
 "(Gate 2 NO-GO).")
verdict=("Pattern does NOT reproduce. Gate 1 holds (360 cells intermix on one continuous manifold), but the "
 "embryonic-module geography is absent at single-cell resolution: raw pseudotime gradients are ~0 and the smoothed "
 "structure is a graph-smoothing artifact (null 95% CI \u00b10.9, all p\u22650.26; smoothing flips the raw Crest signs). "
 "Gate 2 NO-GO, Gate 3 NA. EMT-TFs SNAI1 (early/root) \u2192 FOXC1 (late/terminus).")
params=[
 ("Threshold","\u226510 cells/sample (SmartSeq2 scale; floor 100 keeps only 1/6); cliff 31\u21925 \u2192 5/6, 360 cells"),
 ("Embedding","Harmony \u03b8=10; n_pcs=20, n_neighbors=30, spread=1.3; 51 HVG"),
 ("Trajectory","scFates curve (non-branching), N=20, \u03bb=0.3, \u03bc=100; fold-free (2.97)"),
 ("Root","Gast/pSom-high, Crest-low tip; not proliferation-rooted (pt\u2013cycling \u03c1=+0.18)"),
 ("Geometry","Gate 2 NO-GO \u2014 module pattern absent at single-cell resolution"),
 ("EMT-TFs","SNAI1 (early/root) \u2192 FOXC1 (late/terminus); 10-TF panel, VIM excluded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Karaayvas 2018 TNBC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
