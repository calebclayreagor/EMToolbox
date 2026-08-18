import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Hematologic/Zhang2019_Hematologic-5"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Zhang2019_Hematologic-5"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "4/4 samples (\u2265100 cells) intermix on one continuous manifold with no per-patient islands (iLISI 1.00\u21922.26 of 4 "
  "at Harmony \u03b8=10; same-patient nbr frac 0.60; 1 kNN component, 0 detached). Strongly clonal FL batch integrates "
  "into one body."),
 ("Gate 2 — module geography","NO-GO",RED,
  "Embryonic programs are at the control-pool noise floor (means Gast +0.012 / pSom +0.006 / Crest +0.009, 20\u201340\u00d7 "
  "below real-pattern datasets). No Gast/pSom hub (joint-high enrichment 1.0). Gast\u2013pSom r and Crest pseudotime "
  "gradient sit INSIDE the random-module 95% null band (48th / 72nd null percentile) \u2014 no embryonic-specific signal. "
  "Pattern absent."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not reached \u2014 Gate 2 NO-GO halts the gate chain. No bifurcation (curve: 2 tips, 0 forks) and no hub, so there is "
  "no branch pair to test for cross-repression."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Follicular lymphoma (Zhang et al., 2019), 10x \u2014 2 patients (FL1018, FL2001) / 7,002 cells; malignant only: "
 "5,645 B cells across 4 samples (all clear the \u2265100 floor); whole malignant manifold (no lobe scoping). Pattern "
 "absent \u2014 Gate 2 NO-GO.")
verdict=("Pattern does NOT reproduce \u2014 Gate 1 GO, Gate 2 NO-GO, Gate 3 NA. The FL malignant manifold is one "
 "integrated continuum, but the gastrulation/somitogenesis/neural-crest programs are absent: means at the "
 "control-pool floor and, decisively, Gast\u2013pSom co-variation and the Crest pseudotime gradient are indistinguishable "
 "from random gene sets of equal size (48th / 72nd null percentile). No Gast/pSom hub (enrichment 1.0). This corrects "
 "5 prior attempts that called Gate 2 GO by reading score_genes shared-pool artifacts (and, in -4, a circularly-scoped "
 "196-cell cycling lobe that flipped Gast\u2013pSom to +0.33). EMT-TFs ZEB2 (28%) \u00b7 ZEB1 (12%), both terminus-loaded; "
 "SNAI/TWIST/FOXC/PRRX below 3% detection.")
params=[
 ("Min cells/sample","\u2265100 floor (4/4; gap 2.74 not a cliff) \u2192 5,645 cells"),
 ("Scope","whole manifold (no scoping; verified robust across scopes)"),
 ("Root node","tip 2 = Gast/pSom-high, Crest-low"),
 ("Integration","Harmony \u03b8=10; PCA20; spread=1.3"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100 (fold-free, 2 tips / 0 forks)"),
 ("Decisive test","200-draw random-gene-set null (same sizes/pool/smoothing)"),
 ("Gate readout","G1 GO / G2 NO-GO / G3 NA (module means .012/.006/.009)"),
 ("EMT-TFs","ZEB2 (28%) \u00b7 ZEB1 (12%), both terminus-loaded; rest below 3% detection"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Zhang 2019 follicular lymphoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
