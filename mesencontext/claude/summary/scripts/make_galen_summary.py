import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Galen2019_Hematologic"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Galen2019_Hematologic"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "19/28 samples (\u226531 cells) intermix on one continuous manifold with no per-patient islands (iLISI 5.66 of 9.95 "
  "ceiling; radius-graph: 1 detached); both lobes (Cycling 9,872 / Low-cycling 6,227) carry the trajectory."),
 ("Gate 2 — module geography","GO (non-branching, inversion FLAG)",GREEN,
  "Gast/pSom cross-repress (r=\u22120.67); along pseudotime pSom declines / Gast rises (\u03c1=\u22120.87/+0.44); Crest "
  "anti-correlated with pSom (r=\u22120.90) but positive with Gast (r=+0.39) \u2014 the inversion \u2014 rising to a terminal "
  "readout (\u03c1=+0.83; crest-high decile mean pt=0.99)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Gast/pSom co-expression hub, so there is no branch pair to test for "
  "mutual exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Acute Myeloid Leukemia (van Galen et al., 2019), SeqWell \u2014 37 samples / 33,392 cells (master scope); "
 "malignant only: 16,169 load, 16,099 across 19 samples (\u226531) enter preprocessing; the whole malignant manifold "
 "(no lobe scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Galen\u2019s AML malignant manifold is a "
 "single monotone Gast/pSom (cross-repressing) \u2192 terminal-Crest gradient rooted at the primitive, pSom/Gast-high, "
 "low-cycling pole; it lacks Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to test. The developmental "
 "axis spans both lobes (pSom pole low-cycling, Crest terminus cycling), so the whole manifold is kept "
 "(Bischoff/Sun/Lee no-scoping precedent). FLAG: Crest enriches the Gast end (inversion). EMT-TFs ZEB2 (early/root) "
 "\u2192 ZEB1 (late/terminus); FOXC1/SNAI1/TWIST below 3% floor.")
params=[
 ("Min cells/sample","31 (keeps 19/28; cliff 61\u219216)"),
 ("Integration","Harmony \u03b8=10; PCA50; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","tip 2 = Gast/pSom-high, Crest-low"),
 ("Compartments","Cycling 9,872 / Low-cycling 6,227"),
 ("Geometry","Linear (non-branching); inversion FLAG"),
 ("EMT-TFs","ZEB2 (early/root) \u00b7 ZEB1 (late/terminus)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Galen 2019 AML \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
