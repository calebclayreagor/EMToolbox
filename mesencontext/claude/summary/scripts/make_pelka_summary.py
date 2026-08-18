import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Colorectal/Pelka2021_Colorectal"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Colorectal/Pelka2021_Colorectal"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "64 tumours integrate to one continuous manifold (same-sample neighbour fraction 0.71\u21920.10, robust across "
  "\u03b8 2\u201310); a single connected component after island removal."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching (2 tips, 0 forks). Shared developmental gradient with neural crest as the inverse terminal end: "
  "pSom\u2194Crest spatial r=\u22120.89; along pseudotime pSom \u03c1=\u22120.79, Crest \u03c1=+0.83."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No bifurcation \u2192 no hub to test. Cross-repression gate not applicable to the non-branching case."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Colorectal cancer (Pelka et al., 2021), 10x; 108,999 published-malignant cells across 64 tumours, all "
 "samples above the atlas 100-cell floor; 108,979 after removing 20 detached-island cells.")
verdict=("Pattern reproduces (non-branching, Linear-pSom/Crest): one continuous gastrulation/somitogenesis \u2192 "
 "neural-crest developmental axis. Gate 1 GO / Gate 2 GO / Gate 3 NA. No competing arms, so no hub r. EMT-TFs "
 "SNAI1 and FOXC1 both localise to the root; canonical ZEB1/TWIST1 below the 3% floor.")
params=[
 ("Min cells/sample","\u2265100 floor (gap-rule degenerate 1.58)"),
 ("Integration","Harmony \u03b8=10; n_pcs=20 (4,556 HVGs)"),
 ("Scope","whole manifold (proliferation orthogonal)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100 (SA 2.99)"),
 ("Root node","somitogenesis/gastrulation-high tip"),
 ("Geometry","Linear (non-branching); 2 tips / 0 forks"),
 ("EMT-TFs","SNAI1 \u00b7 FOXC1 (both root-loaded)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Pelka 2021 colorectal cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
