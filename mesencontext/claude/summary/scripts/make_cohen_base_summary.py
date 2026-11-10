import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Cohen2021_Hematologic"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Cohen2021_Hematologic"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "54 samples intermix per-neighbourhood (iLISI 1.0\u219214.1 of 54) on one continuous connected component; single "
  "Leiden lobe, aspect 1.09, only 2.8% cycling \u2014 no islands, no batch archipelago, no cycling compartment."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Non-branching: a single Gast/pSom-origin \u2192 terminal-Crest axis. Crest inversely opposes Gast (r=\u22120.69) "
  "and pSom (r=\u22120.61); pSom&Crest joint-high enrichment 0.22 (<1 = inverse gradient, not a co-expression hub)."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "No bifurcation: Gast\u2194pSom near-orthogonal (r=+0.07), no competing arms \u2014 branching-only gate not "
  "applicable."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Multiple myeloma bone-marrow plasma cells (Cohen et al., 2021), MARS-seq \u2014 33,076 malignant cells "
 "across 54 samples (\u2265100 cells). Whole malignant manifold; single differentiation continuum.")
verdict=("The embryonic pattern reproduces as a NON-BRANCHING axis: Gast/pSom-high origin \u2192 terminal "
 "neural-crest, no resolved bifurcation. Linear-pSom/Crest geometry (Gast \u03bc=\u22120.022, pSom \u03bc=+0.014, "
 "Crest \u03bc=+0.001). EMT-TF ZEB1 is the only factor above the detection floor.")
params=[
 ("Sample threshold","\u2265100 cells (floor; smooth decline, no cliff) \u2192 54/73 samples, 33,147 cells"),
 ("Overdispersed genes","482 (scFates); island removal 71 cells / 2 specks \u2192 33,076"),
 ("Integration","Harmony \u03b8=10 on sample (swept 2/5/10; same-sample nbr frac 0.91\u21920.11)"),
 ("Embedding","n_pcs=20 (scree plateau), n_neighbors=30, UMAP spread=1.3"),
 ("Trajectory","scFates curve (ElPiGraph, N=20, \u03bb=0.3, \u03bc=100); non-branching, fold-free (2.5)"),
 ("Root","tip highest Gast+pSom, lowest Crest; Gast \u03c1=\u22120.55, Crest \u03c1=+0.57"),
 ("EMT-TF readout","ZEB1 (3.2%) \u2014 sole factor above floor; others <0.3%"),
 ("Annotation","Malignant plasma cells (author cell_type); single continuum"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Cohen 2021 Multiple Myeloma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
