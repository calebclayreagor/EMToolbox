import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Hematologic/Nam2019_Hematologic"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Nam2019_Hematologic"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) integrates all 10 samples + both group leaves: per-neighbourhood iLISI 1.43\u21923.90 of a 4.94 "
  "perfect-mixing ceiling. One connected component (1 speck removed). Mixed AND continuous."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching case: a single (Gast/pSom)\u2192Crest developmental gradient. Gast & pSom co-vary (smoothed r=+0.23), "
  "both oppose Crest (Gast\u2194Crest r=\u22120.73, pSom\u2194Crest r=\u22120.71). Along pseudotime Gast/pSom fall (\u03c1 \u22120.63/\u22120.66), "
  "Crest rises to a terminal tip (decile pt=0.86). Inverse terminal gradient, no Gast-arm inversion."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks across Nodes=15/20/30). No "
  "bifurcation, so the branching-only hub cross-repression test is not run."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Myeloproliferative neoplasms (CALR-mut ET/MF) (Nam et al., 2019), 10x \u2014 22,605 malignant cells over 10 "
 "samples (2 group leaves); low-cycling Gast/pSom root pole and a cycling Crest terminus, one continuous manifold. "
 "Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces in the non-branching form (Linear-pSom/Crest): one continuous gastrulation/somitogenesis "
 "\u2192 neural-crest axis, Crest terminal. G1 GO / G2 GO / G3 NA. EMT-TFs ZEB1 (early/root) \u2192 ZEB2 (terminus).")
params=[
 ("Sample threshold","\u2265100 cells (no cliff) \u2192 10/10 samples, 22,606 cells"),
 ("Overdispersed genes","2,162 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample \u03b8=10 (iLISI plateau 5\u201310, declines at 20)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 1 island removed \u2192 22,605"),
 ("Geometry","non-branching curve (N=20, \u03bb=0.3, \u03bc=100): 2 tips / 0 forks; corr(t,DC1)=0.98"),
 ("Root","tip 0 = Gast/pSom-high, Crest-low origin"),
 ("Module means (raw)","Gast \u22120.036 \u00b7 pSom +0.008 \u00b7 Crest +0.009 (Linear-pSom/Crest)"),
 ("EMT-TFs","ZEB1 (early/root) \u2192 ZEB2 (late/terminus); detection-gated, FOXC/PRRX/SNAI in panel"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Nam 2019 myeloproliferative neoplasms \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
