import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Skin/Jerby-Arnon2018_Skin"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Jerby-Arnon2018_Skin"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "\u03b8 derived by connectivity (\u03b8=2 fragments the manifold into 2 components / 185 detached; \u03b8=5 = one component, "
  "0 detached, stable through \u03b8=10/20). Per-patient CNV texture is \u03b8-invariant (kNN-purity 2\u20138\u00d7 at every \u03b8) but "
  "no patient forms a disconnected island. Decisive: each of the 8 patients TRAVERSES the shared embryonic axis "
  "(\u03c1(axis,Crest) \u22120.66..\u22120.95, spanning 59\u201396%) \u2014 one continuous gastrulation\u2192neural-crest gradient, not a "
  "per-patient archipelago. iLISI 1.00\u21923.71 \u2014 mixed & continuous; no island removed."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "LOW-pSom, Crest-dominant melanoma (raw means Gast \u22120.49, pSom \u22120.14, Crest +0.20). Gast & pSom OVERLAP at the "
  "origin (spatial r=+0.93; joint-high enrichment 1.44) and decline together along pseudotime (Gast \u03c1=\u22120.98, pSom "
  "\u03c1=\u22120.92), opposed to a terminal neural-crest end that rises (Crest \u03c1=+0.93; decile pt=0.97). Crest "
  "anti-correlated in space (Crest\u2194Gast \u22120.91, Crest\u2194pSom \u22120.82); joint pSom&Crest-high depleted (0.28) \u2014 "
  "inverse gradient, not a hub. Crest peaks at the terminus, not a Gast arm \u2014 no inversion flag."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Single monotone axis \u2014 no bifurcation (curve: 2 tips, 0 forks; PPT tree yields only spurious forks) and no "
  "Gast/pSom-overlap Mixed hub, so there is no branch pair to test for Gast\u2194pSom cross-repression."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Cutaneous/metastatic melanoma (Jerby-Arnon et al., 2018), SmartSeq2 \u2014 23 samples / 7,186 cells (master "
 "scope); malignant only: 2,018 cells; \u2265100-cell floor \u2192 1,379 cells (8 samples) on the trajectory (no island "
 "removal, no scoping).")
verdict=("Non-branching pattern reproduces \u2014 G1 GO, G2 GO, G3 NA. The melanoma malignant manifold is a single monotone "
 "gastrulation/somitogenesis \u2192 terminal-neural-crest gradient (Gast \u03c1=\u22120.98, pSom \u03c1=\u22120.92, Crest \u03c1=+0.93); it "
 "lacks Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to test (Linear class). The atlas\u2019s LOW-pSom, "
 "Crest-dominant case \u2014 Crest the only positive module (+0.20), Gast (\u22120.49) and pSom (\u22120.14) globally weak, the "
 "neural-crest identity of a neural-crest-derived tumour. Two decisive derived calls: \u03b8=5 by connectivity, and a "
 "patient-SHARED continuous-axis test clearing Gate 1 despite \u03b8-invariant per-patient CNV texture. EMT "
 "terminus-loaded: ZEB1 marks the neural-crest terminus, TWIST1 the body factor (contrast Puram\u2019s SNAI1/ZEB1).")
params=[
 ("Cells / patients","1,379 / 8 (\u2265100 floor, 0 islands)"),
 ("Integration","Harmony \u03b8=5 (connectivity); PCA50"),
 ("Island removed","none (patient-shared axis)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","Gast/pSom-high, Crest-low tip"),
 ("Geometry","Linear (non-branching); 2 tips / 0 forks"),
 ("EMT-TFs","TWIST1 (body) \u00b7 ZEB1 (terminus); terminus-loaded, no root TF"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Jerby-Arnon 2018 melanoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
