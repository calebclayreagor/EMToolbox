import sys, os
sys.path.insert(0, "/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Filbin2018_Brain-9"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "All 6 SmartSeq2 samples intermix on one connected kNN component (no per-patient archipelago); a coherent cycling lobe (261 cells) is scoped out so the fork resolves."),
 ("Gate 2 \u2014 module geography","GO (branching)",GREEN,
  "Gast/pSom co-express at the Mixed hub and diverge into two arms; Crest peaks at the OC-arm tip (terminal readout). Branching module pattern present."),
 ("Gate 3 \u2014 cross-repression","GO",GREEN,
  "Mixed hub (n=761) per-gene Gast\u2194pSom r = \u22120.34 (anchor Puram \u22120.49); permutation null +0.00 \u00b1 0.09, p<0.001 \u2192 real competitive cross-repression, not a collider artifact."),
]
panels=[("Manifold \u2014 samples",F+"/samples.pdf"),("Trajectory / root",F+"/manifold.pdf"),
        ("Gastrulation",F+"/Gast_signature.pdf"),("Somitogenesis",F+"/pSom_signature.pdf"),
        ("Neural Crest",F+"/Crest_signature.pdf"),("EMT-TF expression",F+"/expression.pdf"),
        ("Gate 3: r = \u22120.34",F+"/modules.pdf")]
dataset=("Pediatric H3-K27M diffuse midline glioma (Filbin et al., 2018), SmartSeq2 (TPM) \u2014 2,259 malignant cells, 6 samples; 1,998 in the developmental fork. Branching (hub-and-spoke).")
verdict=("Branching \u2014 the embryonic pattern reproduces: a Gast/pSom Mixed hub diverges into AC-like and OC-like arms with cross-repression (r=\u22120.34); Crest is a terminal readout at the OC tip. All three gates GO. EMT-TFs PRRX1 / ZEB1 (with ZEB2).")
params=[("Min-cell threshold","\u2265100 (no clean count gap; keeps all 6)"),("Integration","Harmony on sample, \u03b8=10"),
        ("Embedding","PCA50 \u2192 n_pcs=20, k=30, UMAP spread=1.3"),("Overdispersed genes","3,779"),
        ("Cycling lobe removed","Leiden clusters (>50% cyc), 261 cells"),("Trajectory","scFates PPT tree (Nodes=40, \u03bb=3000)"),
        ("Root","Gast/pSom-high, Crest-low tip (non-Crest, not the fork)"),("Hub / EMT-TFs","Mixed convergence cluster (n=761); PRRX1 / ZEB1 / ZEB2")]
build_summary(os.path.join("/home/caleb/EMToolbox/mesencontext/claude/Brain/Filbin2018_Brain-9","summary.pdf"),"Filbin 2018 pediatric H3-K27M glioma \u2014 analysis summary",gates,panels,dataset,verdict,params,branching=True)
print("built filbin")
