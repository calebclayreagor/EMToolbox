import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Pancreas/Raghavan2021_Pancreas-4"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Pancreas/Raghavan2021_Pancreas-4"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (sample, \u03b8=5): same-sample neighbour fraction 0.94\u21920.26 (plateau by \u03b8=2); samples intermix "
  "per-neighbourhood (iLISI) on one continuous connected manifold; 0 detached islands removed."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching: Gast & pSom co-vary (smoothed r=+0.32, joint-high enrichment 1.15 = overlap) and both oppose Crest "
  "(r=\u22120.80 / \u22120.69); single Gast/pSom\u2192Crest gradient with Crest terminal (decile pseudotime 0.68). "
  "Classical/basal plasticity axis is real (r=\u22120.70) but ORTHOGONAL to the embryonic modules (pSom vs classical/basal "
  "+0.04/+0.05) \u2014 not the developmental bifurcation."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No Gast/pSom bifurcation (they overlap rather than cross-repress) \u2192 no hub to test. Gate 3 not applicable."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Pancreatic ductal adenocarcinoma (Raghavan et al., 2021), Seq-Well \u2014 7,168 malignant cells (20 samples); "
 "disease-restricted to PDAC (662 PANET cells excluded). Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces (non-branching): a single Gast/pSom\u2192Crest developmental axis with Crest terminal. Gate 1 "
 "GO / Gate 2 GO / Gate 3 NA. The classical/basal plasticity axis is real (r=\u22120.70) but orthogonal to the embryonic "
 "modules \u2014 not the developmental bifurcation. EMT-TFs FOXC1 (early/root) \u2192 ZEB2 (late/terminus).")
params=[
 ("Sample threshold","\u2265100 cells; 20/22 samples kept (45 & 29-cell samples dropped)"),
 ("Disease restriction","PDAC only (662 PANET cells, patient PANFR0580, excluded)"),
 ("Overdispersed genes","1,308; PCA 50PC; Harmony(sample, \u03b8=5)"),
 ("Embedding","knn n_pcs=20, n_neighbors=30; UMAP spread=1.3"),
 ("Trajectory","scFates curve N=15, \u03bb=0.3, \u03bc=100 (2 tips, 0 forks); corr(x,pt)=+0.97"),
 ("Root","Gast/pSom-high tip"),
 ("Geometry","Linear (non-branching); classical/basal axis orthogonal"),
 ("EMT-TFs","FOXC1 (early/root) \u2192 ZEB2 (late/terminus); 3% floor, no VIM"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Raghavan 2021 PDAC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
