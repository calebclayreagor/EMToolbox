import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Prostate/Dong2020_Prostate"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Prostate/Dong2020_Prostate"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Malignant cells from all 4 patients (9,698; \u2265100-cell floor, no sample dropped) form one continuous manifold "
  "\u2014 0 detached islands, single connected component; every transcriptional lobe contains all 4 patients. "
  "Judged on the embedding, not the composition-capped iLISI (1.78/4, one patient \u224849% of cells)."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Single developmental axis: Gast & pSom co-vary (smoothed r=+0.90; joint-high enrichment 2.4 \u2014 an overlap, "
  "not competing arms) and jointly oppose neural-crest (pSom\u2194Crest r=\u22120.53). Along pseudotime Gast/pSom "
  "decline (\u03c1 \u22120.58/\u22120.71), Crest rises to a terminal end (\u03c1 +0.79, Crest-high decile pt 0.98). "
  "Non-branching \u2014 passes."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "No bifurcation (fold-free single curve, 2 tips / 0 forks). The branching-only cross-repression test does not "
  "apply; correlation & modules notebooks are not produced."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Prostate adenocarcinoma (Dong et al. 2020), 10x \u2014 9,698 malignant cells across 4 patients "
 "(\u2265100-cell floor, all samples kept; publication cell_type calls). Non-branching embryonic axis.")
verdict=("The embryonic program reproduces as a single monotone gradient \u2014 a Gast/pSom-high (overlap) origin "
 "flowing to an inverse neural-crest terminus \u2014 the collapsed-bifurcation (Linear-pSom/Crest) case, distinct "
 "from Puram\u2019s hub-and-spoke. Gate 1 GO, Gate 2 GO, Gate 3 NA.")
params=[
 ("Malignant / threshold","9,698 cells, 4 patients; \u2265100 floor (no cliff; all kept)"),
 ("Overdispersion / PCA","1,670 overdispersed; 50 PC \u2192 20 for kNN"),
 ("Integration","Harmony on sample, \u03b8=10 (one patient \u224849%); spread=1.3"),
 ("Island removal","radius graph 6\u00d7 median NN \u2192 0 removed (one component)"),
 ("Compartments","Leiden res=0.15 \u2192 Body 8,696 + Cycling 1,002; whole kept"),
 ("Cell-cycle","cc-free (anti-corr survives 7,988 non-cycling; pt\u2194cyc \u03c1=\u22120.24)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100; 2 tips 0 forks (self-approach 2.59)"),
 ("Root / Orientation","tip 2 (Gast/pSom-high); rigid rotation \u2212170.4\u00b0, corr(x_lin,pt)=+0.85"),
 ("EMT-TFs","SNAI1 (root, 6.0%) \u2192 TWIST1 (terminus, 26.8%); \u0394pt=0.37"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Dong 2020 Prostate \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
