import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Hematologic/Gaiti2019_Hematologic"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Gaiti2019_Hematologic"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "The 7 SmartSeq2 plates and 4 patients intermix per-neighbourhood on one continuous, low-cycling manifold (iLISI "
  "1.99 pre-Harmony \u2192 5.53 of 7 samples at \u03b8=5; same-sample-neighbour fraction 0.66\u21920.21). One connected "
  "component, 0 detached islands."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single (gastrulation+somitogenesis)\u2192neural-crest axis, not a hub with two cross-repressing arms. Gast and pSom "
  "co-vary (raw r +0.07, smoothed +0.64) and both oppose Crest (raw \u22120.57 / \u22120.59); along pseudotime Gast \u03c1 \u22120.96 "
  "and pSom \u03c1 \u22120.66 fall while Crest \u03c1 +0.97 rises to a terminal tip. Joint pSom&Crest enrichment 0.43 (<1 \u2192 "
  "inverse gradient, not a hub)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Non-branching topology (principal curve: 2 tips, 0 forks, fold self-approach 3.0, stable across Nodes 15/20/30; a "
  "PPT tree finds 0 branch points) \u2014 no bifurcation, so the hub cross-repression test does not apply."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Chronic lymphocytic leukemia (Gaiti et al., 2019), SmartSeq2 (plate-based) \u2014 672 malignant CD19+ cells, "
 "7 plates / 4 patients. Non-branching Linear-pSom/Crest.")
verdict=("The embryonic pattern reproduces as a non-branching single (gastrulation/somitogenesis)\u2192neural-crest axis "
 "(Linear-pSom/Crest) \u2014 GO / GO / NA. EMT-TFs ZEB2 (terminus) vs PRRX1 (least terminus-biased); all panel TFs skew "
 "terminal, no root-end factor.")
params=[
 ("Min-cell threshold","67 (96\u219248 plate cliff geomean); 7 full plates / 672 cells"),
 ("Integration","Harmony on sample \u03b8=5; n_pcs=20; overdispersed 45 \u2192 PCA 44"),
 ("Geometry / root","principal curve (ElPiGraph), non-branching; root = tip 0 (Gast/pSom-high)"),
 ("Hub identity","NA \u2014 non-branching, no convergence hub"),
 ("EMT-TFs","ZEB2 (terminus) vs PRRX1 (least terminal); no root-end factor; VIM excluded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Gaiti 2019 CLL \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
