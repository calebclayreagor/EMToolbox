import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Hematologic/Roider2020_Hematologic"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Roider2020_Hematologic"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) integrates 9 patients despite a severe clonal batch effect: same-sample neighbour fraction "
  "0.995\u21920.26; iLISI median 1.00\u21924.58 of 9. One connected component (1 speck removed). Mixed AND continuous."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching case: a single (Gast/pSom)\u2192Crest developmental gradient with organized Gast\u2194pSom cross-repression "
  "(smoothed r=\u22120.41; Crest\u2194pSom r=\u22120.52). Along pseudotime Gast/pSom fall (\u03c1 \u22120.77/\u22120.15), Crest rises to a "
  "terminal tip (decile pt 0.77). Joint pSom&Crest enrichment 0.50 (<1 = inverse gradient, not a hub)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable \u2014 non-branching topology (principal curve, 2 tips / 0 forks, fold self-approach 2.95). No resolved "
  "bifurcation, so the branching-only hub cross-repression test is not run."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("B-cell lymphoma lymph-node biopsies (Roider et al., 2020), 10x \u2014 22,599 malignant cells over 9 samples "
 "(DLBCL/FL/tFL); reactive-lymph-node normals contribute no malignant cells; single low-cycling body (~11% cycling). "
 "Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces in the non-branching form (Linear-pSom/Crest): one continuous gastrulation/somitogenesis "
 "\u2192 neural-crest axis, Crest terminal. G1 GO / G2 GO / G3 NA. EMT-TFs ZEB2 (early/root) \u2192 ZEB1 (terminus).")
params=[
 ("Sample threshold","\u2265100 cells (largest gap 1583\u2192327 above floor) \u2192 9/9 samples"),
 ("Overdispersed genes","1,334 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample \u03b8=10 (mixing plateau; clonal patient batch)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 1 island removed \u2192 22,599"),
 ("Geometry","non-branching curve N=20, \u03bb=0.3, \u03bc=100; 2 tips / 0 forks (2.95)"),
 ("Root","tip 0 = Gast/pSom-high, Crest-low, low-cycling origin"),
 ("Module means (raw)","Gast \u22120.027 \u00b7 pSom +0.002 \u00b7 Crest +0.005 (Linear-pSom/Crest)"),
 ("EMT-TFs","ZEB2 (early/root) \u2192 ZEB1 (late/terminus); only ZEB1/ZEB2 clear >3% floor"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Roider 2020 B-cell lymphoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
