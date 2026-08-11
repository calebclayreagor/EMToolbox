import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Breast/Chung2017_Breast"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Breast/Chung2017_Breast"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) on sample: per-neighbourhood same-sample fraction 0.75\u21920.25 (chance 0.09); iLISI 3.8\u21925.9 of 11 "
  "samples. One connected component, 0 detached islands. Samples intermix across a single continuous strip \u2014 GO."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast & pSom co-vary (raw r=+0.18) and both oppose Crest (r=\u22120.65 / \u22120.54). Along pseudotime Gast/pSom fall "
  "(\u03c1\u2248\u22120.95) while Crest rises (\u03c1=+0.95); NC-high decile at t=0.98 (terminal); joint pSom&Crest enrichment 0.37<1 "
  "\u2014 inverse terminal gradient, a single (Gast/pSom)\u2192Crest axis. Present but not resolved into two arms \u2014 GO."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Non-branching topology (curve: 2 tips, 0 forks across N=15/20/30; PPT tree also 0 forks). No bifurcation to test \u2014 NA."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (Chung et al., 2017), SmartSeq2 \u2014 317 malignant cells (13 samples reported) \u2192 309 analysed "
 "(11 samples \u226510 cells). Sparse plate-based data. Non-branching Linear-pSom/Crest.")
verdict=("The embryonic pattern reproduces as a single gastrulation/somitogenesis \u2192 neural-crest axis (non-branching); "
 "no Gast\u2194pSom bifurcation, so Gate 3 is NA. Geometry Linear-pSom/Crest \u2014 consistent with the linear outcome across "
 "most CCCA datasets. EMT-TFs FOXC1 (early/root) \u2192 SNAI1 (late/terminus).")
params=[
 ("Threshold","\u226510 cells/sample (SmartSeq2 scale; anchor floor 100 would empty it) \u2192 11/12, 309 cells"),
 ("Embedding","Harmony \u03b8=10; n_pcs=20, n_neighbors=30, spread=1.3; 401 HVG"),
 ("Trajectory","scFates curve (non-branching), N=20, \u03bb=0.3, \u03bc=100; fold-free (2.98)"),
 ("Root","Gast/pSom-high, Crest-low tip (Gast/pSom early, Crest late); lower-cycling pole"),
 ("Geometry","Linear-pSom/Crest; pSom globally strongest (Gast \u22120.276, pSom +0.124, Crest \u22120.074)"),
 ("EMT-TFs","FOXC1 (early/root) \u2192 SNAI1 (late/terminus); 10-TF panel, VIM excluded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Chung 2017 breast cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
