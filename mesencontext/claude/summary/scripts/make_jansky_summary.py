import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Neuroendocrine/Jansky2021_Neuroendocrine"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Neuroendocrine/Jansky2021_Neuroendocrine"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "13/14 samples (\u2265269 cells) intermix on one continuous manifold with no per-patient islands; the kNN "
  "graph is a single connected component (27,987 cells; one 129-cell spillover sample dropped). "
  "Same-sample-neighbour fraction 0.233 vs mixing null 0.111 \u2014 well-integrated across 13 patients."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast/pSom decline together along pseudotime (\u03c1=\u22120.44/\u22120.14) and co-vary positively (r=+0.55); "
  "Crest is spatially anti-correlated (r=\u22120.72/\u22120.80) and rises to a terminal readout (\u03c1=+0.36; "
  "crest-high decile mean pt=0.72). Modules ride a dominant noradrenergic-differentiation axis \u2014 present, "
  "but not resolved into two competing arms."),
 ("Gate 3 — hub mutual exclusivity","NA",GREY,
  "Single monotone differentiation axis \u2014 no bifurcation and no Gast/pSom-overlap hub, so there is no "
  "branch pair to test for competitive cross-repression."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Neuroblastoma (Jansky et al., 2021), 10x \u2014 childhood adrenal NB; malignant only: 28,116 load, "
 "27,987 across 13 samples on one continuous manifold; the full compartment carries the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Jansky's manifold is a single "
 "noradrenergic-differentiation axis (progenitor \u2192 differentiating neuronal); embryonic modules ride it as a "
 "secondary Gast/pSom \u2192 terminal-Crest gradient, lacking Puram's hub-and-spoke, so Gate 3 has no hub to test. "
 "EMT-TFs monotone: ZEB1 (42% det) rises weakly to the terminus; canonical SNAI1/2, TWIST1, PRRX1, FOXC1 sit "
 "near the detection floor (no mesenchymal arm).")
params=[
 ("Min cells/sample","\u2265269 (keeps 13/14; gap 561\u2192129, r4.35)"),
 ("Integration","Harmony(sample) \u03b8=5; 50PC\u219220; UMAP spread=1.3"),
 ("Malignant states","Noradren. progenitor 17,333 / Differentiating 10,654"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100 (fold-free, 2 tips)"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Manifold","full malignant (no lobe split); 1 kNN component"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Jansky 2021 Neuroblastoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
