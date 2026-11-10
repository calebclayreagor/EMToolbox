import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, RED, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Head-and-Neck/Chen2020_Head-and-Neck-2"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Head-and-Neck/Chen2020_Head-and-Neck-2"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "8/14 samples (\u2265107 cells) intermix on one continuous manifold: iLISI 2.1 / 3.2 ceiling, metrics plateau at "
  "\u03b8\u22652 (over-integration null passes); P11-removal control confirms genuine cross-patient mixing; single kNN "
  "component."),
 ("Gate 2 \u2014 module geography","NO-GO",RED,
  "No Gast/pSom hub. Gast and pSom are orthogonal (r=\u22120.05) \u2014 neither co-varying (overlap case) nor "
  "cross-repressing (branching); both diffuse across the manifold. Structure is carcinoma-state (cycling, "
  "squamous/basal, hypoxia, IFN/MHC-II), not embryonic. Both oppose Crest (\u22120.54/\u22120.44); Crest is not a "
  "proliferation confound."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not tested \u2014 no bifurcation and no hub to run 04_correlation / 05_modules on (branching-only gate)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Nasopharyngeal carcinoma (Chen et al., 2020), 10x \u2014 14 patients / 3,763 malignant load; 3,674 across "
 "8 samples (\u2265107 cells) enter the manifold.")
verdict=("Pattern does not reproduce. Gate 1 GO but Gate 2 NO-GO: NPC malignant cells form a continuous "
 "carcinoma-state manifold with no embryonic module geography \u2014 Gast/pSom independent, no hub, no arms. "
 "EMT-TFs PRRX1 (62%) / VIM (53%) broad, no mesenchymal terminus; canonical SNAI1/ZEB1/TWIST1 near-absent "
 "(1\u20137%).")
params=[
 ("Min cells/sample","\u2265107 (keeps 8/14)"),
 ("Integration","Harmony on sample, \u03b8=2, 20 it"),
 ("Island removal","none (single kNN comp.)"),
 ("Trajectory","scFates PPT N=50 \u03bb=300 \u03c3=0.5"),
 ("Root node","35 = Progenitor-like"),
 ("n_pcs","19 (>0.5% var each; \u03b8-sweep 0\u201310)"),
 ("Scaling","none (log1p, reference-matched)"),
 ("Signatures","score_genes, union control pool"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Chen 2020 NPC \u2014 analysis summary",gates,panels,dataset,verdict,params,
              run_label="run 3 of 7")
print("built")
