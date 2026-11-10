import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Prostate/Chen2021_Prostate"; F="/home/caleb/EMToolbox/figures/mesencontext/claude/Prostate/Chen2021_Prostate"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "12/13 samples (\u226555 cells) intermix on one continuous manifold with no per-patient islands (radius-graph: "
  "0 detached); the whole low-cycling malignant manifold (14,266 cells, cycling 2.1%) carries the trajectory \u2014 "
  "no separable compartment."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Somitogenesis & Gastrulation decline along pseudotime (\u03c1=\u22120.32 / \u22120.18); Neural-crest anti-correlated "
  "with pSom (r=\u22120.76), rising to a terminal readout (\u03c1=+0.41; crest-high decile mean pt=0.92). Gast/pSom do "
  "not co-vary (r=\u22120.11) \u2014 an inverse gradient, no hub."),
 ("Gate 3 \u2014 hub mutual exclusivity","NA",GREY,
  "Single monotone pSom\u2192Crest axis \u2014 no bifurcation and no Gast/pSom co-expressing hub, so there is no "
  "branch pair to test for mutual exclusivity."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Prostate cancer (Chen et al., 2021), 10x \u2014 13 samples / 36,424 cells (master scope); malignant only: "
 "14,291 load, 14,266 across 12 samples (\u226555) enter preprocessing; all 14,266 (one continuous manifold, "
 "0 detached islands) enter the trajectory.")
verdict=("Non-branching pattern \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Chen\u2019s prostate malignant manifold is a "
 "single monotone Somitogenesis \u2192 terminal Neural-crest gradient (non-branching), matching the developmental "
 "axis; it lacks Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to test. Expressed EMT-TFs (TWIST1, "
 "FOXC1) are root-enriched and decline toward the terminus \u2014 no canonical EMT-TF is induced at the neural-crest "
 "end; SNAI1/ZEB1 near the detection floor (3.0% / 0.4%).")
params=[
 ("Min cells/sample","\u2265 55 (keeps 12/13; gap 125\u219225)"),
 ("Compartment","whole manifold (2.1% cycling, no split)"),
 ("Root node","tip = Gast/pSom-high, Crest-low"),
 ("Integration","Harmony \u03b8=10; PCA 50PC; spread=1.3"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Orientation","x-flip, no swap (raw-x \u2225 pt, r=+0.94)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Chen 2021 Prostate \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
