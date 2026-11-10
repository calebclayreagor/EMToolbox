import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Sarcoma/Jerby-Arnon2021_Sarcoma"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Sarcoma/Jerby-Arnon2021_Sarcoma"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "3 patients (SyS12pt/13/14) intermix on one continuous manifold; the kNN graph is a single component across "
  "the \u03b8 sweep (same-sample frac 1.00\u21920.72 at \u03b8=5). Cross-platform concat fails (10x/SmartSeq2 stay "
  "platform-segregated, ~0.87 at every \u03b8), so the run is scoped to the 10x leaf."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Gast & pSom co-vary (smoothed r=+0.76) while Crest opposes both (\u22120.75 / \u22120.97); the Crest-high decile "
  "sits at the trajectory terminus (mean pt 1.00). pSom-dominant \u2192 Linear-pSom/Crest."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Single monotone curve (0 forks), so the branching-only cross-repression test does not apply."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Synovial sarcoma (Jerby-Arnon et al., 2021); 10x scRNA-seq (UMI counts); 8,322 malignant cells, "
 "3 patients, after island removal. The SmartSeq2 leaf (4,371 cells, 11 patients) reproduces the same axis "
 "direction as an independent check.")
verdict=("Pattern reproduces (non-branching). A single gastrulation/somitogenesis-high origin flows to a "
 "neural-crest terminus; the EMT axis runs PRRX1 (root) \u2192 PRRX2 (terminus). Gate 1 GO / Gate 2 GO / Gate 3 "
 "NA \u2014 the Linear-pSom/Crest outcome shared by most CCCA datasets.")
params=[
 ("Min cells/sample","none (3 balanced samples; ratio 1.59)"),
 ("Scope","10x leaf (platform un-integratable)"),
 ("Root node","tip 2 = Gast/pSom-high, Crest-low"),
 ("Integration","Harmony \u03b8=5 (\u03b8=10 over-integrates)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100 (SA 2.58)"),
 ("EMT-TFs","PRRX1 (root) \u2192 PRRX2 (terminus)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Jerby-Arnon 2021 Synovial Sarcoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
