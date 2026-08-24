import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Lung/Kim2020_Lung-2"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Lung/Kim2020_Lung-2"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "One connected manifold (0 detached islands). Dominant sample P1028 (40%) spread throughout, not an "
  "archipelago; median 5 of 11 samples per 30-cell neighbourhood. iLISI 1.00\u21922.61 across the \u03b8 sweep "
  "(\u03b8=10 on the mixing plateau). Read on the embedding + iLISI, not a scalar."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching: single developmental axis. Gast/pSom overlap (spatial r=\u22120.11); both oppose Crest "
  "(Gast-Crest r=\u22120.53, pSom-Crest r=\u22120.38). Crest is a terminal inverse gradient (Crest-high decile "
  "pseudotime 0.75; joint-high enrichment 0.31/0.44 < 1). Crest terminal to both modules \u2014 no Crest-arm "
  "inversion flag. PPT tree over-tiles the blob (no clean Y)."),
 ("Gate 3 — hub cross-repression","NA",GREY,
  "Not applicable \u2014 non-branching manifold has no Gast/pSom bifurcation hub to test."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Lung Adenocarcinoma (Kim et al., 2020), 10x \u2014 11 patients; 10,538 malignant cells (10,368 after "
 "thresholding) enter the analysis; the whole malignant manifold enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO (non-branching), Gate 3 NA (LINEAR geometry). "
 "The embryonic-development programme reproduces as a single continuous gastrulation/somitogenesis \u2192 neural-crest "
 "axis: Gast/pSom co-vary at the origin, Crest rises to the terminus (inverse gradient), no competing-arm "
 "bifurcation \u2014 so Gate 3 has no hub to test. EMT-TFs FOXC1 (root) \u2192 PRRX2 (terminus).")
params=[
 ("Min-cell threshold","\u2265100 cells/sample \u2192 11/14 kept (no dominant cliff, top/2nd 1.2 \u2192 floor)"),
 ("Integration","Harmony on sample, \u03b8=10"),
 ("Geometry","n_pcs=30; no scale before PCA"),
 ("Trajectory","ElPiGraph curve N=20 (fold-free 2.89)"),
 ("Root","Gast/pSom-high tip 0 (Crest-low origin)"),
 ("Module means","Gast \u22120.040 \u00b7 pSom +0.052 \u00b7 Crest \u22120.045"),
 ("EMT-TF axis","FOXC1 (root) \u2192 PRRX2 (terminus)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Kim 2020 LUAD \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
