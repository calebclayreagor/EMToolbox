import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Brain/Venteicher2017_Brain"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Brain/Venteicher2017_Brain"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "9 samples intermix per-neighbourhood (iLISI 1.0\u21924.99/9) on one continuous manifold (single kNN component, 0 "
  "islands); no per-patient archipelago."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.60) and both oppose Crest (\u22120.89 / \u22120.76): one developmental axis, Crest an inverse "
  "terminal gradient. Non-branching case."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No bifurcation (curve: 2 tips, 0 forks, fold-free across params) \u2192 not tested."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("IDH-mutant astrocytoma (Venteicher et al., 2017), SmartSeq2 (TPM) \u2014 10 samples; 4,985 malignant cells "
 "across 9/10 samples enter the analysis; the whole malignant manifold enters the trajectory (non-branching linear "
 "geometry).")
verdict=("The embryonic-program pattern reproduces as the non-branching case: a single continuous "
 "gastrulation/somitogenesis\u2192neural-crest developmental axis, rooted at the Gast/pSom-high pole with Crest as an "
 "inverse terminal gradient. No Gast\u2013pSom bifurcation (Gate 3 NA). Linear pSom/Crest geometry (pSom \u03bc=+0.21 "
 "globally strongest). Gate 1 GO, Gate 2 GO (non-branching), Gate 3 NA. EMT-TFs ZEB1 (91% pan-tumour) \u2192 PRRX1 "
 "(terminus-enriched).")
params=[
 ("Min-cell threshold","\u2265146 \u2192 9/10 samples, 4,985 cells (tail gap 192\u2192112, r=1.71; geo-mean cut)"),
 ("Genes / embedding","6,317 overdispersed (GAM); n_pcs=20 (scree elbow~6 rejected); Harmony \u03b8=10"),
 ("Islands removed","0 (single connected kNN component; radius-graph = 1 component)"),
 ("Geometry","Non-branching \u2014 scFates curve N=20, \u03bb=0.3, \u03bc=100 (2 tips, 0 forks; fold-free, self-approach 2.96)"),
 ("Root","curve tip 0 \u2014 Gast/pSom-high, Crest-low (developmental origin; Crest is late)"),
 ("EMT-TFs","ZEB1 (91% pan-tumour) \u2192 PRRX1 (terminus-enriched); Snail/Twist/FoxC families near-absent"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Venteicher 2017 IDH-mut astrocytoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
