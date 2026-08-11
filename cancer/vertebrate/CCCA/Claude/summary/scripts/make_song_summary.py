import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Prostate/Song2022_Prostate"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Prostate/Song2022_Prostate"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "14/15 samples clear the \u2265100-cell floor and intermix per-neighbourhood (iLISI median 1.95 \u2192 7.12 of 14 "
  "after Harmony \u03b8=10); one continuous manifold, 0 detached islands."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Dominant inverse gradient pSom\u2194Crest (r=\u22120.85); Gast\u2194pSom weak (r=\u22120.19). Tree tips all share "
  "one program \u2192 spurious forks; curve fold-free (self-approach 2.93). Single pSom\u2192crest axis."),
 ("Gate 3 — hub mutual exclusivity","NA",GREY,
  "No bifurcation, so no convergence hub to test. Joint pSom&Crest-high enrichment 0.27 (\u226a1) confirms an "
  "inverse gradient, not a co-expression hub."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Prostate Cancer (Song et al., 2022), Seq-Well S3 \u2014 15 samples / 21,743 cells (master atlas); 4,658 "
 "malignant cells, of which 14 samples clear the \u2265100-cell floor \u2192 4,574 cells on the whole-manifold "
 "trajectory. Uniformly luminal AR-driven adenocarcinoma (KLK3 in 97% of cells). Two AR-output compartments: "
 "Luminal-AR-active (3,916) and Luminal-AR-low (658). Cycling 0.7%, orthogonal to all developmental programs.")
verdict=("Non-branching linear trajectory on a somitogenesis\u2192neural-crest embryonic axis. Root at the "
 "Gast/pSom-high, Crest-low tip; pseudotime runs Gast/pSom-high \u2192 Crest-high (Crest decile mean pseudotime 0.95, "
 "terminal). Gate 1 GO, Gate 2 GO (non-branching), Gate 3 NA. Classical mesenchymal EMT-TFs are largely below "
 "detection (max FOXC1 2.4%) \u2014 the honest low-EMT readout for a luminal epithelial adenocarcinoma; FOXC1 (early) "
 "/ TWIST1 (late) shown.")
params=[
 ("Min-cell threshold","\u2265100 floor (mult. gap degenerate at rank 0); 14/15 kept"),
 ("Integration","Harmony on sample \u03b8=10 (plateaus by \u03b8=5); PCA 50\u219220"),
 ("Overdispersed genes","199; neighbours k=30; UMAP spread=1.3, seed=1"),
 ("Islands / lobes","UMAP radius graph 6\u00d7 median-NN (0 removed); Leiden res=0.15"),
 ("Trajectory","curve 20 nodes, epg \u03bb=0.3 \u03bc=100 (fold-free 2.93)"),
 ("Root","Gast/pSom-high tip (Crest-low origin)"),
 ("EMT-TF axis","FOXC1 (early) \u2192 TWIST1 (late)"),
 ("Geometry","Linear \u2014 pSom/Crest (non-branching)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Song 2022 Prostate Cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
