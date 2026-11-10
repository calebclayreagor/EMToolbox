import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Pancreas/Raghavan2021_Pancreas"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Pancreas/Raghavan2021_Pancreas"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "20/20 PDAC samples (\u2265120 cells) intermix on one continuous manifold with no per-patient islands "
  "(radius-graph: 50 cells / 1 speck removed; iLISI median 1.00\u21927.22 of 20); both lobes (Ductal-body 6,494 / "
  "Cycling 674) carry the trajectory. One PANET sample (662 cells, a distinct neuroendocrine malignancy) was "
  "excluded to match the declared PDAC scope."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Single dominant pSom\u2192Crest axis: pSom high over the classical-ductal body declines along pseudotime "
  "(\u03c1=\u22120.74); Crest anti-correlated (r=\u22120.68), depleted at the root and rising to a distal plateau "
  "(\u03c1=+0.61; crest-sm peaks mid-to-distal, decile pt=0.59). Gast co-varies with pSom (joint-high enrichment "
  "1.15); joint pSom&Crest-high depleted (0.23) \u2014 an inverse gradient, not a hub."),
 ("Gate 3 \u2014 hub mutual exclusivity","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub (curve: 2 tips, 0 forks, self-approach 2.57), "
  "so there is no branch pair to test for mutual exclusivity."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("PDAC (Raghavan et al., 2021), Seq-Well \u2014 24 patients / 24,412 cells (master scope); malignant only: "
 "7,904 cells, of which 7,242 are PDAC (662 PANET neuroendocrine cells dropped). After the \u2265120-cell floor, "
 "7,168 cells across 20 samples enter preprocessing; the whole malignant manifold (no lobe scoping) enters the "
 "trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Raghavan\u2019s metastatic PDAC "
 "malignant manifold is a single monotone somitogenesis \u2192 distal-neural-crest gradient (classical-ductal body "
 "\u2192 neural-crest-like distal pole); it lacks Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to "
 "test. The axis spans both lobes and is orthogonal to cell cycle (module\u2013cyc |\u03c1|\u22640.20; pt\u2013cyc "
 "\u03c1=+0.11), so the whole manifold is kept. Raw module means are pSom-dominant and geography is a coherent "
 "inverse pSom\u2192Crest gradient (Crest depleted at root, rising to a distal plateau) \u2014 not the "
 "mutually-exclusive territories of the failed Peng 2019 PDAC run. EMT-TFs FOXC1 (early/root) \u2192 ZEB2 (late) "
 "on the widened FOXC/PRRX panel.")
params=[
 ("Min cells/sample","\u226573 (geom-mean 120\u219245)"),
 ("Scope","PDAC only; whole manifold"),
 ("Root node","tip 0 = pSom-high, Crest-low"),
 ("Integration","Harmony \u03b8=10; PCA50; spread=1.3"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Compartments","Ductal-body 6,494 / Cycling 674"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Raghavan 2021 PDAC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
