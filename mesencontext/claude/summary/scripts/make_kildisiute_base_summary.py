import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Neuroendocrine/Kildisiute2021_Neuroendocrine"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Neuroendocrine/Kildisiute2021_Neuroendocrine"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "2 populated samples (\u2265101 cells) intermix on one continuous manifold with no per-patient islands "
  "(radius-graph: 0 detached). Manifold resolves into two lobes; trajectory is scoped to the Embryonic lobe "
  "(1,504) \u2014 the Cycling lobe (216) confounds Gast with proliferation."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.91); along pseudotime Gast is flat (\u03c1=\u22120.01) and pSom declines (\u03c1=\u22120.26). "
  "Crest is anti-correlated with both (r=\u22120.66/\u22120.84), rising to a terminal readout (\u03c1=+0.40; "
  "neural-crest-high decile mean pt=0.70)."),
 ("Gate 3 \u2014 hub mutual exclusivity","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub, so there is no branch pair to test for mutual "
  "exclusivity."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Neuroblastoma (Kildisiute et al., 2021), 10x + CEL-seq2 \u2014 21 patients / 19,723 cells (master scope). "
 "Multi-platform with platform-exclusive patients, so the 10x (UMIcounts) leaf is resolved; malignant only: "
 "1,766 load, 1,720 across 2 samples (\u2265101) enter preprocessing; Embryonic compartment (1,504).")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. The neuroblastoma malignant "
 "manifold is a single monotone Gast/pSom \u2192 terminal-Crest gradient (non-branching), matching the "
 "developmental axis; it lacks Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to test. Unlike Lee, "
 "the axis is confined to the non-cycling lobe (Gast/pSom anti-correlate under proliferation), so the trajectory "
 "is scoped to it (K\u00fcrten lobe-identity precedent). EMT-TFs ZEB2 (early/root) \u2192 ZEB1 (late/terminus); "
 "FOXC/PRRX/SNAI near the detection floor; end-separation weak (\u0394pt=0.25).")
params=[
 ("Min cells/sample","\u2265101 (keeps 2/5; gap 425\u219224)"),
 ("Scope","10x leaf + Embryonic lobe"),
 ("Root node","tip 2 = Gast/pSom-high, Crest-low"),
 ("Integration","Harmony \u03b8=10; PCA50; spread=1.3"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Compartments","Embryonic 1,504 / Cycling 216"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Kildisiute 2021 NB \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
