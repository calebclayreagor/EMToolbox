import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/EMToolbox/mesencontext/claude/Brain/Choudhury2022_Brain"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Choudhury2022_Brain"
gates=[
 ("Gate 1 — mixing & continuity","NO-GO",RED,
  "Malignant cells form a per-patient archipelago. At the best-mixing integration (\u03b8=10) the kNN graph is a single "
  "component (iLISI 1.0\u21923.0) \u2014 the scalars a na\u00efve test reads as \u201cintegrated\u201d \u2014 yet the embedding is organised "
  "BY PATIENT: every patient self-clusters locally (self-neighbour enrichment 1.8\u20137.2\u00d7); 3/5 patients cross the "
  "2.5\u00d7 line (1/3/4 at 7.2/3.4/2.8\u00d7) and the two largest (5,6) hold their own territories. Integration strength "
  "does not fix it \u2014 the enrichment GROWS with \u03b8 (patient 1: 7.2\u219211.9\u219212.9\u00d7), so Harmony over-corrects. Each "
  "patient carries the same embryonic modules \u2192 inter-patient CNV/clonal heterogeneity (expected for meningioma), "
  "not a shared cell-state continuum \u2192 do not force a trajectory."),
 ("Gate 2 — module geography","N/A",GREY,
  "Not reached. Gate 2 tests a Gast/pSom hub and Crest geography on a fitted manifold; with Gate 1 NO-GO no "
  "manifold/trajectory is fit, so the module-geography gate does not apply."),
 ("Gate 3 — cross-repression","N/A",GREY,
  "Not reached (branching-only, and downstream of Gate 2). No hub, no bifurcation, no hub r."),
]
panels=[("Malignant manifold — samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Meningioma (Choudhury et al., 2022), 10x (UMI counts) \u2014 37,049 malignant cells; 7/10 samples, 5 patients "
 "enter preprocessing. First meningioma / first non-glial brain tumour in the atlas.")
verdict=("The embryonic-program pattern does NOT reproduce in Choudhury 2022 meningioma: the malignant compartment is a "
 "per-patient archipelago with no sample-integrated, continuous cell-state manifold. Gate 1 NO-GO \u2014 analysis stops "
 "before the trajectory. A genuine portability NO-GO (integration failure), distinct from a pattern-absent Gate-2 "
 "NO-GO. The FOXC mesenchymal TF family is broadly expressed (arachnoid/mesenchymal identity), reported "
 "unconditionally without pseudotime.")
params=[
 ("Sample threshold","\u2265780 cells (geo-mean across the 2254\u2192270 gap, 8.35\u00d7); keeps 7/10 samples (5 patients)"),
 ("Gene / PCA","2,828 overdispersed (scFates GAM); n_pcs=20 (PC1 alone \u224825% variance, inter-patient/CNV axis)"),
 ("Integration","Harmony on sample, \u03b8 swept 10/20/40; \u03b8=10 best mixing (iLISI 3.0) \u2014 diagnostic, not corrective"),
 ("Root / geometry","None \u2014 no trajectory fit (Gate 1 NO-GO); geometry not applicable"),
 ("EMT-TFs shown","FOXC2 (68%) \u00b7 FOXC1 (67%) \u2014 broadest detectable (FOXC/PRRX panel; VIM excluded, not a TF)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Choudhury 2022 meningioma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
