import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN
NB="/home/caleb/EMToolbox/mesencontext/claude/Skin/Ji2020_Skin-6"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Ji2020_Skin-6"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Cell-cycle regressed out (de-novo S/G2M scores), Harmony on sample (\u03b8=2), n_pcs=20. Embedding is "
  "sample-integrated (all 8 patients interleave; 30-NN cross-sample fraction 0.63 vs 0.78 max) and one "
  "continuous body (single radius-graph component). Without CC regression a spurious cycling axis dominates a "
  "lobe \u2014 the confound the prior linear read never removed."),
 ("Gate 2 \u2014 module geography","GO (branching)",GREEN,
  "Basal Gast/pSom hub diverges into a Gast-leaning differentiation arm (KRT1/10; Gast +0.00 vs hub \u22120.04) and "
  "a pSom-leaning TSK / leading-edge arm (pSom +0.06). Crest is a terminal readout enriched on the pSom (TSK) "
  "arm and depleted at the differentiation tip \u2014 uncoupled from the Gast/pSom axis (acceptable)."),
 ("Gate 3 \u2014 hub cross-repression","GO (branching)",GREEN,
  "On the basal hub (n=3,756), Gast-loading and pSom-loading genes anti-correlate: mutual r = \u22120.38 (Puram "
  "anchor \u22120.49; Filbin branching \u22120.34). Competitive cross-repression at the branch point."),
]
panels=[("Manifold \u2014 samples",F+"/samples.pdf"),("Trajectory / root",F+"/manifold.pdf"),
        ("Gastrulation",F+"/Gast_signature.pdf"),("Somitogenesis",F+"/pSom_signature.pdf"),
        ("Neural Crest",F+"/Crest_signature.pdf"),("EMT-TF expression",F+"/expression.pdf"),
        ("Gate 3: r = \u22120.38",F+"/modules.pdf")]
dataset=("Cutaneous SCC (Ji et al., 2020), 10x \u2014 10,523 malignant cells (8/10 patients). Geometry: BRANCHING "
 "(hub-and-spoke).")
verdict=("Pattern REPRODUCES (branching). A basal progenitor hub diverges into a keratinocyte-differentiation arm "
 "(Gast) and a TSK / leading-edge EMT arm (pSom) with hub cross-repression r = \u22120.38; Crest is a terminal "
 "readout on the pSom arm. Gate 1 GO / Gate 2 GO / Gate 3 GO \u2014 the third branching case in the atlas. EMT-TFs "
 "SNAI2 / PRRX2.")
params=[
 ("Threshold","keep samples \u2265103 (gap-finding 40\u2192268, ~6.7\u00d7) \u2192 8/10 patients, 10,598 \u2192 10,531 \u2192 10,523 (islands)"),
 ("Cell cycle","de-novo S/G2M scores regressed out of the over-dispersed matrix (clean-embedding step)"),
 ("Embedding","1,443 over-dispersed genes, PCA 50 \u2192 Harmony(sample, \u03b8=2), n_pcs=20, UMAP spread=1.3"),
 ("Trajectory","scFates PPT tree (Nodes=80, \u03bb=600, \u03c3=0.4) on X_umap; root = basal-max fork"),
 ("Hub","Basal progenitor cluster (branch-point / root convergence zone); subtypes by markers + Ji calls"),
 ("EMT-TFs","SNAI2 / PRRX2 (Gast/pSom arms)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Ji 2020 cutaneous SCC \u2014 analysis summary",gates,panels,dataset,verdict,params,
              branching=True, run_label="run 7 of 10")
print("built")
