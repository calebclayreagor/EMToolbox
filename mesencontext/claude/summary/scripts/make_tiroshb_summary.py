import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Brain/Tirosh2016_Brain"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Brain/Tirosh2016_Brain"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "All 6 tumours intermix per-neighbourhood (iLISI 1.02\u21924.30 of 6 under Harmony \u03b8=10) on ONE continuous manifold "
  "(single kNN component, 0 islands removed) \u2014 no per-patient archipelago."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.38) and BOTH oppose Crest (\u22120.85 / \u22120.59): a single developmental axis with Crest an "
  "inverse terminal gradient. Non-branching case \u2014 GO. Crest enriches the terminus, not a Gast arm."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No bifurcation \u2014 scFates curve is robustly fold-free (2 tips, 0 forks, self-approach 2.99 across Nodes 15\u201330). "
  "Hub cross-repression is not defined for a linear axis \u2014 Gate 3 not tested."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("IDH-mutant oligodendroglioma (Tirosh et al., 2016), SmartSeq2 (TPM) \u2014 4,089 malignant cells across 6/6 "
 "samples. Non-branching Linear-pSom/Crest.")
verdict=("The embryonic-program pattern reproduces as the non-branching case: one continuous gastrulation/somitogenesis "
 "\u2192 neural-crest developmental axis, rooted at the Gast/pSom-high pole with Crest as an inverse terminal gradient. No "
 "Gast\u2013pSom bifurcation (Gate 3 NA). Geometry Linear-pSom/Crest (pSom \u03bc=+0.16 globally strongest; Gast \u22120.04, Crest "
 "\u22120.20). EMT-TFs SNAI2 \u00b7 ZEB2 (both rise to the Crest terminus).")
params=[
 ("Min-cell threshold","\u2265100 \u2192 6/6 samples (4,089 cells); counts descend smoothly 1185\u2192428"),
 ("Genes / embedding","5,800 overdispersed genes; n_pcs=20; Harmony \u03b8=10 on sample"),
 ("Islands removed","0 (single kNN component; continuous manifold)"),
 ("Geometry","non-branching curve (N=20, \u03bb=0.3, \u03bc=100): 2 tips / 0 forks, fold-free"),
 ("Root node","curve node 2 = Gast/pSom-high, Crest-low origin"),
 ("EMT-TFs","ZEB1 (82%), ZEB2 (83%), PRRX1 (38%), SNAI2 (3%) rise to Crest; display SNAI2 \u00b7 ZEB2"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Tirosh 2016 IDH-mut oligodendroglioma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
