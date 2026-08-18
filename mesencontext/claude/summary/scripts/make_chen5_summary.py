import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Head-and-Neck/Chen2020_Head-and-Neck-5"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Head-and-Neck/Chen2020_Head-and-Neck-5"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "8/14 samples (\u2265107 malignant cells; multiplicative count gap 107\u219236) intermix on one continuous manifold "
  "\u2014 mean iLISI 2.16 (\u224850% of neighbourhoods cross the >2 threshold), a single connected component; the "
  "39-cell detached speck was removed. No per-patient islands."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast & pSom do not resolve into two competing arms \u2014 both localise at the origin (high-decile mean pseudotime "
  "0.22 each; Gast~pSom r=+0.00, no cross-repression). Crest is the inverse/terminal gradient (r=\u22120.78 vs Gast; "
  "high-decile pt 0.97; along pseudotime Gast \u03c1=\u22120.79, Crest \u03c1=+0.82). Non-branching."),
 ("Gate 3 — hub mutual exclusivity","NA",GREY,
  "Single monotone Gast/pSom \u2192 Crest axis \u2014 no bifurcation and no Gast/pSom-overlap hub, so there is no branch "
  "pair to test for competitive cross-repression (branching-only gate; \u00a72)."),
]
panels=[("Gate 1: integration",os.path.join(F,"samples.pdf")),
        ("Trajectory / root",os.path.join(F,"manifold.pdf")),
        ("Gast",os.path.join(F,"Gast_signature.pdf")),
        ("pSom",os.path.join(F,"pSom_signature.pdf")),
        ("Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TFs",os.path.join(F,"expression.pdf"))]
dataset=("Nasopharyngeal carcinoma (Chen et al., 2020), 10x \u2014 71,896 cells / 14 samples (3,763 malignant). "
 "Malignant only: 3,674 pass the \u2265107-cell sample threshold; 3,635 (8 samples) enter the trajectory after the "
 "39-cell detached speck is removed.")
verdict=("\u2713 Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO (non-branching), Gate 3 NA. The NPC malignant "
 "manifold is a single monotone Gast/pSom \u2192 terminal-Crest gradient matching the developmental axis; it lacks "
 "Puram's hub-and-spoke bifurcation, so Gate 3 has no hub to test. EMT-TFs FOXC1 (early/root) \u2192 PRRX1 "
 "(late/terminus); prototypical SNAI1/TWIST1 fall below the 3% detection floor and the panel is weakly organised (|\u03c1|<0.18).")
params=[("Min cells/sample","\u2265107 (keeps 8/14; gap 107\u219236)"),
 ("Integration","Harmony(sample) \u03b8=5; PCA 20PC"),
 ("Island removal","radius-graph (\u221239 detached speck)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Geometry","non-branching curve (roundish, aspect 1.4)"),
 ("Subtypes","markers + Chen 2020 (3CA mp_top)"),
 ("EMT-TFs","FOXC1 (early) \u2192 PRRX1 (late)")]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Chen 2020 NPC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
