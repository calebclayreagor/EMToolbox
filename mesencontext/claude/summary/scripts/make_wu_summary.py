import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Breast/Wu2021_Breast"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Breast/Wu2021_Breast"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "20/20 samples (\u2265100 cells) intermix on one continuous manifold with no per-patient islands "
  "(radius-graph: 0 detached; iLISI 1.0\u21924.96); both lobes (Low-cycling 11,803 / Cycling 12,686) carry "
  "near-identical developmental means \u2014 no lobe scoping."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching signature (spec \u00a71): embryonic programs present with Crest an inverse/terminal gradient \u2014 "
  "pSom\u2194Crest r=\u22120.71, Crest terminal (crest-high decile pt=0.94, rho=+0.55); Gast/pSom body ordered along "
  "pseudotime (pt 0.34/0.46), centroids collinear (area/perim\u00b2=0.010), cell-cycle-independent (pt\u2194cyc "
  "rho=+0.00). FLAG: Gast/pSom cross-repress (r=\u22120.47, obs/exp=0.36) \u2014 spec-permitted, organized at the body "
  "end opposite Crest."),
 ("Gate 3 — hub mutual exclusivity","NA",GREY,
  "No bifurcation: Gast/pSom repel (obs/exp=0.36) with 0 forks, so the program collapses onto a single axis "
  "rather than two arms \u2014 there is no branch pair to test for mutual exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast Carcinoma (Wu et al., 2021), 10x \u2014 20 patients / 100,064 cells (master scope); malignant only: "
 "24,489 cells across all 20 samples (\u2265100 min-cell floor) enter preprocessing; the whole malignant manifold "
 "(no lobe scoping) enters the trajectory.")
verdict=("Non-branching developmental pattern reproduces \u2014 Gate 1 GO, Gate 2 GO (non-branching), Gate 3 NA. Per "
 "spec \u00a71\u2013\u00a72, the non-branching case (embryonic programs present, Crest an inverse/terminal gradient, no "
 "bifurcation) passes Gate 2. Wu's breast malignant manifold shows exactly that: a Gast/pSom body opposite a "
 "terminal Neural-Crest gradient (crest-high decile pt=0.94, rho=+0.55; dominant inverse gradient pSom\u2194Crest "
 "r=\u22120.71), the programs organized along one axis rather than resolved into two arms. Module-high territories are "
 "collinear (area/perim\u00b2=0.010) and ordered Gast(pt 0.34)\u2192pSom(pt 0.46) body\u2192Crest terminus, "
 "cell-cycle-independent \u2014 developmental signal, not proliferation. Atypical feature, flagged: Gast and pSom "
 "cross-repress (r=\u22120.47, obs/exp=0.36) rather than overlap; the spec explicitly permits some cross-repression "
 "in the non-branching case, and here the repulsion is organized \u2014 at the body end opposite the terminal Crest \u2014 "
 "not the disorganized spread of a NO-GO. EMT-TFs SNAI1 (root) \u2194 SNAI2 (terminus) are near the detection floor "
 "(5.2%/4.1%; \u0394pt=0.09); the axis is carried by the module scores, not a single canonical EMT-TF.")
params=[
 ("Min cells/sample","\u2265100 floor (gap rule ill-defined)"),
 ("Integration","Harmony \u03b8=10; PCA 50\u219220; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Root node","tip = Gast/pSom-high, Crest-low"),
 ("Compartments","Low-cycling 11,803 / Cycling 12,686"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Wu 2021 Breast \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
