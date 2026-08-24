import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Colorectal/Li2017_Colorectal"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Colorectal/Li2017_Colorectal"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "9/10 samples (248 malignant cells) intermix on one continuous, elongated manifold (radius-graph: 0 detached "
  "islands; kNN: 1 component); whole manifold enters the trajectory."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.89) and decline along pseudotime (\u03c1 \u22120.82 / \u22120.37); Crest anti-correlated "
  "(r=\u22120.96 / \u22120.97), rising to a terminal readout (\u03c1 +0.56; crest-high decile pt=1.00)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub, so there is no branch pair to test for mutual "
  "exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Colorectal carcinoma (Li et al., 2017), SmartSeq2 \u2014 18 samples / 590 cells (master scope); 254 malignant "
 "loaded; 248 across 9 patients (\u22658 cells) enter preprocessing; the whole malignant manifold (no lobe scoping) enters "
 "the trajectory. Non-branching Linear-pSom/Crest.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Li's colorectal malignant manifold is a "
 "single monotone Gast/pSom \u2192 terminal-Crest gradient (non-branching), matching the developmental axis; it lacks "
 "Puram's hub-and-spoke bifurcation, so Gate 3 has no hub to test. Cell cycle is orthogonal to the axis (pseudotime\u2194"
 "cycling \u03c1=\u22120.01), so the whole manifold is kept. EMT-TFs ZEB1 (early/root) \u2192 FOXC1 (late/terminus); end-separation "
 "weak (\u0394pt=0.14) at this SmartSeq2 depth (248 cells).")
params=[
 ("Min cells/sample","\u22658 (keeps 9/10; smooth counts)"),
 ("Integration","Harmony \u03b8=5; PCA(HVG); spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=15, \u03bb=0.3, \u03bc=100"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("HVG","seurat 2000 (pagoda2 degenerate at n=248)"),
 ("EMT-TFs","ZEB1 (early/root) \u2192 FOXC1 (late/terminus); \u0394pt=0.14"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Li 2017 CRC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
