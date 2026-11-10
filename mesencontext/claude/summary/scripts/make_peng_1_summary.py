import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, RED, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Pancreas/Peng2019_Pancreas-1"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Pancreas/Peng2019_Pancreas-1"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "All 16 samples intermix on one continuous connected component (0 detached islands; UMAP aspect 1.17; iLISI "
  "median 1.0\u21925.3 of 16 at \u03b8=10) \u2014 judged on the embedding, not a scalar. Cell cycle (6.6% cycling) is not a "
  "module confound (|\u03c1|\u22640.24; the pSom\u2013Crest spatial anti-correlation is unchanged when cyclers are excluded), "
  "so the whole malignant manifold is carried forward."),
 ("Gate 2 \u2014 module geography","NO-GO",RED,
  "Embryonic module pattern absent. The three smoothed modules occupy a 2-D triangle (PCA variance 0.55/0.40; "
  "Gast/pSom/Crest top-decile peaks 110\u2013134\u00b0 apart) \u2014 no Gast/pSom co-expression hub. They do not order along "
  "pseudotime (pSom \u03c1=+0.11, Crest \u03c1=\u22120.10) and Crest is non-terminal (Crest-high decile at pseudotime 0.60; "
  "joint pSom&Crest enrichment 0.41). Neither the branching hub nor the non-branching pSom\u2192Crest axis reproduces."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Branching-only gate. The manifold is non-branching (curve: 2 tips, 0 forks) and Gate 2 did not pass. No hub \u2014 "
  "Gast and pSom are anti-correlated and sit at opposite triangle corners (spatial r=\u22120.41)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Pancreatic ductal adenocarcinoma (Peng et al., 2019), 10x \u2014 7,945 malignant cells, 16 samples.")
verdict=("Pattern does NOT reproduce. Gate 1 GO / Gate 2 NO-GO / Gate 3 NA \u2014 developmental programs are present as "
 "scores but geographically unresolved (a triangle, not an axis): a triangular, non-axial module geography, not "
 "the Linear-pSom/Crest developmental axis seen in the same-tissue Steele/Lin/Moncada PDAC GO runs. EMT-TFs ZEB1 "
 "(root end) / SNAI2 (terminus end).")
params=[
 ("Threshold","\u2265100-cell floor (gap-finding premise unmet) \u2192 all 16 samples kept"),
 ("Integration","Harmony \u03b8=10; iLISI median 1.0\u21925.3 of 16"),
 ("Cell cycle","6.6% cycling; not a module confound (|\u03c1|\u22640.24); whole manifold carried"),
 ("Module geometry","2-D triangle (PCA var 0.55/0.40; peaks 110\u2013134\u00b0 apart); no hub"),
 ("Trajectory","scFates curve (2 tips, 0 forks); root = Gast/pSom-high tip"),
 ("EMT-TFs","ZEB1 (root) / SNAI2 (terminus); Snail/Zeb/Twist + FOXC/PRRX, 3% floor"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Peng 2019 PDAC \u2014 analysis summary",gates,panels,dataset,verdict,params,
              run_label="run 2 of 3")
print("built")
