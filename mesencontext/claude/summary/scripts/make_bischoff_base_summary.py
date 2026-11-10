import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Lung/Bischoff2021_Lung"; F="/home/caleb/EMToolbox/figures/mesencontext/claude/Lung/Bischoff2021_Lung"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "10/19 samples (\u226543 cells) intermix on one continuous manifold with no per-patient islands; the kNN graph "
  "is a single connected component (13,382 cells, no island removal). Density is bimodal (a thin transitional "
  "waist) but topologically continuous \u2014 both poles are multi-patient (terminus: 7 samples >5%)."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Gast/pSom decline together along pseudotime (\u03c1=\u22120.60/\u22120.23); Crest is spatially anti-correlated "
  "(r=\u22120.40/\u22120.72) and rises to a terminal readout (\u03c1=+0.29; crest-high decile mean pt=0.73). The modules "
  "ride a dominant alveolar-differentiation axis \u2014 present but not resolved into two competing arms."),
 ("Gate 3 \u2014 cross-repression","NA",GREY,
  "Single monotone differentiation axis \u2014 no bifurcation and no Gast/pSom-overlap hub, so there is no branch "
  "pair to test for competitive cross-repression."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Lung adenocarcinoma (Bischoff et al., 2021), 10x \u2014 early-stage LUAD; malignant only: 13,439 loaded, "
 "13,382 across 10 samples on one continuous manifold; the full compartment carries the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Bischoff\u2019s manifold is a single "
 "alveolar-differentiation axis (alveolar/AT2 \u2192 dedifferentiated); embryonic modules ride it as a secondary "
 "Gast/pSom \u2192 terminal-Crest gradient, lacking Puram\u2019s hub-and-spoke, so Gate 3 has no hub to test. EMT-TFs "
 "FOXC1 (early/root, 33% det) \u2192 ZEB1 (late/terminus); canonical SNAI1/TWIST1 near the floor.")
params=[
 ("Min cells/sample","\u226543 (keeps 10/19; gap 127\u219215, \u00d78.5)"),
 ("Malignant states","Alv/AT2 4,173 / Secretory 1,761 / Dediff 7,448"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Integration","Harmony(sample) \u03b8=2; 50PC \u2192 12; UMAP spread=1.3"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100 (fold-free, 2 tips)"),
 ("Manifold","full malignant (no lobe split); 1 kNN component"),
 ("EMT-TFs","FOXC1 (early/root, 33% det) \u2192 ZEB1 (late/terminus); SNAI1/TWIST1 near floor"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Bischoff 2021 LUAD \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
