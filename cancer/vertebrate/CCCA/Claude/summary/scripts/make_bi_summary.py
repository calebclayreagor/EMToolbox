import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Kidney/Bi2021_Kidney"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Kidney/Bi2021_Kidney"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "5/8 samples (natural-break \u2265160 cells) intermix on one continuous manifold; no per-patient islands "
  "(41 detached cells removed). Diff-sample kNN 0.46 = 0.67 of the mixing ceiling; 1 component."),
 ("Gate 2 — module geography","GO",GREEN,
  "Non-branching: Gast/pSom co-vary from a shared origin (no opposing arms); Crest is the inverse terminal "
  "gradient (Crest\u2013pSom r = \u22120.65; Crest vs pseudotime = +0.71). pSom globally strongest."),
 ("Gate 3 — hub mutual exclusivity","NA",GREY,
  "No bifurcation and no Gast/pSom hub \u2014 the branching-only cross-repression test does not apply."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Kidney renal-cell carcinoma (Bi et al., 2021), 10x \u2014 8 patients / 34,326 cells (master scope); "
 "malignant only: 8,040 load, 7,822 across 5 samples enter the trajectory.")
verdict=("Pattern reproduces (non-branching). A single embryonic axis runs from a Gast/pSom-high origin to a "
 "Neural-crest-high terminus \u2014 the programs are present but not resolved into competing arms, so there is "
 "no hub and Gate 3 is NA. EMT-TFs: canonical factors all decline toward the terminus; only ZEB2 clears the "
 "detection floor (19%) and marks the mesenchymal/gastrulation origin \u2014 no bipolar EMT-TF split.")
params=[
 ("Min cells/sample","\u2265160 (natural break, keeps 5/8)"),
 ("Integration","Harmony on sample, \u03b8=10"),
 ("Island removal","UMAP radius-graph (\u221241 cells)"),
 ("Trajectory","scFates curve N=20 (non-branching)"),
 ("Root node","tip 0 = Gast/pSom origin"),
 ("Modules","score_genes, union control pool"),
 ("n_pcs / spread","20 / 1.3"),
 ("Overdispersion","scFates find_overdispersed"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Bi 2021 Kidney RCC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
