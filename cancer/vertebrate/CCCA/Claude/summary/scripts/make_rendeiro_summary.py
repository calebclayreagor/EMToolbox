import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Hematologic/Rendeiro2020_Hematologic-5"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Rendeiro2020_Hematologic-5"
gates=[
 ("Gate 1 — mixing & continuity","NO-GO",RED,
  "Judged on the regenerated embedding across a \u03b8-sweep (1/2/3/5/10 \u00d7 n_pcs 20/30/40) with per-neighbourhood iLISI. "
  "The malignant compartment is a per-patient archipelago: unintegrated kNN patient accuracy 99.7%, Leiden 99.3% "
  "patient-pure. Harmony mixes only by forced over-integration \u2014 even at \u03b8=10, patient kNN accuracy stays 52% "
  "(chance 34%) and iLISI plateaus ~3.0/4. Signatures carry no manifold geography (Moran's I +0.02 = random-signature "
  "control). No single connected continuous developmental gradient \u2014 NO-GO."),
 ("Gate 2 — module geography","not evaluated",GREY,
  "Not evaluated \u2014 the gate chain stops at the Gate 1 NO-GO (no integrated continuous manifold on which to read a "
  "Gast/pSom hub or arms). For the record, modules are near-zero and cell-cycle-orthogonal, and Gast\u2013pSom co-vary "
  "(r=+0.05, no cross-repression)."),
 ("Gate 3 — cross-repression","not evaluated",GREY,
  "Not evaluated \u2014 reached only when a branching manifold clears Gates 1\u20132. No trajectory is fit (correlation / "
  "modules notebooks correctly not produced)."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Chronic lymphocytic leukemia (Rendeiro et al., 2020), 10x \u2014 18,598 malignant B-cells over 7 samples / 4 "
 "patients (longitudinal ibrutinib). Each patient is a genetically distinct CLL clone.")
verdict=("Pattern does NOT reproduce. Gate 1 NO-GO \u2014 a per-patient clonal archipelago with no shared continuous "
 "manifold and no embryonic module geography. No trajectory is warranted; analysis stops at preprocessing + the "
 "unconditional EMT-TF step.")
params=[
 ("Min-cell threshold","\u2265100 (multiplicative cliff 1012\u219280, 12.65\u00d7); 7/11 samples"),
 ("Malignant cells","18,854 raw \u2192 18,657 (threshold) \u2192 18,598 (island removal)"),
 ("Overdispersed genes","528; PCA 50 comps, NO scaling"),
 ("Integration","Harmony on sample \u03b8=2 canonical; swept 1/2/3/5/10 \u00d7 n_pcs 20/30/40"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 59 island cells removed"),
 ("Cell cycle","42.2% cycling; modules cell-cycle-orthogonal (r +0.02) \u2014 no lobe to scope"),
 ("Geometry","None \u2014 no manifold/trajectory fit (Gate 1 NO-GO); Gast\u2013pSom +0.05 (not branching)"),
 ("EMT-TFs","ZEB2 (12.3%) \u00b7 ZEB1 (3.8%) \u2014 only TFs above 3% floor; VIM excluded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Rendeiro 2020 CLL \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
