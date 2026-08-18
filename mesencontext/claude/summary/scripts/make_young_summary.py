import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Kidney/Young2018_Kidney-1"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Kidney/Young2018_Kidney-1"
gates=[
 ("Gate 1 — mixing & continuity","NO-GO",RED,
  "The malignant compartment is a composite of THREE biologically distinct kidney cancers \u2014 clear-cell RCC (1,373), "
  "Wilms tumour (287), papillary RCC (144). Each sample is (near-)pure for one type (Cram\u00e9r V(sample,type)=0.93), so "
  "integrating \u201csamples\u201d integrates three cancers. Across a \u03b8 0\u219220 sweep, per-neighbourhood iLISI(tumour-type) "
  "stays ~1.0\u20131.2 vs a 1.64 well-mixed ceiling: the types never intermix at any integration strength. The kNN graph "
  "is one component throughout (the misleading scalar), but the embedding shows type-segregated islands."),
 ("Gate 2 — module geography","N/A",GREY,
  "Not evaluated \u2014 Gate 1 NO-GO halts the chain before the manifold / signature steps."),
 ("Gate 3 — cross-repression","N/A",GREY,
  "Not evaluated \u2014 branching-only, and no trajectory is fit."),
]
panels=[("Malignant manifold — samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Kidney cancer (Young et al., 2018), 10x scRNA-seq. 2,055 malignant cells loaded; 1,804 retained after "
 "sample thresholding (\u226563 cells). A mixture of clear-cell RCC, pediatric Wilms tumour, and papillary RCC.")
verdict=("The embryonic-development cell-state pattern does NOT reproduce: the malignant \u201cmanifold\u201d is not one "
 "continuous cell-state continuum but three unrelated cancers that refuse to integrate. Gate 1 = NO-GO; no "
 "trajectory is fit. Geometry: none (un-integrable composite of three malignancies).")
params=[
 ("Sample threshold","\u226563 cells (geo-mean of 87\u219247 gap, 1.85\u00d7); 11/25 kept \u2192 1,804 cells"),
 ("Overdispersed genes","531 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample; \u03b8 swept 0\u201320, read per-neighbourhood; \u03b8=2 for visual"),
 ("n_pcs / spread","20 / 1.3 (10x precedents at ~1.8k cells)"),
 ("Root / geometry","None \u2014 no trajectory fit (Gate 1 NO-GO)"),
 ("EMT-TFs shown","ZEB2 (25.4%) \u00b7 FOXC1 (9.5%); FOXC/PRRX added, VIM excluded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Young 2018 kidney cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
