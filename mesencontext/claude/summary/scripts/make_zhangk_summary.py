import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Kidney/Zhang2021_Kidney-3"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Kidney/Zhang2021_Kidney-3"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "1 connected component at all \u03b8; iLISI peak 3.12 @ \u03b8=10; the axis recurs within patients (not a between-patient "
  "integration artifact)."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching: no Gast/pSom co-expression hub (joint co-high 4.9% vs 11.6% expected); pSom\u2194Crest inverse terminal "
  "gradient r=\u22120.80, Gast/pSom cross-repression r=\u22120.53. Single organized axis, no divergent arms."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable \u2014 no bifurcation / hub to test for Gast\u2194pSom node anti-correlation."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Clear-cell + chromophobe renal cell carcinoma (Zhang et al., 2021), 10x \u2014 11,410 malignant cells \u2192 11,218 "
 "after per-sample threshold \u2192 11,136 after island removal, across 7 samples (6 ccRCC + 1 chromophobe); the whole "
 "malignant manifold enters the trajectory (non-branching linear geometry).")
verdict=("The embryonic pattern reproduces as the non-branching case. A single continuous manifold carries an organized "
 "posterior-somitogenesis (origin) \u2194 neural-crest (terminal) inverse axis (r=\u22120.80) with Gast/pSom cross-repression "
 "(r=\u22120.53), but no Gast/pSom co-expression hub and no divergent arms \u2014 so no bifurcation. Geometry LINEAR; Gate 3 "
 "NA. The axis is genuine intra-tumoral biology: it reproduces within every individual patient (mean pSom\u2194Crest "
 "r=\u22120.57), not a between-patient integration artifact. EMT programme is origin-loaded (all 6 expressed TFs decline "
 "from the origin).")
params=[
 ("Min-cell threshold","369 (geom-mean of dominant gap 192\u2192710, ratio 3.70); drops 1 sample"),
 ("Over-dispersed genes","1,363 (scFates find_overdispersed); n_pcs=20 (scree knee)"),
 ("Integration","Harmony on sample, \u03b8=10 (iLISI peak 3.12; \u03b8=20 re-segregates chromophobe)"),
 ("Island removal","radius graph 6\u00d7 median NN; keep largest comp (99.3%); 82 fringe cells"),
 ("Geometry","LINEAR \u2014 ElPiGraph curve (Nodes 12, \u03bb 2.0); 2 tips, 0 forks, fold-free (2.99)"),
 ("Root","Gast/pSom-high, Crest-low curve tip (developmental origin; Crest is late)"),
 ("Module means","Gast \u22120.034 / pSom +0.085 / Crest \u22120.060 (Crest terminal, no Gast arm)"),
 ("EMT-TFs","ZEB2 (23.9%, origin) / SNAI2 (3.3%, body); all origin-loaded, 0 terminus factor"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Zhang 2021 RCC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
