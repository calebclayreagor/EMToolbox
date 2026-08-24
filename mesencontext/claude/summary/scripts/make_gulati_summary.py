import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Gulati2020_Breast-1"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Gulati2020_Breast-1"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "7/8 samples (\u226554 cells) intermix on one continuous manifold with no per-patient islands (radius-graph: 0 detached; "
  "iLISI median 2.47\u21924.79 of 7); both lobes (Low-cycling 513 / High-cycling 305) carry the trajectory."),
 ("Gate 2 — module geography","NO-GO",RED,
  "Developmental geography is ABSENT in raw per-cell scores (Gast\u2194pSom = \u22120.02) and appears only after graph-"
  "smoothing. A permutation null (smoothing random scores on the same graph) reproduces it: smoothed \u22120.77 within null "
  "95% CI \u00b10.7; the defining terminal-Crest gradient (\u03c1=+0.73) is non-significant (p=0.14). The programs are present "
  "but not organised into a developmental axis \u2014 pattern absent."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not reached \u2014 Gate 2 NO-GO halts the gate chain; branching-only, and there is no bifurcation or Mixed-type hub to "
  "test."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (Gulati et al., 2020), SmartSeq2 \u2014 15 samples / 1,902 cells (master scope); malignant only: "
 "861 load, 818 across 7 samples (\u226554) enter preprocessing; whole malignant manifold (no lobe scoping). A trajectory "
 "is fit, but the module pattern is absent (Gate 2 NO-GO).")
verdict=("Pattern does NOT reproduce \u2014 Gate 1 GO, Gate 2 NO-GO, Gate 3 NA. Gate 1 holds (818 cells intermix on one "
 "continuous manifold), but the embryonic-module geography is absent at single-cell resolution: raw Gast\u2194pSom = \u22120.02 "
 "(no cross-repression), and the smoothed structure (\u22120.77; terminal Crest \u03c1=+0.73) is not distinguishable from a "
 "graph-smoothing artifact \u2014 a permutation null on this 818-cell SmartSeq2 graph gives 95% CI \u00b10.7, terminal-Crest "
 "non-significant (p=0.14). EMT-TFs (unconditional step) ZEB2 (early) \u2192 SNAI2 (late).")
params=[
 ("Min cells/sample","\u226554 (7/8; gap 68\u219243)"),
 ("Scope","whole manifold (no scoping)"),
 ("Root node","tip 2 (pSom/Gast-high)"),
 ("Integration","Harmony \u03b8=2; PCA20; spread=1.3"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100 (PPT forks unstable 2\u21928)"),
 ("Compartments","Low-cyc 513 / High-cyc 305 (cell cycle orthogonal, |r|\u22640.03)"),
 ("EMT-TFs","ZEB2 (early) \u2192 SNAI2 (late); mesenchymal factors lean crest-terminal"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Gulati 2020 breast cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
