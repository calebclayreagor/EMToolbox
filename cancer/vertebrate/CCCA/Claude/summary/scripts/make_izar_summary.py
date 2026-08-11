import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Ovarian/Izar2020_Ovarian"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Ovarian/Izar2020_Ovarian"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Both platforms and all 11 retained samples intermix on one connected manifold; the platform batch that "
  "sample-only Harmony leaves (same-platform frac 1.00) is removed by joint platform+sample Harmony (\u21920.65). No "
  "islands."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Shared Gast/pSom gradient (geography r=+0.53; reproduced within each platform) with Crest the inverse, terminal "
  "end (Crest~Gast \u22120.68, Crest~pSom \u22120.92; Crest-high decile at pt 0.81)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Non-branching principal curve (0 forks across Nodes 15\u201330), so there is no hub to test."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("HGSOC malignant ascites (Izar et al., 2020), two platforms (SmartSeq2 1,158 + 10x 751 malignant); 1,909 "
 "loaded \u2192 1,904 after thresholding. Both leaves concatenated on the shared gene space; platform treated as a "
 "batch covariate alongside sample.")
verdict=("The embryonic-program pattern reproduces as a single non-branching axis \u2014 a Gast/pSom-high developmental "
 "origin flowing to a neural-crest-high terminus, with proliferation orthogonal to (not aligned with) the axis. "
 "Consistent with the Linear-pSom/Crest outcome seen across most of the atlas.")
params=[
 ("Min cells/sample","10 (mult-gap 21\u21925; keeps 11/12)"),
 ("Integration","Harmony [platform, sample] \u03b8=10; PCA20"),
 ("Scope","whole manifold (no lobe scoping)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","tip Gast/pSom-high, Crest-low"),
 ("Geometry","Linear (non-branching); 0 forks"),
 ("EMT-TFs","SNAI2 (root) \u2192 PRRX2 (terminus)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Izar 2020 HGSOC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
