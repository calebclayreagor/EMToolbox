import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Lung/Kim2020_Lung"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Lung/Kim2020_Lung"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "13/14 samples (\u226542 cells) intermix on one continuous manifold; radius-graph finds 0 detached islands. "
  "Harmony \u03b8=5 (mixing plateaus by \u03b8=5); both compartments span multiple patients."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Gast/pSom near-orthogonal (r=\u22120.11), pSom broadly dominant over the body; Crest anti-correlated "
  "(r=\u22120.55 / \u22120.41), rising to a terminal readout (\u03c1=+0.48; crest-high decile mean pt=0.81). Gast "
  "declines along pseudotime (\u03c1=\u22120.55) \u2014 one monotone Gast/pSom \u2192 neural-crest axis, no second arm."),
 ("Gate 3 \u2014 hub mutual exclusivity","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub, so there is no branch pair to test."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Lung Adenocarcinoma (Kim et al., 2020), 10x \u2014 14 patients / 32,493 cells (master scope); malignant "
 "only: 10,538 load, 10,512 across 13 samples (\u226542) enter preprocessing. The whole malignant manifold (no lobe "
 "scoping) enters the trajectory: Embryonic 9,315 (6% cycling) + Cycling 1,197 (61%).")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Kim\u2019s LUAD malignant manifold "
 "is a single monotone Gast/pSom \u2192 terminal-neural-crest gradient, matching the developmental axis; it lacks "
 "Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to test. The developmental axis spans both "
 "proliferation lobes (orthogonal to cell cycle; per-lobe module means near-identical, Crest-high decile split "
 "52/48), so the whole manifold is kept (Bischoff/Sun no-scoping precedent). Caveat: pseudotime co-varies with "
 "cycling (\u03c1=+0.41). EMT-TFs FOXC1 (early/root) \u2192 PRRX2 (late/terminus); canonical SNAI1/ZEB1/TWIST1 near "
 "the detection floor, end-separation weak (\u0394pt=0.21).")
params=[
 ("Min cells/sample","\u226542 (13/14 kept; gap 70\u219226, ratio 2.7)"),
 ("Scope","whole manifold (no lobe scoping)"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Integration","Harmony \u03b8=5 on 50-PC; UMAP spread=1.3"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Compartments","Embryonic 9,315 / Cycling 1,197"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Kim 2020 LUAD \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
