import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Ovarian/Shih2018_Ovarian"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Ovarian/Shih2018_Ovarian"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=20) collapses the strong patient batch effect: same-sample neighbour fraction 0.73\u21920.20 "
  "(perfect-mixing floor 0.16), iLISI median 2.98\u21925.82 of 7 samples. One connected component (0 islands). Patient "
  "islands (pre-Harmony) fuse into one continuous mixed cloud."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single (Gast/pSom)\u2192Crest developmental gradient. Gast & pSom co-vary (smoothed r=+0.23; joint enrichment 0.95 ~ "
  "origin overlap), both oppose Crest (Gast\u2194Crest r=\u22120.80, pSom\u2194Crest r=\u22120.74). Along pseudotime Gast/pSom fall "
  "(\u03c1 \u22120.86/\u22120.62), Crest rises to a terminal tip (decile pt=0.99); joint pSom&Crest enrichment 0.26 (<1 = inverse "
  "gradient, not a hub)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks; PPT tree 0 branch nodes). No "
  "bifurcation, so the branching-only hub cross-repression test is not run."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("HGSOC/LGSOC ovarian tumours (Shih et al., 2018), SmartSeq2 \u2014 633 malignant cells over 7 samples; sparse "
 "(~1250 genes/cell), a single low-cycling body with a cycling spur (~43% cycling). Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces in the non-branching form (Linear-pSom/Crest): one continuous gastrulation/somitogenesis "
 "\u2192 neural-crest axis, Crest terminal. G1 GO / G2 GO / G3 NA. EMT-TFs SNAI1/FOXC1/PRRX2 all origin/root-enriched "
 "(no terminal EMT-TF).")
params=[
 ("Sample threshold","floor \u2265100 rejected (3/16); cliff 60\u219237 \u2192 geo-mean 47 \u2192 7/16, 633 cells"),
 ("Feature selection","scFates HVG underpowered on 633 sparse cells (33) \u2192 Seurat HVG 2000"),
 ("Integration","Harmony on sample \u03b8=20 (mixing collapses to floor; strong ovarian batch)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3 (SS2 precedent); 0 islands removed"),
 ("Geometry","non-branching curve N=20, \u03bb=0.3, \u03bc=100; 2 tips / 0 forks (2.84)"),
 ("Root","tip 2 = Gast/pSom-high, Crest-low origin; axis cell-cycle-free (\u03c1=\u22120.03)"),
 ("Module means (raw)","Gast \u22120.013 \u00b7 pSom +0.065 \u00b7 Crest \u22120.034 (Linear-pSom/Crest)"),
 ("EMT-TFs","SNAI1 (8.4%), FOXC1 (6.8%), PRRX2 (3.5%) \u2014 all origin/root-enriched; overlay SNAI1 & FOXC1"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Shih 2018 ovarian cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
