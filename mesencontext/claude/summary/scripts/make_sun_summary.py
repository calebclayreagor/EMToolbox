import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Liver-Biliary/Sun2021_Liver-Biliary"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Liver-Biliary/Sun2021_Liver-Biliary"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "6 patients (P04, P05, P09, P10, P16, P18) intermix on one connected component; a cycling-enriched lobe "
  "(~32%) does not separate, is not gastrulation-high, and leaves the Gast\u2194Crest gradient intact when "
  "removed \u2192 full manifold, no scoping."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Principal curve fold-free (2 tips, 0 forks); shared developmental gradient \u2014 Gast declines "
  "(\u03c1=\u22120.79) while Crest rises to the terminus (\u03c1=+0.60); smoothed Gast\u2194Crest r=\u22120.71 "
  "(inverse terminal gradient)."),
 ("Gate 3 — hub mutual exclusivity","NA",GREY,
  "Non-branching manifold \u2014 no fork, so the Gast\u2194pSom cross-repression test does not apply "
  "(branching-only gate; \u00a72)."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Hepatocellular carcinoma (Sun et al., 2021), 10x \u2014 16,498 cells / 18 samples (2,737 malignant). "
 "Malignant only: 2,338 pass the thin-sample threshold (cut 125, keeps 6 samples); 2,337 enter the trajectory "
 "after 1-cell island removal.")
verdict=("Malignant cells recapitulate an embryonic developmental gradient \u2014 a non-branching "
 "gastrulation\u2192neural-crest axis, no bifurcation. Gast declines while Crest rises to the terminus (smoothed "
 "Gast\u2194Crest r=\u22120.71). Gate 1 GO, Gate 2 GO (non-branching), Gate 3 NA. The EMT axis is monotone (no "
 "root-specific TF; all candidates rise to terminus); ZEB1 is the strongest terminus marker (53% expressing).")
params=[
 ("Malignant cells","2,737 raw (18 samples) \u2192 threshold cut 125 keeps 6 samples/2,338 \u2192 island removal 1 \u2192 2,337"),
 ("Expression / features","log-normalised 10x; 7,498 overdispersed (scFates find_overdispersed); modules vs union control pool"),
 ("Embedding","n_pcs=20; Harmony on sample (\u03b8=5); kNN k=15; UMAP spread=1.3; one connected component"),
 ("Trajectory","ElPiGraph principal curve on X_umap (Nodes=20, \u03bb=0.3, \u03bc=100); 2 tips, 0 forks; fold-free (self-approach 2.97)"),
 ("Root / orientation","root = Gast/pSom-high, Crest-low tip; pseudotime left\u2192right (orient_sx=+1, raw coords)"),
 ("EMT-TFs","panel SNAI/ZEB/TWIST + FOXC/PRRX, 3% floor; axis MONOTONE (all rise to terminus); ZEB1 strongest (53%)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Sun 2021 HCC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
