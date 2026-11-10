import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN
NB="/home/caleb/EMToolbox/mesencontext/claude/Skin/Ji2020_Skin-2"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Ji2020_Skin-2"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "\u03b8=10 integrates 8 patients into one connected manifold; no per-sample islands."),
 ("Gate 2 \u2014 module geography","GO (branching)",GREEN,
  "Gast/pSom hub diverges into opposed Gast & pSom arms; Crest terminal on the pSom arm. A branching "
  "hub-and-spoke wishbone rooted at the Gast/pSom-high tip."),
 ("Gate 3 \u2014 hub cross-repression","GO (branching)",GREEN,
  "Mixed-hub Gast\u2194pSom mutual r = \u22120.47 (Puram \u22120.49); null 0.01\u00b10.09, p<0.003."),
]
panels=[("Manifold \u2014 samples",F+"/samples.pdf"),("Trajectory / root",F+"/manifold.pdf"),
        ("Gastrulation",F+"/Gast_signature.pdf"),("Somitogenesis",F+"/pSom_signature.pdf"),
        ("Neural Crest",F+"/Crest_signature.pdf"),("EMT-TF expression",F+"/expression.pdf"),
        ("Gate 3: r = \u22120.47",F+"/modules.pdf")]
dataset=("Cutaneous squamous cell carcinoma (Ji et al., 2020), 10x \u2014 8/10 patients retained; 7,085 malignant "
 "developmental cells (10,531 pre-scope).")
verdict=("Embryonic branching pattern REPRODUCES \u2014 Gast/pSom hub, two cross-repressing arms, Crest terminal on "
 "the pSom arm (r=\u22120.47 vs Puram \u22120.49). Gate 1 GO / Gate 2 GO / Gate 3 GO. A Gast/pSom hub diverges into "
 "opposed Gast and pSom arms with the neural-crest terminus on the pSom arm; EMT-TFs PRRX2 (Gast arm) / SNAI2 "
 "(pSom arm terminus).")
params=[
 ("Threshold","100 cells/sample (clean 6.70\u00d7 count gap 40\u2192268); keeps 8/10 patients (10,531 cells)"),
 ("Genes","1,443 overdispersed (scFates); PCA 50 PC"),
 ("Integration","Harmony \u03b8=10 (10x precedent); branch survives strong integration"),
 ("Cycling scope","3,446 cells in 5 high-cycling (>50%) Leiden lobes removed \u2192 7,085-cell fork re-embedded (Filbin)"),
 ("Embedding","kNN n_pcs=20 / n_neighbors=30; UMAP spread=1.3"),
 ("Trajectory","scFates PPT tree Nodes=60 \u03bb=3000 \u03c3=0.5; 4 tips / 2 forks (hub-and-spoke Y)"),
 ("Hub","fork-Leiden(res 0.4) max joint Gast+pSom = 'Mixed' (1,513 cells)"),
 ("Root","Gast/pSom-high, Crest-low tip (root_score 0.99)"),
 ("EMT-TFs","PRRX2 (Gast arm) / SNAI2 (pSom arm terminus)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Ji 2020 cutaneous SCC \u2014 analysis summary",gates,panels,dataset,verdict,params,
              branching=True, run_label="run 3 of 10")
print("built")
