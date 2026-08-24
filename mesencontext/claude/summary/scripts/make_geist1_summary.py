import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Ovarian/Geistlinger2020_Ovarian-1"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Ovarian/Geistlinger2020_Ovarian-1"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "5/5 samples (\u2265259 cells) intermix on one continuous manifold with no per-patient islands (radius-graph: 1 speck, "
  "25 cells removed; iLISI median 1.00\u21922.23 of 5); both compartments (Embryonic 2,857 / Cycling-Metabolic 3,049) "
  "carry the trajectory."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single Gast/pSom \u2192 Crest axis: Gast & pSom co-vary (r=+0.63) and decline along pseudotime (\u03c1=\u22120.79/\u22120.63); "
  "Crest anti-correlated (r=\u22120.79/\u22120.95), rising to a terminal readout (\u03c1=+0.79; Crest-high decile mean pt=0.98). "
  "Global strength pSom>Gast>Crest-neg (Linear-pSom/Crest)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "All four PPT-tree tips are pSom-leaning (no Gast arm) \u2014 the \u201cforks\u201d are density + cycling structure inside one "
  "co-varying programme, not a bifurcation. No Mixed hub, no branch pair to test."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("High-grade serous ovarian carcinoma (Geistlinger et al., 2020), 10x \u2014 5 patients / 41,031 cells (master "
 "scope); malignant only: 5,931 load, 5,906 across 5 samples (\u2265259) after a 25-cell speck; the whole malignant "
 "manifold (no lobe scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Geistlinger\u2019s HGSOC malignant manifold "
 "is a single monotone Gast/pSom \u2192 terminal-neural-crest gradient, matching the developmental axis; it lacks "
 "Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to test. The axis spans both density lobes (cycling is a "
 "weaker secondary gradient, \u03c1(cyc,pt)=\u22120.47), so the whole manifold is kept (Bischoff/Sun/Zhou no-scoping "
 "precedent). EMT-TFs are a root/mesenchymal readout, all declining from the Gast/pSom-high root: PRRX2 (root-end, "
 "steepest) \u2192 SNAI2 (terminus-end, least declining); canonical ZEB1/TWIST near the detection floor (6.2%/2.0%).")
params=[
 ("Min cells/sample","\u2265100 (keeps 5/5; top-of-distribution gap, no thin tail)"),
 ("Scope","whole manifold (no scoping)"),
 ("Integration","Harmony \u03b8=10; n_pcs=20; spread=1.3"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Compartments","Embryonic 2,857 / Cycling 3,049"),
 ("EMT-TFs","PRRX2 (root) \u2192 SNAI2 (terminus)"),
 ("Geometry","Linear-pSom/Crest (non-branching; fold-free 2.99)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Geistlinger 2020 HGSOC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
