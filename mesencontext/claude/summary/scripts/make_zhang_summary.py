import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Ovarian/Zhang2022_Ovarian"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Ovarian/Zhang2022_Ovarian"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "20/22 samples (\u226541 cells) / 11 patients intermix on one continuous manifold with no per-patient islands "
  "(radius-graph: 0 detached); both lobes (Body 8,002 / Terminal cap 756) carry the trajectory."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.55) and decline along pseudotime (\u03c1=\u22120.65/\u22120.80); Crest anti-correlated "
  "(r=\u22120.83/\u22120.82), rising to a terminal readout (\u03c1=+0.87; crest-high decile mean pt=0.94)."),
 ("Gate 3 — hub mutual exclusivity","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub, so there is no branch pair to test for "
  "mutual exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("High-Grade Serous Ovarian Carcinoma (Zhang et al., 2022), 10x \u2014 22 samples / 11 patients / 51,786 "
 "cells (master scope); malignant only: 8,806 load, 8,758 across 20 samples (\u226541) enter preprocessing; the "
 "whole malignant manifold (no lobe scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Zhang's HGSOC malignant manifold "
 "is a single monotone Gast/pSom \u2192 terminal-Crest gradient (non-branching), matching the developmental axis; it "
 "lacks Puram's hub-and-spoke bifurcation, so Gate 3 has no hub to test. The developmental axis is orthogonal to "
 "cycling (\u03c1=\u22120.003) \u2014 no proliferation confound, and both lobes are low-cycling, so the whole manifold is "
 "kept (Bischoff/Sun no-scoping precedent). EMT-TFs SNAI1 (early/root) \u2192 PRRX2 (late/terminus); canonical "
 "ZEB1/TWIST near the detection floor (6.5%/3.1%); EMT-TF end-separation weak (\u0394pt=0.29).")
params=[
 ("Min cells/sample","\u226541 (20/22; gap 57\u219230)"),
 ("Integration","Harmony \u03b8=5; PCA 50PC; spread=1.3"),
 ("Scope","whole manifold (no lobe scoping)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Compartments","Body 8,002 / Terminal cap 756"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Zhang 2022 HGSOC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
