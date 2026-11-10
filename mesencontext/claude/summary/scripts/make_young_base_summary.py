import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Kidney/Young2018_Kidney"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Kidney/Young2018_Kidney"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "7/25 samples (\u2265100 cells) intermix on one continuous manifold (kNN = 1 component; 0.91 of the "
  "perfect-mixing ceiling), no per-patient islands (radius-graph: 3 specks stripped). No proliferation "
  "compartment (most-cycling lobe 1.5%); module means near-identical across all 3 lobes \u2192 whole manifold."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Single dominant pSom\u2192Crest axis: pSom high over the body declines along pseudotime (\u03c1=\u22120.75); Crest "
  "anti-correlated (r=\u22120.78), rising to a terminal readout (\u03c1=+0.72; Crest-high decile mean pt=0.89). Gast "
  "weakly structured (\u03c1=+0.39). Joint pSom&Crest-high depleted (enrichment 0.22) \u2014 an inverse gradient, "
  "not a co-expression hub."),
 ("Gate 3 \u2014 hub mutual exclusivity","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub, so there is no branch pair to test for mutual "
  "exclusivity."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Wilms tumour / RCC (Young et al., 2018), 10x \u2014 66 samples / 125,139 cells (master scope); malignant "
 "only: 2,055 cells \u2192 1,438 after \u2265100/sample threshold (7/25 samples) \u2192 1,435 after island removal enter "
 "preprocessing; the whole malignant manifold (no lobe scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Young\u2019s kidney malignant "
 "manifold is a single monotone somitogenesis\u2192terminal-neural-crest gradient (pSom-high body \u2192 "
 "neural-crest-like terminus), matching the developmental axis; it lacks Puram\u2019s hub-and-spoke bifurcation, so "
 "Gate 3 has no hub to test. The manifold is continuous and cell-cycle-free (most-cycling lobe 1.5%, Gast vs g2m "
 "r=\u22120.02), so no proliferation caveat; the whole manifold is kept (Bi/Steele no-scoping precedent). Module "
 "means Gast \u22120.008 / pSom +0.042 / Crest \u22120.029 (pSom-dominant Linear-pSom/Crest). EMT-TFs ZEB2 (early/root, "
 "23.3% expressing, \u03c1=\u22120.20) \u2192 FOXC1 (late/terminus, 3.6%, \u03c1=+0.03) \u2014 FOXC1 surfaces only via the "
 "widened panel; end-separation weak (\u0394pt=0.27). Curve fold-free (self-approach 2.84, 0 forks).")
params=[
 ("Min cells/sample","\u2265100 floor (7/25; gap non-dominant)"),
 ("Scope","whole manifold (no scoping)"),
 ("Root node","tip 0 = pSom-high, Crest-low"),
 ("Geometry","Linear-pSom/Crest (non-branching)"),
 ("Integration","Harmony \u03b8=10; PCA50; spread=1.3"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Overdispersed","262 genes; n_pcs=30"),
 ("EMT-TFs","ZEB2 (early) \u00b7 FOXC1 (late)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Young 2018 Kidney (Wilms/RCC) \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
