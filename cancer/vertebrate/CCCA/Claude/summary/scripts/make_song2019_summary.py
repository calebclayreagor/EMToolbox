import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Lung/Song2019_Lung"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Lung/Song2019_Lung"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "3 tumour samples (P4/P3/P1, \u2265100-cell floor after dropping the 3-cell P4_Normal spillover) intermix on one "
  "continuous manifold with no per-patient islands (radius-graph: 0 detached; iLISI median 1.00\u21921.65 of 3); a single "
  "Leiden lobe carries the whole trajectory."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single dominant (Gast/pSom)\u2192Crest axis: Gast/pSom high over the origin decline along pseudotime (Gast \u03c1=\u22120.72, "
  "pSom \u03c1=\u22120.37); Crest anti-correlated in space (Gast\u2194Crest r=\u22120.89), rising to a terminal readout (\u03c1=+0.74; "
  "Crest-high decile mean pt=0.84). Joint pSom&Crest-high depleted (enrichment 0.54) \u2014 an inverse gradient, not a "
  "co-expression hub."),
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
dataset=("NSCLC / lung adenocarcinoma (Song et al., 2019), 10x \u2014 6 samples / 8,772 cells (master scope); malignant "
 "only: 1,144 cells across 3 tumour samples (drop the 3-cell P4_Normal spillover); whole malignant manifold (single "
 "lobe, no scoping). Non-branching Linear-pSom/Crest.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Song's NSCLC malignant manifold is a "
 "single monotone gastrulation/somitogenesis \u2192 terminal-neural-crest gradient rooted at the Gast/pSom-high pole; it "
 "lacks Puram's hub-and-spoke bifurcation, so Gate 3 has no hub to test. The compartment is 57% cycling but forms one "
 "Leiden lobe \u2014 the axis is developmental, not proliferative (Gast/Crest cell-cycle-free; Gast\u2194Crest anti-correlation "
 "survives within non-cycling cells, r=\u22120.87; pseudotime\u2194cycling \u03c1=\u22120.19). EMT-TFs are detection-limited in this "
 "sparse 1.1k-cell compartment: only SNAI1 (root, 12.5%) and ZEB2 (terminus, 1.6%) survive the gene filter.")
params=[
 ("Min cells/sample","\u221a(62\u00b73)\u224813 (62\u21923 cliff) \u2192 3 tumour samples, 1,144 cells"),
 ("Scope","whole manifold (single lobe, no scoping)"),
 ("Root node","tip 2 = Gast/pSom-high"),
 ("Integration","Harmony \u03b8=10; n_pcs=20; spread=1.3"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Geometry","Linear-pSom/Crest (non-branching)"),
 ("EMT-TFs","SNAI1 (root, 12.5%) \u2192 ZEB2 (terminus, 1.6%); rest below detection"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Song 2019 NSCLC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
