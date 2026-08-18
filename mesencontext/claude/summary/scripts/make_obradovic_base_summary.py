import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Kidney/Obradovic2021_Kidney"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Kidney/Obradovic2021_Kidney"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "6/8 samples (dominant 522\u2192153 cliff, cut at geo-mean 282) intermix on one continuous manifold with no "
  "per-patient islands (radius-graph: 0 detached; iLISI median 1.00\u21924.28 of 6); both low-cycling lobes "
  "(main body 8,207 / neural-crest terminus 902) carry the axis."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single dominant pSom\u2192Crest axis: pSom high over the main body declines along pseudotime (\u03c1=\u22120.56); "
  "Crest anti-correlated (r=\u22120.95), rising to a terminal readout (\u03c1=+0.67; Crest-high decile mean pt=0.93). "
  "Gast co-varies weakly with pSom (r=+0.47), also declining (early programme, spent); joint pSom&Crest-high "
  "depleted (enrichment 0.21) \u2014 an inverse gradient, not a co-expression hub."),
 ("Gate 3 — hub mutual exclusivity","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub, so there is no branch pair to test for mutual "
  "exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Clear-cell RCC (Obradovic et al., 2021), 10x \u2014 8 patients / 19,781 cells (master scope); malignant "
 "only: 9,369 cells; 9,109 across 6 tumour-bearing samples (drop 2 spillover samples below the 522\u2192153 cliff) "
 "enter preprocessing; the whole malignant manifold (no lobe scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Obradovic's ccRCC malignant "
 "manifold is a single monotone somitogenesis\u2192terminal-neural-crest gradient (somitogenesis-high body \u2192 "
 "neural-crest-like terminus), matching the developmental axis; it lacks Puram's hub-and-spoke bifurcation, so "
 "Gate 3 has no hub to test. Malignant cells are almost entirely non-cycling (~1%), so unlike K\u00fcrten/Lin/Qian "
 "there is no proliferative-lobe confound: both lobes are low-cycling with near-identical developmental means, and "
 "the whole manifold is kept (Bischoff/Sun/Lee/Steele no-scoping precedent). The clean-count-gap premise is met "
 "here (dominant cliff 522\u2192153, ratio 3.41 \u226b runner-up 1.86), so the threshold is cut at the geometric mean "
 "(282), not the \u2265100 floor. EMT-TFs are root/body-loaded: ZEB2 (early) \u2192 ZEB1 (late) chosen by data over "
 "Puram's SNAI1/ZEB1 pair, but all expressed factors decline along pt and end-separation is weak (\u0394pt=0.08); no "
 "factor rises to the neural-crest terminus.")
params=[
 ("Min cells/sample","282 (geo-mean of 522\u2192153 cliff; 6/8)"),
 ("Integration","Harmony \u03b8=10; PCA50; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Root node","tip 0 = pSom-high, Crest-low"),
 ("Lobes","body 8,207 / terminus 902"),
 ("EMT-TF axis","ZEB2 (early) \u2192 ZEB1 (late)"),
 ("Geometry","Linear / non-branching (fold-free)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Obradovic 2021 ccRCC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
