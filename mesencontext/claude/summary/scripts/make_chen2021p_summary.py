import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Prostate/Chen2021_Prostate-1"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Prostate/Chen2021_Prostate-1"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Integration + continuity: iLISI rises from a sample-segregated baseline (median 1.0) and plateaus by "
  "\u03b8=10 (median 3.6, 12 samples intermixed); 0 detached islands \u2014 one continuous manifold."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Shared Gast/pSom developmental gradient with Crest as an inverse terminal gradient (pSom\u2194Crest "
  "r=\u22120.76; Crest-high decile at pseudotime 0.92). No two competing arms."),
 ("Gate 3 — hub cross-repression","NA",GREY,
  "No bifurcation: a PPT tree over-forks a continuous cloud \u2014 all tips share one profile (low Gast, "
  "moderate pSom, low Crest), no opposing Gast-high vs pSom-high arms. Curve fit: 2 tips, fold-free."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Prostate adenocarcinoma (Chen et al., 2021), 10x \u2014 14,266 malignant cells (12/13 samples above "
 "threshold).")
verdict=("Pattern reproduces as the non-branching case \u2014 one continuous gastrulation/somitogenesis \u2192 "
 "neural-crest developmental axis rooted at the Gast/pSom-high pole; no hub or bifurcation, so no "
 "cross-repression to test. Gate 1 GO, Gate 2 GO (non-branching), Gate 3 NA. EMT-TFs FOXC1 / TWIST1 are both "
 "root-enriched \u2014 no expressed EMT-TF marks the neural-crest terminus.")
params=[
 ("Min-cell threshold","55 (geom. mean, 125\u219225 gap; 12/13)"),
 ("Integration","Harmony \u03b8=10, n_pcs=20"),
 ("Overdispersed genes","1,583"),
 ("Geometry","Linear \u2014 non-branching curve"),
 ("Root","Gast/pSom-high tip (origin)"),
 ("Module means","Gast +0.004 / pSom +0.036 / Crest \u22120.069"),
 ("Hub identity / r","NA (non-branching)"),
 ("EMT-TFs shown","FOXC1 / TWIST1 (both root-enriched)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Chen 2021 Prostate Cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
