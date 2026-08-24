import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/EMToolbox/mesencontext/claude/Neuroendocrine/Kildisiute2021_Neuroendocrine-1"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Neuroendocrine/Kildisiute2021_Neuroendocrine-1"
gates=[
 ("Gate 1 — mixing & continuity","NO-GO",RED,
  "Malignant cells form a per-platform / per-patient archipelago. At the best-mixing integration (\u03b8=10) the kNN "
  "graph is a single component \u2014 the scalar a na\u00efve test reads as \u201cintegrated\u201d \u2014 yet the embedding is organised BY "
  "SAMPLE: platforms NEVER share a neighbourhood (iLISI(technology)=1.00/2, pinned across the entire \u03b8 sweep 2\u201350), "
  "and at low \u03b8 the manifold is two disconnected blobs split cleanly by platform. The platform batch is perfectly "
  "confounded with patient (each patient on one platform only), so Harmony-on-sample has no anchor. Even within one "
  "platform the two patients barely mix (iLISI \u22481.8/2) \u2014 inter-patient / inter-platform (technical + CNV/clonal) "
  "heterogeneity, not a shared cell-state continuum."),
 ("Gate 2 — module geography","N/A",GREY,
  "Not reached. Gate 2 tests a Gast/pSom hub and Crest geography on a fitted manifold; with Gate 1 NO-GO no "
  "manifold / trajectory is fit, so the module-geography gate does not apply."),
 ("Gate 3 — cross-repression","N/A",GREY,
  "Not reached (branching-only, and downstream of Gate 2). No hub, no bifurcation, no hub r."),
]
panels=[("Malignant manifold — samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Neuroblastoma (Kildisiute et al., 2021), Neuroendocrine \u2014 10X (UMI) + CEL-seq2 (TPM) merged (inner join, "
 "32,118 shared genes). \u2265166-cell threshold keeps 4/14 samples (2,632 cells); a sparse 10-sample tail is dropped.")
verdict=("The embryonic-program pattern does NOT reproduce in Kildisiute 2021 neuroblastoma: the malignant compartment "
 "is a per-platform / per-patient archipelago with no sample-integrated, continuous cell-state manifold. Gate 1 "
 "NO-GO \u2014 analysis stops before the trajectory. ZEB2 / ZEB1 are the broadly-expressed EMT-TFs, reported "
 "unconditionally.")
params=[
 ("Data merge","10X UMI + CEL-seq2 TPM, inner join (32,118 genes)"),
 ("Sample threshold","\u2265166 cells (gap 412\u219267, 6.15\u00d7); keeps 4/14 (2,632 cells)"),
 ("Gene / PCA","1,513 overdispersed; n_pcs=20 (PC1 \u224857% variance = CNV axis)"),
 ("Integration","Harmony on sample, \u03b8 2/5/10/20/50; \u03b8=10 best; iLISI(tech)=1.00/2 throughout"),
 ("Root / geometry","None \u2014 no trajectory fit (Gate 1 NO-GO)"),
 ("EMT-TFs shown","ZEB2 (45.2%) \u00b7 ZEB1 (44.4%); FOXC/PRRX added, VIM excluded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Kildisiute 2021 neuroblastoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
