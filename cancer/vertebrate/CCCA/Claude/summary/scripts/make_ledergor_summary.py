import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Hematologic/Ledergor2018_Hematologic-1"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Ledergor2018_Hematologic-1"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "16/18 samples (\u2265183 cells) intermix on one continuous manifold with no per-patient islands (radius-graph: 13 "
  "detached; iLISI median 1.00\u21925.13 of 16 \u2248 32% of ideal; kNN graph = 1 component at every \u03b8). Self-neighbour "
  "enrichment falls with integration \u2014 Harmony works, not an archipelago."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single dominant pSom\u2192Crest axis: pSom high at the Gast/pSom-high origin declines along pseudotime (\u03c1=\u22120.56); "
  "Crest anti-correlated (smoothed r=\u22120.96) and rises to a terminal readout (\u03c1=+0.57; crest-high decile mean pt=0.81). "
  "Gast weak/flat. Axis holds within patients (r=\u22120.64)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub, so there is no branch pair to test."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Multiple myeloma (Ledergor et al., 2018), MARS-seq \u2014 8,273 malignant plasma cells load (MM+SMM marrow); "
 "8,197 across 16 samples (\u2265183) enter preprocessing; 8,184 after island removal; the whole malignant manifold "
 "(no lobe scoping) enters the trajectory. Non-branching Linear-pSom/Crest.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. The myeloma malignant manifold is a "
 "single monotone somitogenesis \u2192 terminal-neural-crest gradient; it lacks Puram's hub-and-spoke bifurcation, so "
 "Gate 3 has no hub to test. The axis is a within-patient cell-state gradient (77\u201386% of module variance "
 "within-sample), not clonal/CNV structure, and is orthogonal to cell cycle (0.3% cycling). EMT-TFs: only ZEB1 "
 "(3.3%) / ZEB2 (1.4%) clear the detection floor \u2014 MARS-seq dropout silences the panel.")
params=[
 ("Min cells/sample","\u2265183 (16/18; gap 183\u219250)"),
 ("Integration","Harmony \u03b8=20; n_pcs=20; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root","tip: Gast/pSom-high, Crest-low"),
 ("Geometry","Linear (pSom/Crest); 0 stable forks"),
 ("Island removal","13 cells (radius-graph)"),
 ("EMT-TFs","ZEB1 (+ZEB2); rest <3% detection (MARS-seq dropout)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Ledergor 2018 multiple myeloma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
