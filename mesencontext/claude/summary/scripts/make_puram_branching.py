import sys, os
sys.path.insert(0, "/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Head-and-Neck/Puram2017_Head-and-Neck"; out="/home/caleb/EMToolbox/mesencontext/claude/Head-and-Neck/Puram2017_Head-and-Neck/summary.pdf"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "10/17 samples (\u2265100 cells) intermix on one continuous manifold; no per-patient islands (64 detached cells removed)."),
 ("Gate 2 \u2014 module geography","GO",GREEN,
  "Gast/pSom hub diverges into arms; Crest is a terminal readout at the Basal tip (0.43 > Atypical 0.27 \u2248 Classical 0.24)."),
 ("Gate 3 \u2014 hub mutual exclusivity","GO",GREEN,
  "On 466 Mixed-hub cells, per-gene Gast vs pSom correlation vectors anti-correlate: r = \u22120.47 (ref \u2248 \u22120.49)."),
]
panels=[("Gate 1: integration",F+"/samples.pdf"),("Trajectory / root",F+"/manifold.pdf"),
        ("Gast",F+"/Gast_signature.pdf"),("pSom",F+"/pSom_signature.pdf"),
        ("Crest",F+"/Crest_signature.pdf"),("EMT-TFs",F+"/expression.pdf"),
        ("Gate 3: r = \u22120.47",F+"/modules.pdf")]
dataset=("Head & Neck SCC (Puram et al., 2017), SmartSeq2 \u2014 18 patients / 5,902 cells (master scope); malignant only: 2,539 load, 2,408 across 4 subtypes enter the trajectory.")
verdict=("\u2713 Pattern reproduces \u2014 all three gates pass. Gast/pSom mutually exclusive within the Mixed hub (r = \u22120.47 vs ref \u22120.49), hub at the root of a hub-and-spoke manifold; EMT-TFs ZEB1 (Classical) / PRRX1 (Atypical).")
params=[("Min cells/sample","\u2265 100 (keeps 10/17)"),("Integration","Harmony on sample, 20 it"),
        ("Island removal","UMAP radius-graph (\u221264 cells)"),("Trajectory","scFates PPT N=200 \u03bb=2000 \u03c3=0.5"),
        ("Root node","85 = Mixed hub (466 cells)"),("Subtypes","markers + Puram 2017"),
        ("EMT-TFs shown","ZEB1 (Classical) / PRRX1 (Atypical)"),("Reference r","\u22120.49 (embryonic anchor)")]
build_summary(out,"Puram 2017 HNSCC \u2014 recapitulation summary",gates,panels,dataset,verdict,params,branching=True)
print("built",out)
