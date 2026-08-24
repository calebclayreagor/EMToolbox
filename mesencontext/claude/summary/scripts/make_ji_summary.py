import sys, os
sys.path.insert(0, "/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Ji2020_Skin-9"; out="/home/caleb/EMToolbox/mesencontext/claude/Skin/Ji2020_Skin-9/summary.pdf"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "8/10 samples form one continuous, sample-mixed manifold (iLISI\u22484.0; single kNN component; 13 detached cells removed). Cell-cycle regression required."),
 ("Gate 2 \u2014 module geography","GO (branching)",GREEN,
  "A branching wishbone: three lobes (Basal, Differentiated, Mixed) meet at one convergence with a smooth monotone pseudotime (r\u22480.96). Rooted at the Basal tip (COL17A1\u207a/TP63\u207a progenitor)."),
 ("Gate 3 \u2014 cross-repression","GO",GREEN,
  "On the Basal root population (3,524 cells), Gast\u2194pSom gene loadings mutually anti-correlate: r = \u22120.41 (permutation p\u22480.0005) \u2014 within range of branching anchors (Puram \u22120.49, Filbin \u22120.34)."),
]
# branching: 6 strips + square modules LAST; correlation omitted from embed
panels=[("Manifold \u2014 samples",F+"/samples.pdf"),("Trajectory / root",F+"/manifold.pdf"),
        ("Gastrulation",F+"/Gast_signature.pdf"),("Somitogenesis",F+"/pSom_signature.pdf"),
        ("Neural Crest",F+"/Crest_signature.pdf"),("EMT-TF expression",F+"/expression.pdf"),
        ("Gate 3: r = \u22120.41",F+"/modules.pdf")]
dataset=("Cutaneous SCC (Ji et al., 2020), 10x \u2014 10 patients, 48,164 cells; 10,598 malignant \u2192 10,518 after QC. Subtypes Mixed / Basal / Differentiated / TSK. Branching (hub-and-spoke wishbone).")
verdict=("Branching \u2014 clean 3-tip wishbone rooted at the Basal progenitor tip, competitive Gast\u2194pSom cross-repression (r=\u22120.41, p\u22480.0005) at the Basal root; Crest terminal. All three gates GO. EMT-TFs SOX9 / SNAI2.")
params=[("Min-cell threshold","\u2265100 (gap 40\u2192268; keeps 8/10)"),("Cell-cycle regression","S + G2M regressed \u2014 key to clean manifold"),
        ("Integration","Harmony on sample, \u03b8=2; n_pcs=20"),("Embedding","UMAP min_dist=0.4, spread=1.0"),
        ("Trajectory","scFates PPT N=40, \u03bb=700, \u03c3=0.8 (3-tip wishbone)"),("Root","Basal tip (COL17A1\u207a/TP63\u207a progenitor)"),
        ("Gate-3 pop / r","Basal root (3,524 cells); r=\u22120.41, p\u22480.0005"),("EMT-TFs shown","SOX9 (basal) / SNAI2 (Differentiated arm)")]
build_summary(out,"Ji 2020 cutaneous SCC \u2014 analysis summary",gates,panels,dataset,verdict,params,branching=True)
print("built",out)
