import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Gao2021_Breast"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Gao2021_Breast"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "5/6 breast samples (\u2265347 cells) intermix on one continuous manifold with no per-patient islands "
  "(radius-graph: 89 detached removed; kNN = 1 component); both compartments (Embryonic 5,242 / Cycling 1,080) "
  "carry the trajectory."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Organised Gast\u2194pSom cross-repression (r=\u22120.49) laid out along one axis; Crest anti-correlated with pSom "
  "(r=\u22120.58), rising to a terminal readout (\u03c1=+0.23; crest-high decile mean pt=0.75). Along pseudotime Gast "
  "declines (\u03c1=\u22120.31); no Gast/pSom co-expression hub (395 vs 731 exp.)."),
 ("Gate 3 \u2014 hub mutual exclusivity","NA",GREY,
  "Single cross-repression axis \u2014 no bifurcation and no Gast/pSom co-expression hub, so there is no branch "
  "pair to test for mutual exclusivity."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast Cancer (Gao et al., 2021), 10x \u2014 11 patients / 29,992 cells (master scope, incl. thyroid). "
 "Breast-only malignant: 6,606 pooled across both matrix leaves (5 anaplastic-thyroid samples excluded), 6,411 "
 "across 5 samples (\u2265347) after threshold, 6,322 after island removal.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Gao\u2019s breast malignant "
 "manifold is a single axis of organised Gast\u2194pSom cross-repression (r=\u22120.49) with a terminal neural-crest "
 "gradient (non-branching, Linear-pSom/Crest); it lacks Puram\u2019s hub-and-spoke bifurcation (no co-expression "
 "hub), so Gate 3 has no branch pair to test. The proliferation split is orthogonal to the developmental axis "
 "(root tercile 4.5% cycling vs terminus 40%), so the whole manifold is kept (Bischoff/Sun/Lee no-scoping "
 "precedent). EMT-TFs FOXC1 (early/root) \u2192 SNAI2 (late/terminus); ZEB1/TWIST2 near the detection floor "
 "(1.1%/0.3%); end-separation weak (\u0394pt=0.25).")
params=[
 ("Min cells/sample","\u2265347 (gap 618\u2192195)"),
 ("Scope","whole manifold; breast-only"),
 ("Root node","tip 2 = Gast/pSom-high"),
 ("Integration","Harmony \u03b8=10; PCA50; spread 1.3"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Compartments","Embryonic 5,242 / Cycling 1,080"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Gao 2021 Breast \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
