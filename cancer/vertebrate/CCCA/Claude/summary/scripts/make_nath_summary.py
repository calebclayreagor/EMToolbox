import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Ovarian/Nath2021_Ovarian"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Ovarian/Nath2021_Ovarian"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) on 15 retained patients integrates the manifold: iLISI median 1.00 \u2192 5.50 (of 15). Read on the "
  "regenerated embedding + per-neighbourhood iLISI \u2014 patients intermix across one connected component (a 3-cell "
  "speck removed). Mixed AND continuous."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Over the low-cycling body a single (Gast/pSom) \u2192 Crest gradient: along pseudotime Gast/pSom fall (\u03c1 \u22120.22 / "
  "\u22120.60) and Crest rises to a terminal end (\u03c1 +0.21, Crest-high decile late). Crest opposes Gast in space (r=\u22120.41); "
  "joint pSom&Crest-high enrichment 0.42 (<1 = inverse gradient, not a co-expression hub)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve: 2 tips, 0 forks, fold-free). With no bifurcation "
  "there are no competing arms to test for mutual Gast\u2194pSom anti-correlation."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("High-grade serous ovarian carcinoma (Nath et al., 2021), 10x \u2014 32,484 malignant cells, 15 patients; "
 "trajectory scoped to the 26,703-cell low-cycling body. Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces (non-branching). A single gastrulation/somitogenesis \u2192 neural-crest developmental axis "
 "over the low-cycling HGSOC body; no bifurcation. Geometry Linear-pSom/Crest. Gates G1 GO / G2 GO / G3 NA. EMT-TFs "
 "FOXC1 (early/root, 27%) \u2192 ZEB2 (terminus, 4%).")
params=[
 ("Sample threshold","cliff 767\u2192149 (ratio 5.15) \u2192 geom-mean 338; keeps 15/18 (drops iCell8 + P10)"),
 ("Integration","Harmony on sample \u03b8=10; n_pcs=20, n_neighbors=30, spread=1.3"),
 ("Scope (cell-cycle fork)","proliferative lobe (5,781, 74% cyc) scoped out; body 26,703; modules cc-free"),
 ("Geometry / root","non-branching curve (N=20, \u03bc=100): 2 tips/0 forks; corr(t,x)=+0.98; root tip 0"),
 ("Module means (raw)","Gast \u22120.004 \u00b7 pSom +0.085 \u00b7 Crest \u22120.010 (Linear-pSom/Crest)"),
 ("EMT-TFs","FOXC1 (early/root, 27%) \u2192 ZEB2 (terminus, 4%); VIM excluded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Nath 2021 HGSOC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
