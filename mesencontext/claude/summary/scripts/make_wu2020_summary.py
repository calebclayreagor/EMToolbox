import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Hematologic/Wu2020_Hematologic-3"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Wu2020_Hematologic-3"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "One connected kNN component at every \u03b8 (2/10/20); 488 cells (0.5%) in tiny detached specks, removed. Harmony \u03b8=10 "
  "minimises residual same-sample enrichment (2.7\u00d7; \u03b8=20 re-segregates). iLISI 9.5/36 (26% of ceiling). Decisive: "
  "between-sample R\u00b2 of the embedding = 0.01 \u2014 patient identity explains ~1% of manifold structure, so this is an "
  "integrated continuum, NOT a per-patient clonal archipelago (cf. Liu2021 MM)."),
 ("Gate 2 — module geography","NO-GO",RED,
  "Embryonic module pattern ABSENT. Smoothed signature geography is featureless (score std ~0.007; no Gast/pSom poles, "
  "no Crest gradient); module means ~0 (Gast +0.002, pSom +0.007, Crest \u22120.004). Gast and pSom ANTI-correlate "
  "(smoothed r=\u22120.37) instead of overlapping as the non-branching case requires. No developmental axis: modules "
  "unaligned with any diffusion component (|r|\u22640.14), flat along pseudotime, and the Crest \"terminal\" position FLIPS "
  "with the root choice (0.59 vs 0.41) \u2014 a rooting artifact, not biology."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable \u2014 no bifurcation (Gate 2 NO-GO). Branching-only 04_correlation / 05_modules not produced."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Bone-marrow acute myeloid leukemia (Wu et al., 2020), Microwell-seq \u2014 96,413 malignant blasts across 36 "
 "samples. A trajectory is fit, but the embryonic module pattern is absent (Gate 2 NO-GO; pattern-absent).")
verdict=("The embryonic developmental pattern does NOT reproduce \u2014 malignant AML blasts form an integrated, continuous "
 "manifold with no Gast/pSom hub, no arms, and no terminal Crest gradient (Gate 2 NO-GO). Geometry: none "
 "(pattern absent). Corrects three prior attempts that read a union-control-pool scoring artifact off an arbitrary "
 "root on a featureless blob. Gate 1 GO (integrated continuum, between-sample R\u00b2=0.01), Gate 3 NA.")
params=[
 ("Min-cell threshold","\u2265100 (clean gap 98\u2192417, 4.26\u00d7) \u2192 36/38 samples, 96,901 cells"),
 ("Integration","Harmony \u03b8=10 (residual-enrichment min); n_pcs=20, k=30, spread=1.3; 443 HVG"),
 ("Island removal","radius-graph 6\u00d7 median, keep largest \u2192 488 removed, 96,413 final"),
 ("Trajectory","scFates ElPiGraph curve (N=20, \u03bb=0.3, \u03bc=100); non-branching; root Gast/pSom-high tip"),
 ("Gate 2 verdict","pattern absent \u2014 module means ~0, geography featureless, Gast\u2013pSom anti-correlate (\u22120.37)"),
 ("Rooting artifact","Crest terminal position flips with root (0.59 tip0 vs 0.41 tip2)"),
 ("EMT-TFs","panel SNAI/ZEB/TWIST/FOXC/PRRX (VIM excluded); only ZEB2 (5.1%) clears 3% floor"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Wu 2020 AML \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
