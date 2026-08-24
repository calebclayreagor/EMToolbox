import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Ovarian/Qian2020_Ovarian-1"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Ovarian/Qian2020_Ovarian-1"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "4/4 tumours (920\u20133345 malignant cells) intermix on one continuous manifold at Harmony \u03b8=10 (per-neighbourhood "
  "iLISI 1.87 of a 2.89 ceiling); radius-graph: 0 detached islands."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.36) and decline along pseudotime (\u03c1=\u22120.48/\u22120.54); Crest anti-correlated "
  "(r=\u22120.28/\u22120.43), rising to a terminal readout (\u03c1=+0.48; crest-high decile pt=0.68). Single (Gast/pSom)\u2192Crest "
  "developmental axis."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Single monotone axis \u2014 a PPT tree's arms co-vary in Gast/pSom (r=+0.68), so there is no bifurcation and no "
  "Gast/pSom hub; no branch pair exists to test for cross-repression."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Ovarian cancer (Qian et al., 2020), 10x \u2014 4 tumours / 16,951 cells (master scope); malignant only: 6,490 "
 "load across all 4 samples (no thin tail to threshold; 0 islands removed). Whole malignant manifold (no lobe "
 "scoping). Non-branching Linear-pSom/Crest.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Qian's ovarian malignant manifold is a "
 "single monotone Gast/pSom \u2192 terminal-Crest gradient (Linear-pSom/Crest), matching the developmental axis; it lacks "
 "Puram's hub-and-spoke bifurcation, so Gate 3 has no hub to test. The developmental axis is orthogonal to the "
 "proliferation split (holds among non-cycling cells alone), so the whole manifold is kept (Lee/Bischoff no-scoping "
 "precedent). EMT-TFs PRRX1 (early/root) \u2192 PRRX2 (late); all TFs decline from the mesenchymal origin.")
params=[
 ("Min cells/sample","\u2265100 (keeps 4/4; no thin tail)"),
 ("Integration","Harmony \u03b8=10; PCA 20; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=15, \u03bb=0.3, \u03bc=100"),
 ("Root node","tip = Gast/pSom-high, Crest-low"),
 ("Compartments","non-cycling 4,971 / cycling 1,519 (axis orthogonal to split)"),
 ("EMT-TFs","PRRX1 (early/root) \u2192 PRRX2 (late); SNAI1/FOXC2 near detection floor"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Qian 2020 ovarian cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
