import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Ovarian/Olbrecht2021_Ovarian-1"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Ovarian/Olbrecht2021_Ovarian-1"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony(sample) swept over \u03b8\u00d7n_pcs with per-neighbourhood iLISI; at \u03b8=10 iLISI plateaus at 3.34/6 and the 6 "
  "samples form one intermixed, connected manifold (single component; 0 islands removed)."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast & pSom co-vary (smoothed r=+0.44) at the root pole; Crest is an inverse terminal gradient (Crest~pSom "
  "r=\u22120.68, Crest-high decile mean pseudotime 0.87). A single embryonic axis, not two competing arms."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Branching-only. No bifurcation (PPT forks scale with node count 6\u219213 = noise; curve fits 0 forks, fold-free "
  "ratio 2.70), so there is no hub to test for Gast\u2194pSom mutual exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("High-grade serous tubo-ovarian carcinoma (Olbrecht et al., 2021), 10x scRNA-seq \u2014 3,936 malignant cells "
 "across 6/10 samples (\u2265155-cell threshold) enter the analysis; the whole malignant manifold enters the trajectory "
 "(non-branching linear geometry).")
verdict=("The embryonic pattern reproduces as a single collapsed axis: a Gast/pSom co-expressing developmental origin "
 "resolving into a neural-crest-high terminus (Gate 1 GO / Gate 2 GO / Gate 3 NA). Pseudotime correlations Gast "
 "\u03c1=\u22120.41, pSom \u22120.18, Crest +0.47 (smoothed). Linear-pSom/Crest geometry; Gast & pSom co-vary rather than "
 "diverge, so there is no Gast\u2013pSom bifurcation (Gate 3 NA). EMT-TFs FOXC1 (root) \u2192 ZEB1 (terminus).")
params=[
 ("Min-cell threshold","155 (geo-mean of 384\u219263 count gap, ratio 6.1) \u2192 6/10 samples"),
 ("Integration","Harmony(sample), \u03b8=10, n_pcs=20 (iLISI plateau 3.34/6)"),
 ("Island removal","radius graph 6\u00d7 median NN \u2192 0 cells removed (single component)"),
 ("Geometry","Linear-pSom/Crest \u2014 curve; 2 tips, 0 forks, fold-free 2.70"),
 ("Root","Gast/pSom-high tip (developmental origin; Crest is late)"),
 ("Pseudotime \u03c1","Gast \u22120.41, pSom \u22120.18, Crest +0.47 (smoothed)"),
 ("Overdispersed genes","1,413 (scFates find_overdispersed)"),
 ("EMT-TFs","FOXC1 (early/root) \u2192 ZEB1 (late/terminus)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Olbrecht 2021 HGSTOC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
