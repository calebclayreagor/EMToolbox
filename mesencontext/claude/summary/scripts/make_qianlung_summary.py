import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Lung/Qian2020_Lung"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Lung/Qian2020_Lung"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "6/8 samples (\u2265100 cells) intermix on one continuous manifold with no per-patient islands (radius-graph: 0 "
  "detached; iLISI median 1.00\u21922.39 of 6); both lobes (Body 3,848 / Cycling 1,400) carry the trajectory."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single dominant pSom\u2192Crest axis: pSom high over the low-cycling body declines along pseudotime "
  "(\u03c1=\u22120.68); Crest anti-correlated (r=\u22120.89), rising to a terminal readout (\u03c1=+0.82; Crest-high decile "
  "mean pt=0.98). Gast weakly structured (early programme, spent); joint pSom&Crest-high depleted (enrichment 0.18) "
  "\u2014 an inverse gradient, not a co-expression hub."),
 ("Gate 3 — hub mutual exclusivity","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub, so there is no branch pair to test for mutual "
  "exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Non-Small-Cell Lung Cancer (Qian et al., 2020), 10x \u2014 8 patients / 27,262 cells (master scope); "
 "malignant only: 5,248 cells across 6 malignant-bearing samples (drop 2 sub-100 spillover samples) enter "
 "preprocessing; the whole malignant manifold (no lobe scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Qian's NSCLC malignant manifold is a "
 "single monotone somitogenesis \u2192 terminal-neural-crest gradient (low-cycling body \u2192 neural-crest-like "
 "terminus), matching the developmental axis; it lacks Puram's hub-and-spoke bifurcation, so Gate 3 has no hub to "
 "test. The Body/Cycling split is partly proliferative and the Crest terminus enriches the cycling side, but the "
 "developmental modules are cell-cycle-free (Gast 0/81, Crest 0/104 cell-cycle genes) and the pSom\u2194Crest "
 "anti-correlation survives within non-cycling cells alone (r=\u22120.89\u2192\u22120.90), so the axis is developmental, "
 "not proliferative \u2014 the whole manifold is kept (Lin/Steele no-scoping precedent), carrying "
 "pseudotime\u2194cycling co-variation (\u03c1=+0.45) as a caveat. EMT-TFs are root/body-loaded: SNAI1 (early) \u2192 "
 "ZEB1 (late) chosen by data over Puram's pair, but all expressed factors decline along pt and end-separation is "
 "weak (\u0394pt=0.08); the only terminus-rising factor (SNAI2, \u03c1=+0.18) sits just below the 3% detection floor.")
params=[
 ("Min cells/sample","\u2265100 floor (6/8; gap non-dominant)"),
 ("Integration","Harmony \u03b8=10; PCA50; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Root node","tip 2 = pSom-high, Crest-low"),
 ("Compartments","Body 3,848 / Cycling 1,400"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Qian 2020 NSCLC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
