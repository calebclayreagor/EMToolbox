import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Lung/Chan2021_Lung-3"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Lung/Chan2021_Lung-3"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "24 of 34 malignant-bearing samples (\u226537 cells each) intermix on one continuous manifold with no per-patient "
  "archipelago (radius-graph: 118/50,999 island cells removed; iLISI median 6.17 of 24); proliferation lobe kept \u2014 "
  "modules are cell-cycle-free."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single embryonic axis: Gast and pSom co-vary (smoothed r=+0.48 \u2014 overlap, not competitive cross-repression); "
  "Crest is an inverse terminal gradient rising where pSom falls (pSom\u2194Crest r=\u22120.80). No hub diverging into two "
  "arms; the Gast\u2194pSom co-variation strengthens in non-cycling cells (+0.48\u2192+0.59)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Non-branching manifold \u2014 a curve with 2 tips / 0 forks (PPT tree also 0 forks), so there is no branch pair and no "
  "convergence hub to test for cross-repression."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("SCLC (Chan et al., 2021), 10x \u2014 37 samples / 86,662 cells (CCCA master scope). Malignant only: 51,052 cells "
 "across 34 samples \u2192 min-cell threshold (\u226537 cells/sample) keeps 50,999 cells across 24 samples \u2192 island removal "
 "\u2192 50,881 cells enter the trajectory; whole manifold (no lobe scoping).")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Chan\u2019s SCLC malignant manifold is a "
 "single continuous gastrulation/somitogenesis \u2192 terminal-neural-crest gradient rooted at the Gast/pSom-high pole, "
 "matching the developmental axis; it lacks Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to test. "
 "SCLC-A/SCLC-N subtypes do not form two module-opposed arms, and the embedding carries a proliferation axis, but "
 "the embryonic modules are cell-cycle-free (|r| with cycling \u22640.16) and the Gast\u2194pSom co-variation strengthens in "
 "non-cycling cells (+0.48\u2192+0.59; the pSom\u2194Crest anti-correlation persists, \u22120.80\u2192\u22120.77), so the whole manifold is "
 "kept. The curve is fold-free (far-node approach / edge = 24.7). EMT-TFs (widened panel incl. FOXC/PRRX): TWIST1 "
 "(root-leaning) \u2192 SNAI1 (terminus-leaning), all weakly pseudotime-associated (|\u03c1|\u22640.11) \u2014 consistent with a "
 "diffuse linear axis.")
params=[
 ("Min cells/sample","\u226537 (dominant 92\u219215 cliff)"),
 ("Integration","Harmony \u03b8=5; n_pcs=20"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=30, \u03bb=0.3, \u03bc=100"),
 ("Root node","tip 2 = Gast/pSom-high"),
 ("Overdispersed HVG","3,228"),
 ("Geometry","Linear (non-branching); 2 tips / 0 forks"),
 ("EMT-TFs","TWIST1 (root) \u00b7 SNAI1 (terminus); |\u03c1|\u22640.11"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Chan 2021 SCLC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
