import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Giustacchini2017_Hematologic"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Giustacchini2017_Hematologic"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Harmony(\u03b8=6) integrates all 35 plates: cross-sample neighbour fraction 0.82; one connected component, 0 "
  "islands removed. Read on the regenerated embedding across an n_pcs/\u03b8 sweep, not a scalar: \u03b8=6 folds the "
  "blast-crisis patient triad into the body (vs deleting ~180 cells at \u03b8=2)."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Non-branching case: a single (Gast/pSom)\u2192Crest developmental gradient. Gast & pSom co-vary (smoothed "
  "r=+0.70), both oppose Crest (Gast\u2194Crest r=\u22120.93, pSom\u2194Crest r=\u22120.80). Along pseudotime Gast falls "
  "(\u03c1 \u22120.57), Crest rises to a terminal tip (\u03c1 +0.60, Crest-high decile pt=0.90). Joint pSom&Crest "
  "enrichment 0.27 (<1 = inverse gradient, not a co-expression hub)."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks). No bifurcation, so the "
  "branching-only hub cross-repression test is not run (correlation / modules notebooks not produced, per spec)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("CML (Giustacchini et al., 2017), SmartSeq2 \u2014 2,055 malignant BCR-ABL cells over 36 patient plates; "
 "single low-cycling body (~16% cycling), one continuous developmental axis.")
verdict=("Pattern reproduces in the non-branching Linear-Gast form: one continuous gastrulation/somitogenesis "
 "\u2192 neural-crest axis, Crest terminal. Gate 1 GO / Gate 2 GO / Gate 3 NA. EMT-TFs ZEB1 & ZEB2 (only factors "
 "clearing detection), rising toward the Crest terminus.")
params=[
 ("Sample threshold","n\u226520 cells (35/36 plates, 2,040); \u2265100 floor rejected (SmartSeq2 caps at 154); gap 15\u219222"),
 ("Overdispersed genes","5,909 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample, \u03b8=6 (stability sweep; folds blast-crisis patients into body)"),
 ("Embedding","n_pcs=20 (scree elbow; n_pcs=40 fragments a patient speck)"),
 ("Geometry","Non-branching scFates curve N=20 \u03bb=0.3 \u03bc=100; 2 tips/0 forks, SA 2.97; corr(x_lin,pt)=+0.99"),
 ("Root","curve tip 0 = Gast/pSom-high, Crest-low origin"),
 ("Module means (raw)","Gast +0.016 \u2265 pSom +0.013 > Crest \u22120.016 (Linear-Gast); cell-cycle-free"),
 ("EMT-TFs shown","ZEB1 (23%) & ZEB2 (42%); FOXC1/PRRX1/TWIST1/SNAI1 <2%, gated out"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Giustacchini 2017 CML \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
