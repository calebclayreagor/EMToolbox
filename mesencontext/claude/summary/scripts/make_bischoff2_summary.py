import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Lung/Bischoff2021_Lung-2"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Lung/Bischoff2021_Lung-2"
gates=[
 ("Gate 1 — integration & continuity","GO",GREEN,
  "Malignant structure is mixed and continuous on one manifold. Judged on the embedding + mixing metrics across an "
  "n_pcs\u00d7\u03b8 sweep: \u03b8=0 gives per-sample islands (iLISI 1.05, diff-sample kNN 0.02) \u2014 integration mixes them "
  "strongly, saturating by \u03b8=2 (iLISI ~3.3\u20133.7 across \u03b8=2/5/10). At the chosen \u03b8=10 (K\u00fcrten precedent) the kNN "
  "graph is a single connected component (comp=1, as at every \u03b8) and strongly mixed (iLISI 3.53, diff-sample kNN 0.43 "
  "of 0.805 ceiling). The two density lobes are poles of one connected manifold \u2014 not disconnected islands (comp=1 "
  "throughout) and not sample-driven (both multi-sample); the thin transitional waist is expected differentiation "
  "density, not a break. Cell cycle does not structure the manifold (\u22646% cycling per lobe) \u2014 no compartment to strip."),
 ("Gate 2 — embryonic module pattern","GO (non-branching, flagged)",GREEN,
  "Non-branching case (\u00a71): Crest is a clean inverse/terminal gradient \u2014 anti-correlates Gast (\u22120.42) and pSom "
  "(\u22120.50), and the Gast&pSom co-high hub is strongly Crest-low (z \u22120.82 vs +0.20). Flag (pass anyway): pSom is "
  "near-ubiquitous (score>0 in 94% of cells), Gast sparse (14%), Gast/pSom co-variation weak (\u22120.15) \u2014 an attenuated "
  "signal versus the K\u00fcrten precedent. The axis is alveolar-differentiation \u2194 EMT."),
 ("Gate 3 — bifurcation cross-repression","NA",GREY,
  "No bifurcation. The curve is fold-free (2 tips, 0 forks, self-approach 2.9); the PPT tree's forks separate no biology "
  "(all tips Gast\u2248\u22120.035 / pSom\u2248+0.06 / Crest\u2248\u22120.035). Branching-only gate \u2192 NA."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime + curve",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Lung adenocarcinoma (Bischoff et al. 2021), 10x scRNA-seq. 13,382 malignant cells across 10 tumor samples "
 "(of 20; normal-tissue samples carry 2\u201315 malignant cells and drop out at threshold).")
verdict=("The embryonic pattern reproduces in the non-branching form \u2014 a single continuous alveolar\u2192EMT manifold with "
 "Crest as an inverse terminal gradient and no Gast/pSom bifurcation. The signal is weaker than the K\u00fcrten HNSCC "
 "precedent (attenuated; flagged), but present and continuous.")
params=[
 ("Min-cell threshold","43 (geo-mean across the 127\u219215 gap, ratio 8.5) \u2192 10 samples, 13,382 cells"),
 ("Islands removed","0 (no detached components at n_neighbors=30) \u2192 13,382 on the manifold"),
 ("Overdispersed genes","1,976 (no pre-PCA scaling)"),
 ("Integration / embedding","Harmony on sample \u03b8=10; n_pcs=20, n_neighbors=30, UMAP spread=1.3 (seed 1)"),
 ("Geometry","2-D continuum (UMAP aspect \u22481.3); scFates curve (non-branching)"),
 ("Root","Alveolar / Crest-low tip (Gast/pSom-high pole; Crest is developmentally late)"),
 ("EMT-TFs shown","FOXC1, TCF12, TCF3, SNAI1, PRRX1/2, ZEB1/2, TCF4 (\u22653% detected; VIM/TGFBI not TFs)"),
 ("Gast\u2013pSom r (whole manifold)","\u22120.15 raw \u2014 attenuated vs Puram hub ref \u2248 \u22120.49 (no windowed hub step; Gate 3 NA)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Bischoff 2021 LUAD \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
