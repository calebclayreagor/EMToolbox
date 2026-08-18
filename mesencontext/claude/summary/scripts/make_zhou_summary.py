import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Sarcoma/Zhou2020_Sarcoma"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Sarcoma/Zhou2020_Sarcoma"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "9/11 samples (\u2265599 cells) intermix on one continuous manifold with no per-patient islands "
  "(radius-graph: 0 detached; iLISI median 1.00\u21924.51 of 9); both lobes (Embryonic 22,156 / Cycling 10,650) "
  "carry the trajectory."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single dominant pSom\u2192Crest axis: pSom high over the osteoblastic body declines along pseudotime "
  "(\u03c1=\u22120.66); Crest anti-correlated (r=\u22120.88), rising to a terminal readout (\u03c1=+0.55; crest-high "
  "decile mean pt=0.93). Gast weakly structured (early programme, spent)."),
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
dataset=("Osteosarcoma (Zhou et al., 2020), 10x \u2014 11 patients / 64,557 cells (master scope); malignant only: "
 "33,459 load, 32,806 across 9 samples (\u2265599) enter preprocessing; the whole malignant manifold (no lobe "
 "scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Zhou's osteosarcoma malignant "
 "manifold is a single monotone somitogenesis \u2192 terminal-neural-crest gradient (osteoblastic body \u2192 "
 "chondroblastic tip), matching the developmental axis; it lacks Puram's hub-and-spoke bifurcation, so Gate 3 has "
 "no hub to test. The axis spans both proliferation lobes (orthogonal to cell cycle; module\u2013g2m |\u03c1|\u22640.14), "
 "so the whole manifold is kept (Bischoff/Sun no-scoping precedent). Caveat: pseudotime co-varies negatively with "
 "cycling (\u03c1\u2248\u22120.55) as the somitogenesis-high root lobe is the more proliferative one. EMT-TFs PRRX2 "
 "(early/root) \u2192 FOXC1 (late/terminus); canonical SNAI1/ZEB1 near the detection floor; EMT-TF end-separation "
 "weak (\u0394pt=0.21).")
params=[
 ("Min cells/sample","\u2265599 (9/11; gap 1007\u2192357)"),
 ("Integration","Harmony \u03b8=10; PCA50; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Root node","tip 2 = pSom-high, Crest-low"),
 ("Compartments","Embryonic 22,156 / Cycling 10,650"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Zhou 2020 Osteosarcoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
