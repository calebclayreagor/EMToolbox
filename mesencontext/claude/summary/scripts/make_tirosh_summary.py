import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Skin/Tirosh2016_Skin-1"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Skin/Tirosh2016_Skin-1"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "6/15 samples (\u226572 cells) intermix on one continuous manifold with no per-patient islands "
  "(radius-graph: 0 detached; iLISI median 1.00\u21924.00 of 6). Each of the 6 patients traverses the shared "
  "gastrulation\u2192neural-crest axis end-to-end (per-patient \u03c1(axis,Crest) \u22120.97..\u22120.80)."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single dominant Gast/pSom \u2192 Crest axis. Gast & pSom overlap at the origin (joint enrichment 1.37; "
  "spatial r=+0.97) and decline along pseudotime (\u03c1=\u22120.98/\u22120.98); Crest is the inverse terminal "
  "gradient (pSom&Crest enrichment 0.23, spatial r=\u22120.94), peaking at the terminus (Crest-high decile mean "
  "pt=0.98). Crest enriches the terminus, not a Gast arm \u2014 no inversion flag."),
 ("Gate 3 — hub mutual exclusivity","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Gast/pSom-overlap hub, so there is no branch pair to test "
  "for cross-repression."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Melanoma (Tirosh et al., 2016), SmartSeq2 \u2014 19 patients / 4,645 cells (full atlas); malignant only: "
 "1,257 load, 1,061 across 6 well-sampled tumours (\u226572 cells) enter preprocessing; the whole malignant "
 "manifold (no lobe scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Tirosh's melanoma malignant "
 "manifold is a single monotone gastrulation/somitogenesis \u2192 terminal-neural-crest gradient. Modules are "
 "globally Crest-dominant (Gast \u22120.51, pSom \u22120.07, Crest +0.15) \u2014 the canonical neural-crest melanoma "
 "signature; Gast and pSom co-vary and both oppose Crest, so the axis is developmental, not a competing "
 "hub-and-spoke bifurcation \u2014 Gate 3 has no hub to test. The axis is cell-cycle-decoupled (module\u2013prolif "
 "|r|\u22640.11; 9.5% cycling), so the whole manifold is kept. EMT-TFs TWIST1 (body/origin) \u2192 SNAI2 "
 "(terminus); ZEB2/SNAI2 broadly expressed, canonical TWIST1 near the detection floor.")
params=[
 ("Min cells/sample","\u226572 (6/15; cliff 98\u219254, ratio 1.81)"),
 ("Integration","Harmony \u03b8=10; PCA50; n_pcs=20; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Geometry","Linear \u2014 non-branching (Crest terminus)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Tirosh 2016 Melanoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
