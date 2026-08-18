import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Lung/Maynard2020_Lung"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Lung/Maynard2020_Lung"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "7/38 samples (\u2265100 cells) intermix on one continuous manifold with no per-patient islands: an integration sweep "
  "(\u03b8 5\u219240) read on the embedding gives one connected component at \u03b8=20 (iLISI median 1.00\u21922.00 of 7); \u03b8=40 "
  "over-integrates into detached islands. Both poles (Body / Terminus) carry the trajectory."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast and pSom co-vary (r=+0.43) at one origin pole; both oppose Crest (r=\u22120.74 / \u22120.64). Along pseudotime "
  "Gast/pSom decline (\u03c1=\u22120.64 / \u22120.63) and Crest rises to a terminal readout (\u03c1=+0.79; Crest-high decile mean "
  "pt=0.83). Joint pSom&Crest-high depleted (enrichment 0.29) \u2014 an inverse gradient, not a co-expression hub; Crest "
  "enriches the pSom/Gast-low pole, so no inversion flag."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Single monotone axis \u2014 0 branch nodes (curve & PPT tree), fold-free (self-approach 2.96), and no Gast/pSom-overlap "
  "hub, so there is no branch pair to test for mutual exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("LUAD (Maynard et al., 2020), SmartSeq2 \u2014 50 samples / 19,777 cells (master scope); malignant only: 3,184 "
 "cells; after \u2265100-cell thresholding 2,486 cells across 7 tumour-bearing samples and island removal 2,396 cells "
 "enter the trajectory (whole manifold, no scoping).")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Maynard\u2019s metastatic-LUAD malignant "
 "manifold is a single monotone Gast/pSom \u2192 terminal-neural-crest gradient (somitogenesis-high origin \u2192 "
 "neural-crest-like terminus), matching the developmental axis; it lacks Puram\u2019s hub-and-spoke bifurcation, so "
 "Gate 3 has no hub to test. The published cell-cycle annotation is NaN for malignant cells, so cycling was scored "
 "de novo; it is diffuse (22%), the modules are cell-cycle-free (Gast 0/81, Crest 0/104 cell-cycle genes), "
 "pSom\u2194Crest anti-correlation survives in non-cycling cells (r=\u22120.64\u2192\u22120.67) and pseudotime\u2194cycling co-variation "
 "is negligible (\u03c1=\u22120.04) \u2014 the axis is developmental, not proliferative. FOXC1 (42% expressing, \u03c1=+0.15) is the "
 "robust neural-crest terminus factor; the root end is weakly marked \u2014 only ZEB2 (~3%, at the detection floor) "
 "surfaces as an early factor and its call is run-sensitive.")
params=[
 ("Min cells/sample","\u2265100 floor (7/38; gap non-dominant)"),
 ("Integration","Harmony \u03b8=20; PCA50; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","tip = Gast/pSom-high, Crest-low"),
 ("Poles","Body 1,198 / Terminus 1,198"),
 ("Geometry","Linear (non-branching); 0 branch nodes"),
 ("EMT-TFs","ZEB2 (early/root) \u00b7 FOXC1 (terminus, 42%)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Maynard 2020 LUAD \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
