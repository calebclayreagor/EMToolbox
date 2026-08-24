import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/EMToolbox/mesencontext/claude/Lung/Zilionis2019_Lung-5"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Lung/Zilionis2019_Lung-5"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "6 samples (\u2265131-cell floor) intermix on one continuous manifold with no per-patient islands (radius-graph: 0 "
  "detached; iLISI 3.42/6; same-sample neighbour fraction 0.91\u21920.40 across the \u03b8 sweep). Roundish body (UMAP "
  "aspect 1.13), single connected component."),
 ("Gate 2 — module geography","NO-GO",RED,
  "Embryonic pattern absent. In score space the modules look anti-correlated (Gast/pSom \u22120.53, \u2248 Puram\u2019s "
  "branching \u22120.49) \u2014 but this is a shared-control-pool artifact: on RAW mean-expression all three POSITIVELY "
  "co-activate (Gast/pSom +0.58, Gast/Crest +0.45, pSom/Crest +0.51; survives library-size regression). One shared "
  "developmental field, not competing arms. No convergence hub (all joint-high enrichments depleted 0.07\u20130.62); "
  "Crest not terminal (high-decile pt 0.56, mid-axis); every principal-tree tip is pSom-dominant (no Gast/Crest arm)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not branching and Gate 2 NO-GO \u2014 no branch pair / hub to test for mutual exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("NSCLC (Zilionis et al., 2019), inDrop (droplet UMI) \u2014 7 patients / 3,995 malignant cells; 3,920 across 6 "
 "samples (all clear the \u2265131 floor) enter preprocessing; the whole malignant manifold (no lobe scoping) enters "
 "the trajectory.")
verdict=("Embryonic pattern does NOT reproduce \u2014 Gate 1 GO / Gate 2 NO-GO / Gate 3 NA. The malignant manifold is a "
 "single continuous, sample-integrated cloud organized by carcinoma metaprograms (Alveolar / cell-cycle / Stress / "
 "IFN; Moran\u2019s I 0.54 / 0.24 / 0.22 vs the embryonic modules\u2019 0.10\u20130.26), not by an embryonic hub-and-arms axis. "
 "The three modules form one shared low-amplitude activation field (raw co-activation +0.45\u2013+0.58): no Gast/pSom "
 "co-expression hub, no Gast or Crest arm (all tree tips pSom-dominant), and Crest sits mid-pseudotime (0.56), not "
 "terminal \u2014 the Peng2019 / Hwang2022 NO-GO signature, opposite Steele 2020\u2019s terminal-Crest GO. The score-space "
 "\u22120.53 that read as branching in five prior attempts is a union-control-pool subtraction artifact, not "
 "cross-repression. EMT-TF step run unconditionally: SNAI2 (early) \u2192 FOXC1 (late) chosen by data over Puram\u2019s "
 "SNAI1/ZEB1, all near the detection floor with negligible end-separation (\u0394pt \u2248 0) \u2014 consistent with no EMT axis.")
params=[
 ("Min cells/sample","\u2265131 (gap 232\u219275, r3.09; drops p2)"),
 ("Integration","Harmony \u03b8=10; 20 PCs; spread 1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","curve N=20, \u03bb=0.3, \u03bc=100; fold-free 2.46"),
 ("Root node","Gast-high, Crest-low tip (origin)"),
 ("Overdispersed","248 genes; PPT tree rejected"),
 ("Geometry","Non-branching; embryonic pattern absent \u2192 NO-GO"),
 ("EMT-TFs","SNAI2 (early) \u2192 FOXC1 (late); near floor, \u0394pt\u22480"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Zilionis 2019 NSCLC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
