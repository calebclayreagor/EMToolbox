import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Pancreas/Steele2020_Pancreas"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Pancreas/Steele2020_Pancreas"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "13/13 samples (\u2265117 cells) intermix on one continuous manifold with no per-patient islands "
  "(radius-graph: 0 detached; iLISI median 1.00\u21925.15 of 13); both lobes (Ductal-classical 6,782 / "
  "Stress-UPR 1,092) carry the trajectory."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single dominant pSom\u2192Crest axis: pSom high over the classical-ductal body declines along pseudotime "
  "(\u03c1=\u22120.70); Crest anti-correlated (r=\u22120.69), rising to a terminal readout (\u03c1=+0.74; crest-high "
  "decile mean pt=0.87). Gast weakly structured (early programme, spent); joint pSom&Crest-high depleted "
  "(enrichment 0.44) \u2014 an inverse gradient, not a co-expression hub."),
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
dataset=("PDAC (Steele et al., 2020), 10x \u2014 16 patients / 48,570 cells (master scope); malignant only: 7,874 "
 "cells across 13 malignant-bearing samples (all clear the \u2265100 floor) enter preprocessing; the whole malignant "
 "manifold (no lobe scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Steele's PDAC malignant manifold "
 "is a single monotone somitogenesis \u2192 terminal-neural-crest gradient (classical-ductal body \u2192 "
 "neural-crest-like terminus), matching the developmental axis; it lacks Puram's hub-and-spoke bifurcation, so Gate 3 "
 "has no hub to test. The axis spans both transcriptional lobes (orthogonal to cell cycle; module\u2013cyc "
 "|\u03c1|\u22640.08), so the whole manifold is kept (Bischoff/Sun/Lee no-scoping precedent). Unlike Zhou, cell cycle "
 "does not define the lobes (PDAC ~94% non-cycling) and pseudotime is uncorrelated with cycling (\u03c1=+0.02), so no "
 "proliferation caveat applies. The raw module means (Gast \u22120.04 / pSom +0.08 / Crest \u22120.05) nearly match the "
 "failed Peng 2019 PDAC run, but the geography differs: Peng showed three mutually-exclusive territories with no "
 "terminal readout (NO-GO), whereas Steele shows a coherent terminal-crest gradient (GO) \u2014 the gate turns on "
 "geometry, not means. EMT-TFs FOXC1 (early/root) \u2192 ZEB2 (late/terminus); canonical SNAI1/ZEB1 near the detection "
 "floor; EMT-TF end-separation weak (\u0394pt=0.12).")
params=[
 ("Min cells/sample","\u2265100 floor (13/13; gap degenerate)"),
 ("Integration","Harmony \u03b8=10; PCA50; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Root node","tip 2 = pSom-high, Crest-low"),
 ("Compartments","Ductal-cl. 6,782 / Stress-UPR 1,092"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Steele 2020 PDAC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
