import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, RED, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Head-and-Neck/Chen2020_Head-and-Neck-3"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Head-and-Neck/Chen2020_Head-and-Neck-3"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "8/14 samples pass the min-cell threshold 107; Harmony(sample, \u03b8=2) fully intersperses all 8 patients; 1 "
  "connected component after island removal (438 detached cells dropped). Mixed and continuous."),
 ("Gate 2 \u2014 module geography","NO-GO",RED,
  "A robust Crest-terminal axis exists (Crest opposes Gast \u22120.64 / pSom \u22120.44, SURVIVES cell-cycle correction "
  "\u2192 not a proliferation artifact). But the defining embryonic BODY is absent: Gast/pSom are decoupled (r=+0.01 "
  "vs K\u00fcrten GO +0.33 / Puram GO \u22120.49) and pSom does not participate (r(t,pSom)=\u22120.17, flat). A two-module "
  "Gast/Crest gradient without a coupled Gast/pSom body is not the embryonic pattern."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "No bifurcation on a linear manifold \u2192 no Gast\u2194pSom arms to test. Correlation + modules notebooks not "
  "produced."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Nasopharyngeal carcinoma (Chen et al., 2020), 10x \u2014 3,236 malignant cells (8 samples).")
verdict=("NOT REPRODUCED (embryonic geography absent; Gate 2 NO-GO). Malignant NPC cells form a mixed, continuous, "
 "non-branching manifold with a real, cell-cycle-independent Crest-terminal gradient (Crest opposes Gast \u22120.64 / "
 "pSom \u22120.44 after cc-correction). But the three-module embryonic pattern is not present: Gast/pSom decoupled "
 "(r=+0.01, vs K\u00fcrten GO +0.33) and pSom does not participate (flat, r(t,pSom)=\u22120.17). This NO-GO corrects, "
 "rather than echoes, the prior attempt\u2019s 'generic-carcinoma' rationale \u2014 the axis is embryonic-flavoured and "
 "NOT mere proliferation; what fails is the coupled Gast/pSom body the gate requires.")
params=[
 ("Expression","UMI \u2192 normalize_total, log1p (no scale)"),
 ("Threshold","min 107 malignant cells/sample (gap 36\u2192107, \u00d72.97) \u2192 8 samples, 3,674 cells"),
 ("Embedding","overdispersed \u2192 PCA(19 PCs, >0.5% var) \u2192 Harmony(sample, \u03b8=2) \u2192 knn15 \u2192 UMAP \u2192 Leiden 0.3"),
 ("Island removal","438 cells (clusters 2,4,6,7,8) \u2192 3,236 cells, 1 component"),
 ("Subtypes","Cycling, Protein-maturation, Hypoxia; 3CA meta-programs + Chen calls"),
 ("Manifold","scFates curve on X_umap (non-branching; 0 branch nodes, 12-combo PPT sweep); rooted Gast/pSom-high"),
 ("EMT-TFs shown","SOX4/PRRX1/TCF4/SNAI2/ZEB2/FOXC1 + 6 more (detect\u226510%); canonical SNAI1/ZEB1/TWIST1 dropped"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Chen 2020 NPC \u2014 analysis summary",gates,panels,dataset,verdict,params,
              run_label="run 4 of 7")
print("built")
