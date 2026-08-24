import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Griffiths2021_Breast-5"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Griffiths2021_Breast-5"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "67/95 samples (\u2265100 cells) intermix on one continuous manifold; per-neighbourhood iLISI(sample) 1.02\u219215.3 "
  "(\u03b8=5), one kNN component (0 detached). The two density lobes are a proliferation / ribosomal axis (identical "
  "module scores), not per-patient islands."),
 ("Gate 2 — module geography","NO-GO",RED,
  "No Gast/pSom hub and no two-arm divergence: Gast-high and pSom-high populations are spatially anti-located "
  "(Jaccard 0.09; co-high fraction 0.007, below the 0.01 independence expectation) and stay negatively related after "
  "removing the ribosomal axis (partial r=\u22120.15) \u2014 Gast and pSom mark the two housekeeping lobes. The only embryonic "
  "relationship, a weak (Gast|pSom)\u2013vs\u2013Crest anti-correlation (r=\u22120.85), is transverse to the trajectory "
  "(|pseudotime \u03c1|\u22640.11) \u2014 matches neither GO template. The embryonic pattern does not reproduce."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not reached \u2014 Gate 2 NO-GO halts the chain, and the manifold is non-branching, so there is no hub or branch pair "
  "to test for Gast\u2194pSom cross-repression."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (Griffiths et al., 2021), neoadjuvant letrozole+ribociclib trial, 10x + iCell8 \u2014 41 patients "
 "/ 111,372 malignant cells. 100-cell floor keeps 67 samples; after stripping 2,324 islands and scoping 5,821 cycling "
 "cells, 102,179 cells form one continuous ER+ luminal body carrying the (attempted) trajectory. Non-branching.")
verdict=("Pattern does NOT reproduce \u2014 Gate 1 GO, Gate 2 NO-GO, Gate 3 NA. The manifold is one integrated, continuous, "
 "non-branching luminal body, but its dominant geometry is a proliferation/ribosomal axis, not the embryonic program. "
 "There is no Gast/pSom hub and no two arms \u2014 Gast and pSom are anti-located, marking the two housekeeping lobes "
 "(co-high 0.007 < chance). The only embryonic relationship is a weak (Gast|pSom)\u2013Crest anti-correlation (r=\u22120.85) "
 "transverse to the trajectory. Corrects five prior attempts that forced a Gate-2 GO on this housekeeping-confounded "
 "signal. Module means Gast \u22120.021 / pSom \u22120.052 / Crest +0.021.")
params=[
 ("Min cells/sample","\u2265100 floor (67/95; smooth dist, no cliff)"),
 ("Integration","Harmony \u03b8=5 (sample); PCA20; spread=1.3"),
 ("Scope","cycling + islands out; luminal body kept (102,179 cells)"),
 ("Trajectory","scFates curve (ElPiGraph) N=20; 2 tips / 0 forks"),
 ("Root node","curve tip, Gast/pSom-high Crest-low"),
 ("Geometry","Linear / non-branching (curve 2 tips)"),
 ("EMT-TFs","ZEB1 (~8.8%), ZEB2 (~5.0%) det.-gated; flat/non-directional; no VIM"),
 ("Overdispersed","3,444 genes; no scaling"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Griffiths 2021 breast cancer \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
