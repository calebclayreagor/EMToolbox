import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Giustacchini2017_Hematologic-1"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Giustacchini2017_Hematologic-1"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "29/34 primary samples (\u226529 cells) intermix on one continuous manifold with no per-patient islands (iLISI 8.67 of "
  "23.39 ceiling, n_pcs=40 \u03b8=10; radius-graph: 0 detached). K562 cell line (91 cells) scoped out \u2014 a detached, "
  "cycling clone reproducing none of the reference relationships."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single developmental axis: Gast/pSom overlap (r=\u22120.04, no competing arms); Crest an inverse terminal gradient "
  "opposing Gast (r=\u22120.88) and pSom (r=\u22120.37). Along pseudotime Gast falls (\u03c1=\u22120.96), Crest rises to a terminal "
  "readout (\u03c1=+0.79; crest-high decile mean pt=0.98)."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Gast/pSom co-expression hub, so there is no branch pair to test for "
  "mutual exclusivity."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Chronic myeloid leukemia (Giustacchini et al., 2017), SmartSeq2/HiSeq 2000 \u2014 42 samples / 2,287 cells "
 "(master scope); malignant only: 2,055 load, 1,845 primary cells across 29 samples (\u226529) enter the trajectory after "
 "the K562 cell line is scoped out. Non-branching Linear-pSom/Crest.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. The primary CML malignant manifold is a "
 "single monotone gastrulation \u2192 terminal-neural-crest gradient rooted at the Gast/pSom-high, Crest-low origin; it "
 "lacks Puram's hub-and-spoke bifurcation (PPT tree: 2 tips, 0 forks), so Gate 3 has no hub to test. Crest peaks at "
 "the low-Gast terminus \u2014 no inversion. EMT-TFs ZEB1 (earlier) \u2192 ZEB2 (terminus); SNAI1/TWIST1/FOXC1/PRRX1 below "
 "the 3% floor.")
params=[
 ("Min cells/sample","\u226529 (keeps 29/34; smooth, 30\u219229 step)"),
 ("Scope","primary tumour (K562 cell line dropped)"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Integration","Harmony \u03b8=10; n_pcs=40; PCA50; spread=1.3"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Geometry","Linear-pSom/Crest (non-branching)"),
 ("EMT-TFs","ZEB1 (earlier) \u2192 ZEB2 (terminus); rest below 3% floor"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Giustacchini 2017 CML \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
