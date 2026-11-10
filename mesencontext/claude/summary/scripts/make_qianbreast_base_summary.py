import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY, RED
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Qian2020_Breast"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Qian2020_Breast"
gates=[
 ("Gate 1 \u2014 mixing & continuity","NO-GO",RED,
  "Malignant cells form a per-patient archipelago. A single connected kNN graph appears only at the most generous "
  "integration (\u03b8=10), where iLISI is just 1.1 of 7 samples \u2014 the scalar a na\u00efve test reads as "
  "\u2018integrated\u2019 yet the embedding is organised BY PATIENT: 6/7 patients self-cluster far above chance "
  "(self-neighbour enrichment 6.8\u201323.5\u00d7, all past the 2.5\u00d7 line). \u03b8=5 splits the manifold into two "
  "disconnected components, one PURE sample 54 (the dominant 65% tumour). Integration does not fix it \u2014 "
  "enrichment GROWS with \u03b8 and is PC-count-invariant (22\u00d7 at n_pcs 20/30/40), so Harmony over-corrects. "
  "Every patient carries the SAME embryonic modules \u2014 inter-patient CNV/clonal heterogeneity, not a shared "
  "cell-state continuum \u2014 do not force a trajectory."),
 ("Gate 2 \u2014 module geography","NA",GREY,
  "Not reached. Gate 2 tests a Gast/pSom hub and Crest geography on a fitted manifold; with Gate 1 NO-GO no "
  "manifold/trajectory is fit, so this gate does not apply."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not reached (branching-only, downstream of Gate 2). No hub, no bifurcation, no hub r."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (Qian et al., 2020), 10x (UMI counts) \u2014 4,818 malignant cells across 7 samples = "
 "7 patients. Gate 1 NO-GO: per-patient archipelago, no integrated continuum.")
verdict=("The embryonic-program pattern does NOT reproduce in Qian 2020 breast cancer: the malignant compartment "
 "is a per-patient archipelago \u2014 no sample-integrated, continuous cell-state manifold. One patient (sample 54, "
 "65% of cells) even forms a fully disconnected component at moderate integration. Gate 1 NO-GO \u2014 analysis "
 "stops before the trajectory (Gates 2 & 3 N/A). EMT-TFs SNAI2 and FOXC1 are the broadest detectable factors, "
 "reported over the un-integrated manifold.")
params=[
 ("Sample threshold","\u2265100 floor; argmax gap 3111\u2192518 (6.01\u00d7) = dominant tumour, not a tail; keeps 7/7"),
 ("Gene / PCA","1,225 overdispersed genes; n_pcs=20 (PC1 21% var, inter-patient/CNV axis)"),
 ("Integration","Harmony on sample, swept \u03b8 2/5/10/20/40; \u03b8=10 first single component (diagnostic)"),
 ("Root / geometry","none \u2014 no trajectory (Gate 1 NO-GO); per-patient archipelago"),
 ("EMT-TFs shown","SNAI2 (11.3%) \u00b7 FOXC1 (10.4%), overlaid without pseudotime"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Qian 2020 Breast \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
