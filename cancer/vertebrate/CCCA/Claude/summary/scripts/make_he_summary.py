import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Prostate/He2021_Prostate"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Prostate/He2021_Prostate"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "11/12 samples (\u226510 cells) intermix on one continuous manifold with no per-patient islands (radius-graph: 0 "
  "detached; iLISI median 2.11\u21925.56 of 11 samples). All three transcriptional lobes (213 / 298 / 322 cells) carry "
  "the trajectory."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single dominant Gast/pSom\u2192Crest axis: gastrulation high at the origin declines steeply along pseudotime "
  "(\u03c1=\u22120.99); neural-crest anti-correlated (r=\u22120.82 vs Gast, \u22120.70 vs pSom), rising to a terminal readout "
  "(\u03c1=+0.85; crest-high decile mean pt=0.91). Gast\u2194pSom weakly positive (+0.18 \u2014 co-vary, not compete); joint "
  "pSom&Crest-high depleted (enrichment 0.15) \u2014 an inverse gradient, not a co-expression hub."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub, so there is no branch pair to test for mutual "
  "exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Metastatic prostate cancer (He et al., 2021), SmartSeq2 \u2014 15 samples / 2,170 cells (master scope); "
 "malignant only: 836 cells across 12 samples; 833 across 11 samples enter preprocessing (\u22655-cell floor drops one "
 "3-cell sample); the whole malignant manifold (no lobe scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. He\u2019s mCRPC malignant manifold is a "
 "single monotone gastrulation/somitogenesis \u2192 terminal-neural-crest gradient, matching the developmental axis; it "
 "lacks Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to test. The axis spans all three transcriptional "
 "lobes (orthogonal to cell cycle; Crest\u2013cyc \u03c1\u22480.00, Gast\u2013cyc \u03c1=\u22120.31), so the whole manifold is kept. Raw module "
 "means (Gast \u22120.30 / pSom +0.05 / Crest +0.05) place it in the Linear-pSom/Crest class; the gate turns on geography "
 "\u2014 a resolved single axis with a terminal Crest readout \u2014 not the means. EMT-TFs: canonical SNAI1/ZEB1/ZEB2/TWIST1 "
 "all below the 3% floor (FOXC/PRRX absent from the SmartSeq2 matrix), so the detectable EMT signal is the "
 "neural-crest/mesenchymal TF program rising to the terminus (SOX4 42%, \u03c1=+0.31); overlay LEF1 (early) \u2192 SOX4 "
 "(late), end-separation weak (\u0394pt=0.12).")
params=[
 ("Min cells/sample","\u22655 (geo-mean of 10\u21923 gap; 11/12)"),
 ("Integration","Harmony \u03b8=10; PCA50; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Embedding","n_pcs=15; lobes 213/298/322"),
 ("Geometry","Linear (non-branching); no hub"),
 ("EMT-TFs","LEF1 (early) \u2192 SOX4 (late); canonical set below 3% floor"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"He 2021 mCRPC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
