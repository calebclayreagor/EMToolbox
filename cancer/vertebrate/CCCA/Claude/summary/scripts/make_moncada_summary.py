import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Pancreas/Moncada2020_Pancreas"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Pancreas/Moncada2020_Pancreas"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Both patients intermix on one continuous manifold \u2014 no per-patient islands. Single connected component "
  "(radius-graph 0 detached; kNN-graph in Harmony-PCA also 1 component); iLISI median 1.00\u21921.97 of 2. Density dips "
  "mid-axis but no empty bins \u2014 one manifold, not two islands."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single pSom\u2192Gast/Crest axis: pSom high at the origin falls along pseudotime (\u03c1=\u22120.89) while Gast (\u03c1=+0.77) and "
  "Crest (\u03c1=+0.27) rise to the terminus. Gast\u2194pSom strongly anti-correlated in space (r=\u22120.89) \u2014 organised "
  "cross-repression \u2014 but the manifold does not bifurcate (0 forks). Joint pSom&Crest enrichment 0.29 (<1: inverse "
  "gradient). FLAG (passes anyway): Crest enriches the Gast end (r(Crest,Gast)=+0.38 vs r(Crest,pSom)=\u22120.56) \u2014 "
  "inversion of the canonical arm assignment."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks). No bifurcation, so the "
  "branching-only hub cross-repression test is not run."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("PDAC (Moncada et al., 2020), inDrop \u2014 2 patients / 3,659 cells; malignant only: 635 cells (publication "
 "cell_type==\"Malignant\"), both samples clear the \u2265100-cell floor, whole malignant manifold (no lobe scoping). "
 "Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces in the non-branching form (Linear-pSom/Crest): one continuous somitogenesis \u2192 "
 "gastrulation/neural-crest axis, rooted at the pSom-high origin. Gast/pSom show organised cross-repression (r=\u22120.89) "
 "without bifurcation, so Gate 3 has no hub to test (NA). Crest inverts onto the Gast end (flagged). EMT-TFs are "
 "root-enriched (FOXC1 dominant at 46%, SNAI2 next); no distinct terminus factor. G1 GO / G2 GO / G3 NA.")
params=[
 ("Sample threshold","\u2265100-cell floor (only 2 samples \u2192 gap-finding degenerate); both kept \u2192 635 cells"),
 ("Overdispersed genes","68 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample \u03b8=10 (mixing reaches 2-sample chance floor)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3 (inDrop scale); 0 islands removed"),
 ("Geometry","non-branching curve N=20, \u03bb=0.3, \u03bc=100; 2 tips / 0 forks (2.84)"),
 ("Root","tip 2 = Gast/pSom-high, Crest-low developmental origin"),
 ("Module means (raw)","Gast \u22120.011 \u00b7 pSom +0.115 \u00b7 Crest \u22120.064 (Linear-pSom/Crest)"),
 ("EMT-TFs","FOXC1 (root, 46%) & SNAI2 (root, 9%); all expressed EMT-TFs root-enriched"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Moncada 2020 PDAC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
