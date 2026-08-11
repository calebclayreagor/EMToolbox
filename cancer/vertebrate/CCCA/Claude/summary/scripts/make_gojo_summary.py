import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Brain/Gojo2020_Brain"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Brain/Gojo2020_Brain"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony \u03b8-sweep on sample: sample iLISI 1.5\u21926.6 (\u03b8=10), one connected component (0 islands); PF/ST/SP "
  "subgroups grade continuously across one cloud (subgroup iLISI stays ~1.6 \u2014 biology preserved)."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching: shared Gast/pSom body with an inverse terminal Crest gradient (Crest-high decile mean pseudotime "
  "= 0.97). Crest opposes Gast (r=\u22120.50) and pSom (r=\u22120.38); Gast~pSom weak (\u22120.20)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No competing Gast/pSom arms (weak \u22120.20, no bifurcation) \u2014 branching-only test does not apply."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Pediatric ependymoma (Gojo et al., 2020), SmartSeq2, 5,378 malignant cells across 20 samples (threshold "
 "\u2265110/sample; PF/ST/SP molecular subgroups).")
verdict=("Pattern reproduces as the non-branching case \u2014 one continuous gastrulation/somitogenesis \u2192 neural-crest "
 "axis, no Gast/pSom bifurcation. Geometry: Linear-pSom/Crest. EMT-TFs overlay TWIST1 (earlier) \u2194 ZEB1 (terminus).")
params=[
 ("Min-cell threshold","\u2265110 / sample (largest gap 140\u219288, geometric mean)"),
 ("Cells retained","5,551 \u2192 5,378 (20/22 samples above threshold; 0 islands)"),
 ("Overdispersed genes","4,997 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample \u03b8=10 (n_pcs=20, spread=1.3); iLISI 6.6"),
 ("Geometry","Non-branching; scFates curve N=30, \u03bb=0.3, \u03bc=100 (2 tips, 0 forks)"),
 ("Root","Gast/pSom-high, Crest-low tip (Crest is late/terminal)"),
 ("Module means (raw)","Gast +0.116 \u00b7 pSom +0.329 \u00b7 Crest +0.003 (pSom-dominant)"),
 ("EMT-TFs","TWIST1 (earlier) \u2194 ZEB1 (terminus); FOXC1/SNAI1/ZEB2/PRRX1 detected"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Gojo 2020 pediatric ependymoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
