import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Head-and-Neck/Chen2020_Head-and-Neck-4"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Head-and-Neck/Chen2020_Head-and-Neck-4"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Harmony on sample (\u03b8=4, n_pcs=19): iLISI 1.08 \u2192 2.33 of a 3.23 ceiling (72%; ceiling <8 because P11+P01=72% "
  "of cells). Single connected kNN component over all 3,674 cells \u2014 continuous, sample-integrated. No patient "
  "islands."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Gast/pSom overlap, Crest inverse terminal gradient. Per-node-cluster corr: Gast~pSom = +0.13 (OVERLAP, not "
  "cross-repression); Gast~Crest = \u22120.82; pSom~Crest = \u22120.50. Curve pseudotime: corr(t,Gast)=\u22120.58, "
  "corr(t,pSom)=\u22120.11, corr(t,Crest)=+0.44 \u2014 a single Gast/pSom-high \u2192 Crest-high axis. Cycling confound "
  "cleared (K\u00fcrten lesson): Gast~G2M = \u22120.49, progenitor is quiescent."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "No bifurcation; branching-only correlation / modules notebooks not produced (spec \u00a76)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Nasopharyngeal carcinoma (Chen et al., 2020), 10x \u2014 14 samples; 3,674 malignant cells retained "
 "(of 3,763; 8 samples \u2265107 cells).")
verdict=("The embryonic pattern reproduces as the NON-BRANCHING case: a single developmental axis from a "
 "Gast/pSom-high progenitor to a Crest-high terminus (structurally the K\u00fcrten 2021 outcome, not Puram\u2019s "
 "branched hub-and-spoke). Gate 1 GO / Gate 2 GO / Gate 3 NA. Detectable EMT-TFs FOXC1, SNAI2, PRRX1, ZEB2 "
 "(canonical SNAI1/ZEB1/TWIST below detection).")
params=[
 ("Min-cell threshold","107 (count-gap rule, 8/14 samples)"),
 ("Scaling","no sc.pp.scale (log1p, reference-matched)"),
 ("Genes","1,290 overdispersed"),
 ("Embedding","PCA n_pcs=19; Harmony \u03b8=4"),
 ("Trajectory","scFates curve Nodes=10; root = Gast/pSom-high tip"),
 ("Signatures","score_genes, union control pool"),
 ("EMT-TFs","FOXC1 / SNAI2 / PRRX1 / ZEB2 (canonical SNAI1/ZEB1/TWIST below floor)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Chen 2020 NPC \u2014 analysis summary",gates,panels,dataset,verdict,params,
              run_label="run 5 of 7")
print("built")
