import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Brain/Hovestadt2019_Brain"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Hovestadt2019_Brain"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "25 samples intermix per-neighbourhood on one continuous manifold (iLISI 1.17\u21927.67; 0 islands removed). Judged on "
  "the regenerated embedding across a Harmony {2,5,10} sweep \u2014 no per-sample archipelago despite strong "
  "medulloblastoma molecular-subgroup batch effect. Cycling compartment present but Gast is not proliferation-"
  "confounded (r=\u22120.13), so the embryonic axis is real and the whole manifold is retained."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Non-branching case: Gast & pSom co-vary (r=+0.46, overlap \u2014 no two competing arms), Crest an inverse terminal "
  "gradient (Crest\u2013Gast r=\u22120.90, Crest\u2013pSom r=\u22120.67). Single (Gast/pSom)\u2192Crest developmental axis; Crest-high decile "
  "at pseudotime 0.82 (terminal). Passes Gate 2 as the non-branching outcome."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No bifurcation \u2014 no hub to test. Gate 3 is branching-only, so it is Not Applicable for this linear manifold."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Medulloblastoma (Hovestadt et al., 2019), SmartSeq2 \u2014 7,921 malignant cells across 25 samples (of 36; "
 "\u2265100-cell floor). Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces as the non-branching case \u2014 one embryonic Gast/pSom \u2192 Crest axis, Crest inverse-terminal; "
 "no bifurcation (Gate 3 NA). Rooted at the Gast/pSom-high pole (Gast early, Crest late); the embryonic axis is not "
 "proliferation-confounded so the whole manifold is retained. EMT-TFs TWIST2 (early/root) \u2192 PRRX1 (late/terminus).")
params=[
 ("Min-cell threshold","\u2265100 (no cliff) \u2192 25/36 samples, 7,921 cells"),
 ("Integration","Harmony on sample \u03b8=5, n_pcs=20 (mixing saturates 5\u201310)"),
 ("Island removal","0 cells"),
 ("Geometry","Linear (non-branching); scFates curve N=20, \u03bc=100, fold-free (2.97)"),
 ("Root node","curve tip 2 = Gast/pSom-high, Crest-low origin"),
 ("Module means","Gast \u22120.043 \u00b7 pSom +0.186 \u00b7 Crest \u22120.026"),
 ("EMT-TFs","TWIST2 (early, pt 0.24) \u2192 PRRX1 (late/terminus, pt 0.50)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Hovestadt 2019 medulloblastoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
