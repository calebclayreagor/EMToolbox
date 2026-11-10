import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN
NB="/home/caleb/EMToolbox/mesencontext/claude/Skin/Ji2020_Skin-7"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Ji2020_Skin-7"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Malignant cells from 8/10 samples (\u2265100 cells) form one continuous, sample-mixed manifold (iLISI\u22484.0; "
  "single kNN component; 13 detached cells removed). Cell-cycle regression was required \u2014 it is the largest "
  "program and otherwise dominates the embedding."),
 ("Gate 2 \u2014 module geography","GO (branching)",GREEN,
  "The embryonic modules resolve into a branching wishbone: a Gast/pSom co-expression hub diverges into a "
  "Gast-leaning (Basal) arm and a pSom-leaning (Differentiated) arm. Crest is a terminal readout at the tips, "
  "uncoupled from Gast/pSom."),
 ("Gate 3 \u2014 hub cross-repression","GO (branching)",GREEN,
  "Within the 4,888-cell Mixed hub, per-gene Gast and pSom loadings mutually anti-correlate: r = \u22120.54 (Puram "
  "anchor \u2248 \u22120.49) \u2014 competitive cross-repression, the bifurcation signature."),
]
panels=[("Manifold \u2014 samples",F+"/samples.pdf"),("Trajectory / root",F+"/manifold.pdf"),
        ("Gastrulation",F+"/Gast_signature.pdf"),("Somitogenesis",F+"/pSom_signature.pdf"),
        ("Neural Crest",F+"/Crest_signature.pdf"),("EMT-TF expression",F+"/expression.pdf"),
        ("Gate 3: r = \u22120.54",F+"/modules.pdf")]
dataset=("Cutaneous SCC (Ji et al., 2020), 10x \u2014 10 patients, 48,164 cells; 10,598 malignant \u2192 10,518 after QC. "
 "Subtypes Mixed / Basal / Differentiated / TSK.")
verdict=("Pattern reproduces \u2014 all three gates GO. Branching wishbone rooted at the Gast/pSom hub; competitive "
 "Gast\u2194pSom cross-repression (r=\u22120.54); Crest terminal, uncoupled. Gate 1 GO / Gate 2 GO / Gate 3 GO. EMT-TFs "
 "SOX9 (hub/basal), SNAI2 (Differentiated arm).")
params=[
 ("Min cells/sample","\u2265100 (gap 40\u2192268, 6.7\u00d7; keeps 8/10, drops P3, P5)"),
 ("Cell-cycle regression","S + G2M scores regressed \u2014 KEY to a clean manifold"),
 ("Island removal","UMAP radius-graph, largest component (\u221213 cells)"),
 ("Integration","Harmony on sample, \u03b8 = 2, 20 it; n_pcs = 20"),
 ("Embedding","UMAP min_dist = 0.4, spread = 1.0"),
 ("Trajectory","scFates PPT tree, Nodes = 60, \u03bb = 2000, \u03c3 = 1.5"),
 ("Geometry / root","Branching (3-tip wishbone); root = Mixed hub (node 16, a tip)"),
 ("Hub / Gate-3 r","Mixed (4,888 cells); r = \u22120.54"),
 ("EMT-TFs","SOX9 (hub/basal), SNAI2 (Differentiated arm) \u2014 Snail/Zeb/Twist ~absent"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Ji 2020 cutaneous SCC \u2014 analysis summary",gates,panels,dataset,verdict,params,
              branching=True, run_label="run 8 of 10")
print("built")
