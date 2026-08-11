import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Breast/Bassez2021_Breast-5"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Breast/Bassez2021_Breast-5"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) on sample: per-neighbourhood iLISI 1.6\u21927.8 of 34 samples (\u03b8 sweep 1/2/5/10, mixing rises to a "
  "plateau). One connected component, 0 detached islands. Samples intermix across one continuous strip \u2014 GO."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast & pSom cross-repress (smoothed r=\u22120.70; node-cluster r=\u22120.55) with NO co-expression hub (both-high "
  "enrichment 0.11<1). Crest opposes pSom (r=\u22120.91) as an inverse terminal gradient (NC-high decile pt=0.82; joint "
  "pSom&Crest 0.25<1). A single cross-repressive (Gast/pSom)\u2192Crest axis, not two diverging arms \u2014 GO."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Non-branching topology (curve: 2 tips, 0 forks across N=15/20/30; PPT tree tips all pSom-high/Gast-low \u2014 no Gast "
  "arm). No bifurcation to test \u2014 NA."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (Bassez et al., 2021), 10x \u2014 13,834 malignant-epithelial cells (scoped from 65,885 CCCA "
 "\"Malignant\", 21% epithelial) across 34 samples (\u226520 cells). Non-branching Linear.")
verdict=("The embryonic pattern reproduces on the correctly-scoped malignant epithelium as a single "
 "gastrulation/somitogenesis \u2192 neural-crest axis with organised Gast/pSom cross-repression (non-branching); no "
 "co-expression hub diverging into two arms, so Gate 3 is NA. Geometry Linear. EMT-TFs FOXC1 (early/root) \u2192 SNAI2 "
 "(late/terminus).")
params=[
 ("Scoping","CCCA \"Malignant\" 21% epithelial \u2192 scoped to 13,834 epithelial cells"),
 ("Threshold","\u226520 epithelial cells/sample (re-derived); 34/42 samples"),
 ("Embedding","Harmony \u03b8=10; n_pcs=20, n_neighbors=30, spread=1.3; 2,211 HVG"),
 ("Trajectory","scFates curve (non-branching), N=20, \u03bc=100; fold-free (2.98)"),
 ("Root","pSom-high, Crest-low tip (pSom early, Crest late); \u03c1 pSom \u22120.34, Crest +0.44"),
 ("Geometry","Linear; raw means Gast \u22120.027 \u00b7 pSom +0.030 \u00b7 Crest \u22120.011"),
 ("EMT-TFs","FOXC1 (early/root) \u2192 SNAI2 (late/terminus); VIM excluded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Bassez 2021 breast cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
