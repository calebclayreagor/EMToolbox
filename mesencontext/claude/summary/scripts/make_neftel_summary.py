import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Brain/Neftel2019_Brain"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Brain/Neftel2019_Brain"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "10x leaf scoped (SmartSeq2 non-integrable: platform iLISI~1.0 across \u03b8=2\u201320, disjoint samples, UMI vs TPM). "
  "7/10 samples (\u2265413 cells) on one connected component; sample iLISI 2.9/7."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Shared Gast/pSom gradient (r=+0.79, co-vary) with Crest an inverse terminal readout (r=\u22120.89/\u22120.90). Curve "
  "fold-free (0 forks); Crest-high decile at pseudotime 0.76."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Gast/pSom co-vary (not compete) \u2192 single collapsed axis, no bifurcation to test."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Glioblastoma (Neftel et al., 2019); SmartSeq2+10x atlas, 10x leaf analyzed; 11,172 malignant raw \u2192 10,229 "
 "final. Platform-exclusive patients make the SmartSeq2 leaf non-integrable with 10x.")
verdict=("Pattern reproduces as a non-branching embryonic axis: Gast/pSom-high origin \u2192 Crest-high terminus; "
 "developmental order pSom \u03c1=\u22120.74, Crest \u03c1=+0.55 along pseudotime, checked off a diffusion embedding "
 "independent of the fitted UMAP. Linear-pSom/Crest (pSom globally strongest).")
params=[
 ("Min cells/sample","\u2265413 (mult-gap 647\u2192264; 7/10)"),
 ("Integration","Harmony \u03b8=10; PCA20; spread=1.3"),
 ("Scope","10x leaf only (SmartSeq2 non-integrable)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","Gast/pSom-high tip"),
 ("Geometry","Linear (non-branching); 0 forks"),
 ("EMT-TFs","ZEB2 (early) \u2192 PRRX1 (late)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Neftel 2019 GBM \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
