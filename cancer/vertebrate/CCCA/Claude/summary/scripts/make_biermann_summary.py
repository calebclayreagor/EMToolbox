import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Skin/Biermann2022_Skin"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Skin/Biermann2022_Skin"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "30 samples (brain-met MBM + peripheral-met MPM, sn/sc) with private melanoma CNV: pre-Harmony same-sample "
  "fraction 0.985. Harmony(\u03b8=10) collapses it to one continuous component (99.97% of cells; 169 detached specks "
  "removed), mixing iLISI 1.0\u21926.4/30, met-sites interleave (1.78/2). Every one of 28 patients traverses the shared "
  "embryonic axis end-to-end (median span 94%) \u2014 a patient-SHARED continuous gradient, not a per-patient "
  "archipelago."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "LOW-pSom, Crest-dominant melanoma (raw means Gast \u22120.05, pSom \u22120.02, Crest +0.05 \u2014 Crest the only positive "
  "module). No Gast/pSom co-expression hub (joint-high enrichment 0.91) \u2014 the two cross-repress in space (r=\u22120.57). "
  "Crest is an inverse TERMINAL gradient: depleted where pSom/Gast are high (joint 0.23 / 0.29), peaking at the "
  "trajectory terminus (Crest decile pt 0.60, latest; \u03c1=+0.32). Crest peaks at the terminus, not a Gast arm \u2014 no "
  "inversion flag."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Single monotone axis \u2014 no bifurcation (curve: 2 tips, 0 forks, fold-free; a PPT tree yields only spurious forks) "
  "and no Gast/pSom co-expression Mixed hub, so there is no branch pair to test for Gast\u2194pSom cross-repression."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Metastatic melanoma (Biermann et al., 2022), 10x \u2014 30 samples (brain-met MBM + peripheral-met MPM, "
 "single-nucleus/single-cell); 136,973 cells master scope, 91,525 malignant; \u2265100-cell floor keeps all 30 samples, "
 "169 detached specks removed \u2192 91,356 on the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 G1 GO, G2 GO, G3 NA. The malignant manifold is a single monotone axis "
 "rooted at the Gast/pSom-high origin \u2192 terminal neural-crest end (pSom \u03c1=\u22120.50, Crest \u03c1=+0.32 along pseudotime); "
 "it lacks Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to test. The atlas\u2019s LOW-pSom, Crest-dominant "
 "case \u2014 Crest the only positive module, the neural-crest identity of a neural-crest-derived tumour. Cell-cycle "
 "confound checked: pSom tracks proliferation (r=+0.50) but Crest, the trajectory-defining module, is decoupled "
 "(\u22120.33), so the axis is developmental and the whole manifold is kept. EMT terminus-loaded: ZEB2 marks the "
 "neural-crest terminus (79%), SNAI2 the body (14%).")
params=[
 ("Cells / patients","91,356 / 30 (\u2265100 floor)"),
 ("Integration","Harmony \u03b8=10; PCA 20PC; spread 1.3"),
 ("Island removed","169 cells (0.18%, sn micro-blobs)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","tip 2 = Gast/pSom-high, Crest-low"),
 ("Geometry","Linear (non-branching); 2 tips / 0 forks"),
 ("EMT-TFs","SNAI2 (body) \u00b7 ZEB2 (terminus); terminus-loaded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Biermann 2022 melanoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
