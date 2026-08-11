import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Hematologic/Cohen2021_Hematologic-2"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Cohen2021_Hematologic-2"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=5) fuses the patient-private myeloma clones: iLISI median 1.0\u219212.5 / 54 samples, one connected kNN "
  "component. Judged on the regenerated embedding across a \u03b8\u00d7n_pcs sweep \u2014 samples intermix on one continuous, "
  "low-cycling body (no proliferative lobe to scope). \u03b8=5 keeps the manifold axis-bearing; \u03b8=10 over-smooths to an "
  "axis-less blob."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Signatures resolve onto a single (Gast/pSom)\u2192Crest axis: smoothed Gast\u2194Crest r=\u22120.73, pSom\u2194Crest r=\u22120.65, "
  "Gast\u2194pSom r=+0.28 (overlap, not two competing arms). Crest is an inverse terminal gradient (Crest-high decile "
  "pseudotime 0.85 vs Gast 0.31 / pSom 0.15). Principal curve is fold-free (2 tips / 0 forks, self-approach 2.8). No "
  "Crest-on-Gast-arm inversion to flag."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Non-branching topology \u2014 no bifurcation and no Gast/pSom hub, so the branching-only cross-repression test does not "
  "apply. Correlation & modules notebooks are correctly not produced."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Multiple myeloma (Cohen et al., 2021), MARS-seq, 32,894 malignant plasma cells over 54 samples. "
 "Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces as the non-branching case \u2014 a single gastrulation/somitogenesis \u2192 neural-crest "
 "developmental axis; no hub, no bifurcation. Gate 1 GO / Gate 2 GO / Gate 3 NA. EMT-TF ZEB1 is the only factor above "
 "the 1% detection floor (terminally-differentiated plasma cells).")
params=[
 ("Min-cell threshold","\u2265100 floor (no dominant cliff); 54/73 samples kept"),
 ("Integration","Harmony on sample \u03b8=5; n_pcs=30, n_neighbors=30, spread=1.3"),
 ("Islands removed","253 cells / 14 detached specks (largest component)"),
 ("Geometry","Non-branching; scFates curve N=20, \u03bb=0.3, \u03bc=100 (2 tips / 0 forks)"),
 ("Root node","curve tip 2 = Gast/pSom-high, Crest-low (Crest-high at terminus)"),
 ("Module means (raw)","Gast \u22120.022 \u00b7 pSom +0.014 \u00b7 Crest +0.001 (Linear single axis)"),
 ("EMT-TFs shown","ZEB1 (3.2%) \u2014 only EMT-TF above the 1% floor; all others <0.3%"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Cohen 2021 multiple myeloma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
