import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN
NB="/home/caleb/EMToolbox/mesencontext/claude/Skin/Ji2020_Skin-4"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Ji2020_Skin-4"
gates=[
 ("Gate 1 \u2014 integration & continuity","GO",GREEN,
  "Harmony (\u03b8=5) merges 8 samples into one connected kNN component; continuous, no sample islands."),
 ("Gate 2 \u2014 module geography","GO (branching)",GREEN,
  "Gast/pSom-high hub diverges into a Gast-arm and a pSom-arm; Crest a terminal readout toward the tips."),
 ("Gate 3 \u2014 hub cross-repression","GO (branching)",GREEN,
  "Hub Gast\u2194pSom module r = \u22120.37 (perm p = 0.007), competitive; Puram \u22120.49 / Filbin \u22120.34 anchors."),
]
panels=[("Manifold \u2014 samples",F+"/samples.pdf"),("Trajectory / root",F+"/manifold.pdf"),
        ("Gastrulation",F+"/Gast_signature.pdf"),("Somitogenesis",F+"/pSom_signature.pdf"),
        ("Neural Crest",F+"/Crest_signature.pdf"),("EMT-TF expression",F+"/expression.pdf"),
        ("Gate 3: r = \u22120.37",F+"/modules.pdf")]
dataset=("Cutaneous SCC (Ji et al., 2020), 10x \u2014 10,531 malignant cells over 8 samples after thresholding (8 of "
 "10; clean 6.7\u00d7 per-sample count gap, keep \u2265100). Developmental compartment 6,800 cells (3,731 cycling "
 "scoped out).")
verdict=("The embryonic pattern reproduces as a BRANCHING hub-and-spoke \u2014 a Gast/pSom-high hub diverging into "
 "competing Gast and pSom arms with hub cross-repression r = \u22120.37, the Puram signature on squamous biology. "
 "Gate 1 GO / Gate 2 GO / Gate 3 GO. EMT-TFs SNAI2 (50%, late/terminal) + PRRX2 (9%, root-end).")
params=[
 ("Min-cell threshold","\u2265100 per sample (6.7\u00d7 count gap 40\u2192268); drops P3, P5"),
 ("Overdispersed genes","1,443 (scFates find_overdispersed)"),
 ("Embedding","PCA 50 \u2192 Harmony(sample, \u03b8=5) \u2192 kNN n_pcs=20 (scree elbow PC17), UMAP spread=1.3"),
 ("Trajectory / geometry","scFates PPT tree (branching), Nodes=50 \u03bb=2000 \u03c3=0.5; dev compartment, fold-free"),
 ("Root (hub)","Gast/pSom-high, Crest-low convergence node (Crest late = terminal)"),
 ("Hub identity","Hub milestone, 1,195 cells; module mutual r = \u22120.37 (p=0.007)"),
 ("Crest arm","terminal readout toward arm tips (\u03c1_pt = +0.25); not on the cross-repression axis"),
 ("EMT-TFs","SNAI2 (50%, late/terminal) + PRRX2 (9%, root-end); SNAI1/ZEB1 near 10x floor"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Ji 2020 cutaneous SCC \u2014 analysis summary",gates,panels,dataset,verdict,params,
              branching=True, run_label="run 5 of 10")
print("built")
