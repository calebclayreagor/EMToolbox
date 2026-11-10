import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Gulati2020_Breast"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Gulati2020_Breast"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Four samples (\u2265100 malignant cells) intermix per-neighbourhood on one continuous manifold \u2014 iLISI rises "
  "2.77\u21923.56 of 4 after Harmony (\u03b8=5), one connected component, no islands removed. Read on the regenerated "
  "embedding, not a scalar alone."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "A single (Gast/pSom)\u2192Crest developmental axis. Gast/pSom do NOT diverge into cross-repressing arms (raw "
  "r=\u22120.05), while both oppose Crest (Gast\u2013Crest r=\u22120.50, pSom\u2013Crest r=\u22120.60). Crest is the inverse "
  "terminal readout (rises along pseudotime \u03c1=+0.93; NC-high decile at pt 1.00; joint pSom&Crest enrichment "
  "0.31<1). Non-branching case \u2192 GO."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "No bifurcation (curve: 2 tips / 0 forks), so there is no Mixed hub to test for Gast\u2194pSom anti-correlation. "
  "Branching-only \u2192 NA; 04_correlation / 05_modules not produced."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (Gulati et al., 2020), SmartSeq2 \u2014 861 malignant cells (8 samples) \u2192 587 analysed "
 "(4 samples \u2265100); single low-cycling Body (no proliferative compartment scoped out).")
verdict=("Pattern reproduces (non-branching, Linear-pSom/Crest): a single Gastrulation/Somitogenesis \u2192 "
 "Neural-Crest developmental axis with Crest as the inverse terminal readout; no Gast\u2194pSom bifurcation. "
 "Gate 1 GO / Gate 2 GO / Gate 3 NA. EMT-TFs ZEB2 (root-end) \u2192 SNAI2 (terminus).")
params=[
 ("Malignant / threshold","861 \u2192 floor \u2265100 (counts smooth, no cliff) \u2192 4 samples / 587 cells; 0 islands"),
 ("Expression / integration","SmartSeq2 TPM (log1p); overdisp=98; n_pcs=20; Harmony(sample) \u03b8=5; k=30; spread=1.3"),
 ("Trajectory / geometry","scFates curve (ElPiGraph) N=20 \u03bb=0.3 \u03bc=100; 2 tips / 0 forks; SA 2.89"),
 ("Root","curve tip 0 (Gast/pSom-high, Crest-low origin); Crest terminal; pt vs prolif \u03c1=\u22120.01"),
 ("Subtype / annotation","single low-cycling Body (no proliferative compartment scoped out); cell_type = Malignant"),
 ("EMT-TFs","ZEB2 (root-end) / SNAI2 (terminus) from 10-TF panel; detection-gated; VIM excluded"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Gulati 2020 Breast \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
