import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Colorectal/Lee2020_Colorectal"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Colorectal/Lee2020_Colorectal"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "14/15 samples (\u2265151 cells) intermix on one continuous manifold with no per-patient islands "
  "(radius-graph: 0 detached); both lobes (Embryonic 6,147 / Cycling 4,823) carry the trajectory."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.49) and decline along pseudotime (\u03c1=\u22120.76/\u22120.56); Crest anti-correlated "
  "(r=\u22120.81/\u22120.83), rising to a terminal readout (\u03c1=+0.77; crest-high decile mean pt=0.95)."),
 ("Gate 3 — hub mutual exclusivity","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Mixed-type hub, so there is no branch pair to test for "
  "mutual exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Colorectal Carcinoma (Lee et al., 2020), 10x \u2014 15 patients / 21,657 cells (master scope); malignant "
 "only: 11,075 load, 10,970 across 14 samples (\u2265151) enter preprocessing; the whole malignant manifold "
 "(no lobe scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Lee's colorectal malignant "
 "manifold is a single monotone Gast/pSom \u2192 terminal-Crest gradient (non-branching), matching the "
 "developmental axis; it lacks Puram's hub-and-spoke bifurcation, so Gate 3 has no hub to test. Unlike Kürten, "
 "the developmental axis spans both lobes (Crest terminus inside the cycling lobe), so the whole manifold is kept "
 "(Bischoff/Sun no-scoping precedent). EMT-TFs FOXC1 (early/root) \u2192 SNAI1 (late/terminus); ZEB1/TWIST near the "
 "detection floor (0.8%/0.2%); EMT-TF end-separation weak (\u0394pt=0.22).")
params=[
 ("Min cells/sample","\u2265151 (keeps 14/15; gap 219\u2192105)"),
 ("Integration","Harmony \u03b8=10; PCA50; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Compartments","Embryonic 6,147 / Cycling 4,823"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Lee 2020 CRC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
