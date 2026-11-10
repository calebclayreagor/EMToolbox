import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Ledergor2018_Hematologic"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Ledergor2018_Hematologic"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=15) fuses the patient-private myeloma clones: same-sample neighbour fraction 0.87\u21920.26, iLISI "
  "1.0\u21925.1 / 16, one connected kNN component. Judged on the regenerated embedding across a \u03b8-sweep \u2014 "
  "samples intermix on one continuous, uniformly low-cycling body (no proliferative lobe to scope)."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Signatures collapse onto a single (Gast/pSom)\u2192Crest axis: smoothed pSom\u2194Crest r=\u22120.97, Gast\u2194pSom "
  "r\u2248\u22120.10 (no cross-repression \u2192 no two competing arms). Crest is an inverse terminal gradient "
  "(crest-high decile pseudotime 0.83; joint pSom&Crest enrichment 0.16). Principal curve is fold-free "
  "(2 tips / 0 forks)."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Non-branching topology \u2014 no bifurcation and no Gast/pSom hub, so the branching-only cross-repression test "
  "does not apply. Correlation & modules notebooks are correctly not produced."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Multiple myeloma (Ledergor et al., 2018), MARS-seq \u2014 8,182 malignant plasma cells over 16 samples. "
 "Uniformly low-cycling body (no proliferative lobe to scope).")
verdict=("Pattern reproduces as the NON-BRANCHING case \u2014 a single gastrulation/somitogenesis\u2192neural-crest "
 "developmental axis; no hub, no bifurcation. Gate 1 GO / Gate 2 GO / Gate 3 NA. EMT-TFs ZEB1 (root) \u2192 ZEB2 "
 "(terminus) \u2014 the only detectably-expressed factors.")
params=[
 ("Min-cell threshold","\u226595 (geom-mean of 183\u219250 cliff; 16/18 samples; drops MM04, MM05)"),
 ("Integration","Harmony on sample, \u03b8=15 (patient-private MM clones), n_pcs=40, k=30, spread=1.3"),
 ("Islands removed","15 cells / 2 detached specks (UMAP radius graph, largest component)"),
 ("Geometry","Non-branching \u2192 scFates curve (ElPiGraph) N=20 \u03bb=0.3 \u03bc=100; 2 tips / 0 forks, fold-free"),
 ("Root node","curve tip 0 \u2014 Gast/pSom-high, Crest-low (pSom\u2192Crest along pseudotime)"),
 ("Module means (raw)","Gast \u22120.029 \u00b7 pSom +0.016 \u00b7 Crest +0.004 \u2192 Linear-pSom/Crest"),
 ("EMT-TFs shown","ZEB1 (root) \u2192 ZEB2 (terminus); detectable 3.3% / 1.5%"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Ledergor 2018 Multiple Myeloma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
