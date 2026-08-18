import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Kidney/Krishna2021_Kidney"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Kidney/Krishna2021_Kidney"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "UT2_Center + UT2_Far intermix on one continuous manifold; 0 detached islands, single Leiden compartment "
  "(\u03b8=10, mixing plateau). Judged on the embedding, not a scalar alone."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching: a single pSom\u2192Crest gradient (pSom_sm\u2013Crest_sm r=\u22120.89); Crest terminal (crest-high decile mean "
  "pt=0.97); Gast weak/diffuse."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No bifurcation (2 tips, 0 forks) \u2014 the competitive Gast\u2194pSom arm test does not apply. Non-branching case, as in "
  "prior Kidney runs (Bi/Zhang)."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Clear-cell RCC (Krishna et al., 2021), 10x; 5,715 malignant cells pre-filter, 5,006 after thresholding (all "
 "CD45\u2212 ccRCC CA9+). One continuous non-branching manifold.")
verdict=("Pattern reproduces (Linear-pSom/Crest). A single embryonic axis rooted at the somitogenesis-high origin "
 "flows to a neural-crest terminus (pSom \u03c1=\u22120.85, Crest \u03c1=+0.75 vs pseudotime); no Gast/pSom bifurcation, so "
 "Gate 3 is NA. Caveat: the clean 15.9\u00d7 count gap retains only two regions of one patient (UT2), 5,006/5,715 "
 "cells, so integration is region-level; cycling \u03c1=\u22120.23 vs pt (not proliferation-driven).")
params=[
 ("Min cells/sample","403 (geom-mean 15.9\u00d7 gap; keeps UT2)"),
 ("Integration","Harmony \u03b8=10; PCA20; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","tip 2 = Gast/pSom-high, Crest-low"),
 ("Geometry","Linear (non-branching); 2 tips / 0 forks"),
 ("EMT-TFs","TWIST2 (early) \u00b7 ZEB2 (late)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Krishna 2021 ccRCC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
