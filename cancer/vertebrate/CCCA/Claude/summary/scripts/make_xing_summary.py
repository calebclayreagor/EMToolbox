import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Lung/Xing2021_Lung"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Lung/Xing2021_Lung"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "All 18 samples (\u2265100 malignant cells) intermix per-neighbourhood on one continuous manifold: iLISI 1.4\u21924.5 "
  "across the \u03b8 0\u219210 sweep, diff-sample kNN fraction 0.72 (of a 0.91 ceiling), a single connected kNN component, "
  "0 detached islands. Cell cycle (~4.5%) is diffuse and does not fragment the cloud. Read on the regenerated "
  "embedding, not a scalar alone."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "The embryonic axis is present: a Gast/pSom-high origin pole giving way to an inverse terminal Neural-crest "
  "gradient (Crest \u03c1 vs pseudotime +0.69, Crest-high decile at pseudotime 0.92; joint pSom&Crest-high depleted, "
  "enrichment 0.28). Gast and pSom cross-repress (smoothed r=\u22120.52, \u22120.78 at the origin) but do NOT resolve into "
  "two competing arms \u2014 a branching-capable PPT fit gives no stable fork (forks grow 2\u21925 with node density on one "
  "roundish mass). Non-branching case, GO; no inversion flag."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable: the manifold is non-branching (single continuous developmental gradient, no stable bifurcation), "
  "so there is no hub convergence population to test for competitive Gast\u2194pSom cross-repression. The branching-only "
  "correlation and modules notebooks are therefore not produced."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Lung cancer (subsolid nodules + adjacent margins), 10x UMI counts \u2014 9,268 malignant cells across 25 samples "
 "\u2192 8,920 cells / 18 samples after the \u2265100-cell floor and island removal.")
verdict=("The embryonic pattern REPRODUCES in the non-branching form: a single continuous gastrulation/somitogenesis \u2192 "
 "neural-crest axis, rooted at the Gast/pSom-high developmental origin, with organised Gast\u2194pSom cross-repression "
 "that does not resolve into competing arms. EMT-TFs FOXC1 (root) \u2192 TWIST2 (terminus). Global module strength "
 "pSom>Gast~Crest (Linear-pSom/Crest).")
params=[
 ("Malignant load","9,268 cells / 25 samples (publication calls)"),
 ("After thresh + islands","8,920 cells / 18 samples"),
 ("Integration","Harmony \u03b8=10 (sweep-derived plateau)"),
 ("Embedding","n_pcs=20, n_neighbors=30, UMAP spread=1.3"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root","curve tip: Gast/pSom-high, Crest-low"),
 ("Topology","non-branching (2 tips, 0 forks, self-approach 2.7)"),
 ("EMT-TFs","FOXC1 (early, 9.6%) \u00b7 TWIST2 (late, 4.5%)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Xing 2021 lung cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
