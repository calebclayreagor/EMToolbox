import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Ovarian/Zhang2019_Ovarian"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Ovarian/Zhang2019_Ovarian"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) integrates both bilateral omental sites of patient VOA11543: same-sample neighbour fraction "
  "0.997\u21920.641 (perfect-mix floor 0.559), iLISI median 1.00\u21921.78 of 2. One connected component after removing a "
  "20-cell island. Mixed AND continuous."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single (Gast/pSom)\u2192Crest developmental gradient. Gast & pSom do NOT compete out of a hub (smoothed r=\u22120.10), "
  "both oppose Crest (pSom\u2194Crest r=\u22120.64, Gast\u2194Crest r=\u22120.44). Along pseudotime Gast falls (\u03c1 \u22120.50), Crest rises "
  "to a terminal tip (\u03c1 +0.34, decile pt=0.80). Joint pSom&Crest enrichment 0.35 (<1 = inverse gradient)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks). No bifurcation, so the "
  "branching-only hub cross-repression test is not run (correlation / modules notebooks are not produced)."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("HGSOC bilateral ovarian tumour (Zhang et al., 2019), 10x \u2014 2,782 malignant cells over 2 omental sites "
 "(1 patient, VOA11543 left+right ovary); predominantly low-cycling (~9% cycling). Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces in the non-branching form (Linear-pSom/Crest): one continuous gastrulation \u2192 neural-crest "
 "axis, Crest terminal. G1 GO / G2 GO / G3 NA. EMT-TFs SNAI1 (root-side) \u2192 FOXC1 (terminus).")
params=[
 ("Sample threshold","\u2265100-cell floor; 2 bilateral sites (no cliff) \u2192 2/2, 2,802 cells"),
 ("Overdispersed genes","1,247 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample \u03b8=10 (bilateral-site batch)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 20-cell island removed"),
 ("Geometry","non-branching; scFates curve N=20, \u03bb=0.3, \u03bc=100 (2 tips / 0 forks)"),
 ("Root","tip 0 = Gast/pSom-high, Crest-low origin"),
 ("Module means (raw)","Gast \u22120.011 \u00b7 pSom +0.042 \u00b7 Crest \u22120.034 (Linear-pSom/Crest)"),
 ("EMT-TFs","SNAI1 (root-side) \u2192 FOXC1 (terminus); FOXC/PRRX in panel"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Zhang 2019 HGSOC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
