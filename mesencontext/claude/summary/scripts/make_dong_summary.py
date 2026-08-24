import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Prostate/Dong2020_Prostate-5"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Prostate/Dong2020_Prostate-5"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "All 4 malignant-bearing samples (\u2265915 cells each) intermix in one connected manifold \u2014 single kNN component, 0 "
  "detached islands; iLISI median rises 1.00\u21921.28/4 under integration (one patient is ~49% of cells, capping the "
  "scalar). Judged on the embedding across a \u03b8\u00d7n_pcs sweep, not a scalar."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single Gast/pSom \u2192 Crest axis. Gast & pSom spatially OVERLAP and co-vary (r=+0.47) \u2014 not a pSom-arm vs Gast-arm "
  "split; both oppose Crest (Gast\u2013Crest \u22120.38, pSom\u2013Crest \u22120.40). Along pseudotime Gast/pSom fall (pSom \u03c1=\u22120.41) "
  "and Crest rises (\u03c1=+0.39) \u2014 an inverse terminal gradient, not a hub-and-spoke bifurcation."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Gast/pSom-overlap \u201cMixed\u201d hub with divergent arms, so there is no "
  "branch pair to test. (Spatially-defined hub Gast\u2194pSom r\u2248\u22120.04, i.e. no cross-repression; the apparent \u22120.38 "
  "under sum-thresholding is a collider/selection artifact, not competition.)"),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Prostate cancer (Dong et al., 2020), 10x \u2014 9,698 malignant cells across 4 samples (\u226510x floor keeps all; "
 "no clean count gap). 8,281 enter the trajectory after a cross-patient cycling compartment (1,417 cells) is "
 "scoped out; the developmental manifold is a single connected component.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. The malignant manifold is a single "
 "monotone gastrulation/somitogenesis \u2192 terminal-neural-crest gradient, a strict linear subset of Puram\u2019s "
 "hub-and-spoke: Gast & pSom co-vary and overlap rather than diverging into competing arms, so there is no Mixed "
 "hub and no bifurcation to test. Raw module means Gast +0.035 / pSom +0.100 / Crest \u22120.041. An orthogonal "
 "AR-luminal \u2194 neuroendocrine lineage axis (decoupled from clinical histology) is continuous and multi-patient \u2014 "
 "not a second trajectory. Curve is fold-free (self-approach 1.74; independent-diffusion continuity \u22120.79). "
 "EMT-TFs: SOX9 (early/root) \u2192 TWIST1 (terminus), detection-gated, VIM excluded.")
params=[
 ("Min cells/sample","\u2265100 (no count gap; all 4 samples 915\u20134765)"),
 ("Integration","Harmony \u03b8=10; PCA 50; spread=1.3"),
 ("Scope","cycling lobe excluded (1,417) \u2192 8,281 dev"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","Gast/pSom-high tip (Crest-low origin)"),
 ("Embedding","n_pcs=20; overdispersed=1,670"),
 ("Geometry","Linear (non-branching); 2 tips / 0 forks"),
 ("EMT-TFs","SOX9 (early/root) \u2192 TWIST1 (terminus); hub r NA"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Dong 2020 prostate cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
