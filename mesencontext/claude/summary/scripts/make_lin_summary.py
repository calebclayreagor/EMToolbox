import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Pancreas/Lin2020_Pancreas"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Pancreas/Lin2020_Pancreas"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) integrates 15 samples (iLISI 1.0\u21924.1, same-sample frac 0.94\u21920.45); one continuous "
  "connected component after removing a justified detached island (652 cells, 14 samples, developmentally flat)."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single pSom\u2192Crest axis: pSom high over ductal body falls along pseudotime (\u03c1=\u22120.59), Crest rises to a "
  "terminal end (\u03c1=+0.32, decile pt 0.82); anti-correlated in space (r=\u22120.38, joint-high enrichment 0.52 = no "
  "hub). Gast weak (\u03c1=\u22120.24). Crest terminal, not on the Gast end \u2192 no inversion flag."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No bifurcation (branching-only gate). Geometry is linear, so the tree cross-repression test does not apply."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Pancreatic Ductal Adenocarcinoma (Lin et al., 2020), 10x \u2014 16 samples; 10,993 malignant cells (10,304 "
 "after threshold + island removal) enter the analysis; the whole malignant manifold enters the trajectory "
 "(non-branching linear geometry).")
verdict=("The embryonic pattern reproduces as a single somitogenesis\u2192neural-crest developmental axis (the "
 "non-branching / collapsed-bifurcation case) \u2014 no Gast/pSom hub, no competing arms; Linear pSom/Crest. Gate 1 GO, "
 "Gate 2 GO (non-branching), Gate 3 NA. EMT-TFs FOXC1 (root-relative) \u2192 SNAI2 (terminus).")
params=[
 ("Threshold","53 cells (geom-mean 76\u219237, gap ratio 2.05) \u2192 15/16 kept"),
 ("Island","652 cells removed (radius-graph 6\u00d7 med-NN; multi-sample, dev-flat)"),
 ("Integration","Harmony \u03b8=10; n_pcs=20; spread=1.3"),
 ("Trajectory","scFates curve (ElPiGraph) Nodes=20, \u03bc=100 (2 tips, 0 forks; self-approach 2.98)"),
 ("Root","pSom-high / Crest-low tip"),
 ("Scope","whole manifold kept (modules cycle-free; axis holds in non-cycling lobe)"),
 ("EMT-TF axis","FOXC1 (root-relative) \u2192 SNAI2 (terminus)"),
 ("Caveat","pt vs cycling \u03c1=+0.42 (cycle-split lobes)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Lin 2020 PDAC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
