import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Skin/Li2019_Skin"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Li2019_Skin"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Mixed & continuous. At Harmony \u03b8=40 the 3 samples share ONE connected component (0 detached cells), sample- "
  "and cell-cycle-mixed throughout. The 2-island split at \u03b8=20 is a technical MARS-seq low-complexity axis "
  "(minor island 11/12 markers are MT-pseudogenes / lincRNAs) merged by stronger integration, not deleted."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Embryonic pattern present (non-branching). pSom/Gast co-localize at the origin with organized Gast\u2194pSom "
  "anti-correlation (r=\u22120.61); Crest is an inverse terminal gradient (Crest\u2194pSom r=\u22120.59) peaking at the "
  "terminus (decile pseudotime 0.80), NOT on a Gast arm \u2014 no inversion flag. No bifurcation."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (scFates curve: 2 tips, 0 forks, fold self-approach 2.98; a "
  "PPT tree adds no stable fork). With a single axis and no bifurcation there is no hub to test for mutual "
  "Gast\u2194pSom cross-repression, so Gate 3 is NA (branching-only)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Melanoma (Li et al., 2019), MARS-seq \u2014 1,082 malignant cells (3 samples \u2265 threshold); low-pSom, "
 "Crest-terminal melanoma (neural-crest lineage).")
verdict=("The embryonic program REPRODUCES as a non-branching axis \u2014 a single gastrulation/somitogenesis \u2192 "
 "neural-crest developmental gradient (Gate 1 GO / Gate 2 GO / Gate 3 NA), the expected melanoma (neural-crest "
 "lineage) pattern. EMT-TFs FOXC1 (body/origin) \u2192 PRRX1 (terminus).")
params=[
 ("Min-cell threshold","1160\u21921082 cells; dominant cliff 154\u219221 (ratio 7.3); geom-mean 56 keeps p25/p21/p26, drops 17 spillover"),
 ("Integration","Harmony \u03b8=40 on sample (first strength giving 1 continuous component; \u03b8=20 leaves 2 islands, \u03b8=80 over-fragments); n_pcs=20"),
 ("Geometry / root","Non-branching scFates curve; root = Gast/pSom-high, Crest-low tip; fold-free (SA 2.98); corr 0.99"),
 ("Module means (raw)","Gast \u22120.015 \u00b7 pSom +0.016 \u00b7 Crest \u22120.002 (Linear-pSom/Crest)"),
 ("EMT-TFs","FOXC1 (body/origin) \u00b7 PRRX1 (terminus); wide panel (Snail/Zeb/Twist + FOXC/PRRX); VIM excluded"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Li 2019 Melanoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
