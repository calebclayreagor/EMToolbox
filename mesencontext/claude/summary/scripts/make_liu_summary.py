import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Liu2021_Hematologic-1"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Liu2021_Hematologic-1"
gates=[
 ("Gate 1 — mixing & continuity","NO-GO",RED,
  "Malignant plasma cells form a per-patient clonal archipelago. Across the full \u03b8\u00d7n_pcs Harmony sweep, 9/10 "
  "patients show self-neighbour enrichment >2.5\u00d7 (worst ~63\u00d7) \u2014 cells sit next to their own clone, not a shared "
  "state. iLISI peaks at only ~59% of ceiling (\u03b8=5) then declines; stronger integration does not merge the clones. "
  "Inter-patient clonal/CNV heterogeneity, not a sample-integrated continuum. Do not force a trajectory."),
 ("Gate 2 — module geography","NA",GREY,
  "Not evaluated \u2014 Gate 1 NO-GO halts the chain before the manifold/signature steps."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not evaluated \u2014 branching-only, and no trajectory was fit."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Multiple myeloma bone-marrow aspirates (Liu et al., 2021), 10x \u2014 17,003 malignant plasma cells "
 "(15 samples \u2265101 cells, 10 patients). Gate 1 NO-GO (clonal archipelago).")
verdict=("The developmental hub-and-arm pattern does NOT reproduce. Clonal MM plasma cells are irreducibly "
 "patient-segregated (Gate 1 NO-GO); no cell-state manifold or module geography can be honestly assessed. Consistent "
 "with the other MM datasets (Cohen 2021) in the atlas. EMT-TFs ZEB1 (11.1%) / ZEB2 (4.7%) \u2014 only detectable "
 "factors, descriptive only.")
params=[
 ("Min-cell threshold","\u2265101 cells \u2192 15/20 samples (17,003 cells); tail cliff 66\u2192156"),
 ("Integration","Harmony on sample; \u03b8 & n_pcs swept \u2192 \u03b8=5, n_pcs=40 (iLISI-maximal)"),
 ("Embedding","n_neighbors=30, spread=1.3"),
 ("Geometry","none fitted (Gate 1 NO-GO); global means Linear-pSom/Crest"),
 ("EMT-TFs shown","ZEB1 (11.1%) / ZEB2 (4.7%) \u2014 only detectable; VIM excluded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Liu 2021 multiple myeloma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
