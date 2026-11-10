import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Skin/Tirosh2016_Skin"; F="/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Tirosh2016_Skin"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "6 samples (\u2265182 cells) intermix on one continuous manifold with no per-patient islands (radius-graph: "
  "0 detached); mean cross-sample kNN fraction 0.47. All cells MITF-high \u2014 a single melanocytic compartment "
  "carries the trajectory (no lobe split)."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.93) and decline along pseudotime (\u03c1=\u22120.73/\u22120.71); Crest anti-correlated "
  "(r=\u22120.81/\u22120.83), rising to a terminal readout (\u03c1=+0.41; crest-high decile mean pt=0.92)."),
 ("Gate 3 \u2014 hub mutual exclusivity","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub, so there is no branch pair to test for "
  "mutual exclusivity."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Melanoma (Tirosh et al., 2016), SmartSeq2 \u2014 19 patients / 4,645 cells (master scope); malignant "
 "only: 1,257 load across 15 samples, 1,061 across 6 samples (\u2265182 cells) enter preprocessing. All cells form "
 "one continuous MITF-high melanocytic compartment that carries the trajectory (no lobe split).")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Tirosh\u2019s melanoma manifold "
 "is a single monotone Gast/pSom \u2192 terminal-Crest gradient (non-branching), matching the developmental axis; "
 "it lacks Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to test. Data-derived EMT-TFs are TWIST1 "
 "(early/root, \u03c1=\u22120.05) \u2192 SNAI2 (late/terminus, \u03c1=+0.44); Puram\u2019s canonical SNAI1/ZEB1 are "
 "expressed (10%/11%) but not the most end-specific factors here.")
params=[
 ("Min cells/sample","\u2265182 (keeps 6/15; gap 98\u219254)"),
 ("Compartment","single melanocytic (all MITF-high)"),
 ("Root node","tip = Gast/pSom-high, Crest-low"),
 ("Integration","Harmony(sample) \u03b8=2; PCA 50PC; UMAP spread=1.0"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Subtypes","Cycling/Hypoxic, Melanocytic-quiescent, Pigmented-Stress"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Tirosh 2016 Melanoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
