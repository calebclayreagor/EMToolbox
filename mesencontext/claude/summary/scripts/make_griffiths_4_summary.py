import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Griffiths2021_Breast-4"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Griffiths2021_Breast-4"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Two platform leaves (10x 110,568 + iCell8 804 malignant) share zero samples/patients and never mix under "
  "Harmony (platform iLISI ~1.0 across the sweep) \u2192 trajectory scoped to the 10x leaf. On the 10x leaf, 71 ER+ "
  "tumours intermix on one continuous manifold (sample iLISI 1.21\u219212.63 of 71; independent Harmony-PCA kNN = 1 "
  "component; 110,050 cells retained). Cycling is orthogonal to the embryonic axis \u2192 whole manifold kept. GO."),
 ("Gate 2 \u2014 module geography","\u2014",GREY,
  "Not evaluated \u2014 this attempt stopped after Gate 1 (only 01_preprocessing produced; no trajectory / signature "
  "steps committed, no processed.h5ad)."),
 ("Gate 3 \u2014 hub cross-repression","\u2014",GREY,
  "Not evaluated \u2014 downstream of Gate 2, which was not reached."),
]
panels=[("Manifold \u2014 samples (Gate 1)",os.path.join(F,"samples.pdf"))]
dataset=("Breast Cancer (ER+, FELINE neoadjuvant trial; Griffiths et al., 2021), 10x + iCell8 \u2014 10x leaf scoped: "
 "110,050 malignant cells across 71 samples (\u226550 cells).")
verdict=("INCOMPLETE ATTEMPT \u2014 reached Gate 1 GO (71 samples form one continuous 10x manifold; cycling orthogonal) "
 "but stopped before the trajectory / signature steps; only the samples deliverable was produced. Gate 1 GO / "
 "Gates 2 & 3 not evaluated. Superseded by later Griffiths runs.")
params=[
 ("Platform scope","10x leaf (iCell8 804 cells never co-embed; platform iLISI ~1.0)"),
 ("Sample threshold","\u226550 cells/sample (smooth dist, no clean cliff); retains >99.8%"),
 ("Integration","Harmony on sample (iLISI-sweep); n_pcs=30 (scree)"),
 ("Island removal","radius graph 6\u00d7 median-NN, largest component \u2192 110,050 cells"),
 ("Gate 1","GO \u2014 sample iLISI 1.21\u219212.63 of 71; 1 connected component; cycling orthogonal"),
 ("Status","INCOMPLETE \u2014 stopped after Gate 1 (preprocessing only)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Griffiths 2021 Breast Cancer \u2014 analysis summary",gates,panels,dataset,verdict,params,
              run_label="run 5 of 6")
print("built")
