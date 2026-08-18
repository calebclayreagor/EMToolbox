import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Breast/Pal2021_Breast-2"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Breast/Pal2021_Breast-2"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "iLISI 1.00\u21924.95 of 22 samples (per-neighbourhood, \u03b8=10); one connected component on the independent "
  "Harmony-PCA and diffusion-map graphs. Mixed and continuous."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single organized axis: pSom/Gast-high origin \u2192 Crest-high terminus (Crest decile pt 0.93; pSom&Crest enrich 0.23, "
  "inverse terminal gradient). Non-branching \u2014 no Gast/pSom co-expression hub (enrich 1.03)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No bifurcation (no hub, no second arm) \u2014 not applicable. Gast & pSom show mild spatial cross-repression "
  "(smoothed r=\u22120.32 on the Body), permitted in the non-branching case."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (Pal et al., 2021), 10x \u2014 59,367 malignant cells (22/26 samples); trajectory scoped to the "
 "44,398-cell low-cycling Body. Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces in the non-branching form \u2014 one continuous pSom/Gast \u2192 Crest developmental axis, no "
 "Gast/pSom bifurcation. G1 GO / G2 GO / G3 NA. EMT-TFs PRRX2 (origin) \u00b7 SNAI1 (latest) \u2014 all 5 detected factors "
 "peak at the origin, none Crest-terminal.")
params=[
 ("Min-cell threshold","12 (geom-mean of 56\u21923 cliff); keeps 22/26 samples"),
 ("Integration","Harmony \u03b8=10, n_pcs=20 (iLISI plateau 5\u201310)"),
 ("Geometry","Linear (non-branching); scFates curve N=20, 2 tips / 0 forks"),
 ("Root","pSom/Gast-high, Crest-low origin; terminus Crest-high"),
 ("Scope (cell-cycle)","Body 44,398 (low-cycling); 14,965 proliferative compartment excluded"),
 ("Module means (all)","Gast \u22120.007 \u00b7 pSom +0.036 \u00b7 Crest \u22120.034; hub enrich 1.03 (none)"),
 ("Cycle independence","pt vs proliferation \u03c1=0.10 (cycle-independent axis)"),
 ("EMT-TFs","PRRX2 (origin) \u00b7 SNAI1 (latest); all 5 detected peak at origin"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Pal 2021 breast cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
