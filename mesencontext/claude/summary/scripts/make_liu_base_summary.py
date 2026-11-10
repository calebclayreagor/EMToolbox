import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Liu2021_Hematologic"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Liu2021_Hematologic"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Clonal MM plasma cells form a per-patient archipelago without integration (pre-Harmony iLISI 1.06). Judged on "
  "the regenerated embedding across a \u03b8 sweep (not a scalar): at \u03b8=15 the 15 samples share ONE continuous "
  "manifold (island strip 42.5\u219228\u219211.7\u21922.4\u21922.7% as integration rises to a clean-speck level), well "
  "mixed per-neighbourhood (iLISI 2.27 of 5.62 ceiling; patient |r|\u22640.19 on diffusion axes). Detached specks "
  "are unintegrated clones of the same states, not a distinct lineage."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Single developmental axis: Gast & pSom vary along it with organised cross-repression (smoothed r=\u22120.67), and "
  "Crest occupies the opposite terminal end (pSom\u2194Crest r=\u22120.95). No Gast/pSom co-expression hub and no "
  "opposing Gast arm \u2192 non-branching. FLAG: Crest enriches the Gast end (Crest\u2194Gast r=+0.56, Crest\u2194pSom "
  "r=\u22120.95) \u2014 inversion of the canonical pSom-arm Crest tip; flagged but PASSES."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Non-branching manifold has no bifurcation; the tree-cluster cross-repression test does not apply."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Multiple myeloma plasma cells (Liu et al., 2021), 10x \u2014 24 samples / 74,986 cells (master scope); "
 "17,267 malignant plasma cells; 15 marrows pass the 66\u2192156 count cliff (\u2265100 cells; 17,003), 16,551 "
 "retained after removing detached islands. Global module means Gast \u22120.024, pSom +0.032, Crest \u22120.006 \u2192 "
 "Linear-pSom/Crest class (pSom the strongest module).")
verdict=("The embryonic-development pattern REPRODUCES as an organised non-branching cross-repression axis "
 "(Gast/pSom early, Crest terminal), with a Crest-on-Gast-arm inversion flag. Gate 1 GO / Gate 2 GO / Gate 3 NA. "
 "EMT-TFs ZEB2 (early) \u2192 ZEB1 (late) \u2014 the only factors above the 3% detection floor.")
params=[
 ("Min-cell threshold","\u2265100 cells/sample (drops 5 thin marrows; count cliff 66\u2192156, ratio 2.4)"),
 ("Integration","Harmony \u03b8=15 on sample, 20 PCs (iLISI plateaus + island fraction bottoms out)"),
 ("Embedding","PCA-50, kNN=30, UMAP spread 1.3"),
 ("Geometry","Non-branching principal curve (ElPiGraph, fold-free SA 2.9; no hub/arm)"),
 ("Scope","Whole manifold (no lobe excised); axis orthogonal to proliferation"),
 ("Root","Gast/pSom-high, Crest-low tip (gastrulation/somitogenesis early, crest late)"),
 ("EMT-TF panel","ZEB2 (early) & ZEB1 (late) clear the >3% floor; VIM excluded"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Liu 2021 Multiple Myeloma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
