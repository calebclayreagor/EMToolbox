import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Ovarian/Olbrecht2021_Ovarian"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Ovarian/Olbrecht2021_Ovarian"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "6 samples / 5 patients share ONE continuous manifold (single kNN component, no detached islands). "
  "Per-neighbourhood iLISI rises 1.00\u21923.33 under Harmony (\u03b8=10): sample-integrated, not a per-patient "
  "archipelago. Judged on the regenerated embedding, not a scalar alone."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.44; +0.71 among non-cycling) and BOTH oppose Crest (pSom\u2194Crest r=\u22120.68); one "
  "developmental axis, Crest an inverse terminal gradient. Cell-cycle confound tested & rejected: "
  "anti-correlation survives excluding cycling cells; modules cc-free."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Branching-only. No bifurcation (curve: 2 tips / 0 forks, fold-free) \u2014 not tested. The non-branching case "
  "passes Gate 2 and reports Gate 3 as NA (distinct from a NO-GO where the pattern is absent)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("High-Grade Serous Tubo-Ovarian Carcinoma (Olbrecht et al., 2021), 10x \u2014 3,936 malignant cells across "
 "6 samples / 5 patients (\u2265155-cell threshold keeps 6/10 samples). Harmony integration on sample (\u03b8=10), "
 "principal-curve trajectory (scFates) on the whole manifold.")
verdict=("Pattern REPRODUCES (non-branching). The embryonic programme recapitulates on a single continuous axis: a "
 "Gast/pSom-high origin resolving into an inverse, terminal Neural-Crest gradient (pSom\u2194Crest r=\u22120.68; along "
 "pseudotime Gast \u22120.33, pSom \u22120.06, Crest +0.40 terminal). Linear-pSom/Crest geometry (means Gast +0.029 / "
 "pSom +0.077 / Crest \u22120.020), not the Puram hub-and-spoke bifurcation. Gate 1 GO / Gate 2 GO / Gate 3 NA. "
 "EMT: FOXC1 (root) \u2192 ZEB1 (terminus).")
params=[
 ("Sample threshold","\u2265155 \u2192 6/10 (gap 384\u219263, ratio 6.10; geom-mean cut)"),
 ("n_pcs","20 (scree elbow; K\u00fcrten(20)/Puram(40) precedent)"),
 ("Integration","Harmony \u03b8=10 (iLISI 1.00\u21923.33, monotone)"),
 ("Island removal","0 cells (UMAP radius-graph, single component)"),
 ("Geometry","Non-branching curve (2 tips / 0 forks, fold-free)"),
 ("Root","tip 0 = Gast/pSom-high; corr(x_lin,pt)=+0.84"),
 ("Cell-cycle","whole manifold kept (pSom\u2194Crest survives non-cycling \u22120.63; cc-free)"),
 ("EMT-TF readout","FOXC1 (root, \u03c1=\u22120.06) \u2192 ZEB1 (terminus, \u03c1=+0.11)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Olbrecht 2021 HGSOC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
