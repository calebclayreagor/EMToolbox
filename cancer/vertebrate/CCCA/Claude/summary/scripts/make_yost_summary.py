import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Skin/Yost2019_Skin"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Skin/Yost2019_Skin"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=5) integrates all 5 patients: same-sample neighbour fraction 0.94\u21920.41, iLISI median 1.02\u21923.21 of 5. "
  "One connected component (0 islands). Mixed AND continuous."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single (Gast/pSom)\u2192Crest developmental gradient. Gast & pSom co-vary (smoothed r=+0.61), both oppose Crest "
  "(pSom\u2194Crest r=\u22120.84, Gast\u2194Crest r=\u22120.82). Along pseudotime Gast/pSom fall (\u03c1 \u22120.43/\u22120.75), Crest rises to a "
  "terminal tip (decile pt=0.84); joint pSom&Crest enrichment 0.32 (<1 = inverse gradient, not a hub)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks). No bifurcation, so the "
  "branching-only hub cross-repression test is not run."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Cutaneous basal cell carcinoma (Yost et al., 2019), 10x \u2014 3,391 malignant cells over 5 patients (5/16 kept "
 "at \u2265110-cell floor); single low-cycling body (~11% cycling). Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces in the non-branching form (Linear-pSom/Crest): one continuous gastrulation/somitogenesis "
 "\u2192 neural-crest axis, Crest terminal. G1 GO / G2 GO / G3 NA. EMT-TFs SNAI1 (early/root) \u2192 FOXC1 (late/terminus).")
params=[
 ("Sample threshold","110 cells (geo-mean of cliff 254\u219248, ratio 5.29) \u2192 5/16, 3,391 cells"),
 ("Overdispersed genes","1007 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample \u03b8=5 (mixing plateau; patient-specific batch)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 0 islands removed"),
 ("Geometry","non-branching curve N=20, \u03bb=0.3, \u03bc=100; 2 tips / 0 forks (2.92)"),
 ("Root","tip 2 = Gast/pSom-high, Crest-low origin (from signature order)"),
 ("Module means (raw)","Gast \u22120.015 \u00b7 pSom +0.046 \u00b7 Crest \u22120.011 (Linear-pSom/Crest)"),
 ("EMT-TFs","SNAI1 (early/root) \u2192 FOXC1 (late/terminus); detection-gated; FOXC/PRRX in panel"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Yost 2019 BCC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
