import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Lung/Laughney2020_Lung"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Lung/Laughney2020_Lung"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "\u03b8 derived by connectivity (\u03b8=5 fragments an 11% blob; \u03b8=10 = one component). One patient (RU680, 125 cells) "
  "stays a same-patient clump at every \u03b8 (kNN-purity 16\u00d7 vs \u22647\u00d7 for the rest) \u2014 an unintegrable island, removed. "
  "Remaining 7/13 samples (2,734 cells) share one continuous manifold, max purity 6.6\u00d7, iLISI 1.00\u21923.24 \u2014 mixed "
  "& continuous."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single developmental axis driven by posterior-somitogenesis (pSom): pSom high at the origin declines along "
  "pseudotime (\u03c1=\u22120.87) opposed to a terminal neural-crest end that rises (\u03c1=+0.26; decile pt=0.68); Crest "
  "anti-correlated in space (Crest\u2194Gast \u22120.72, Crest\u2194pSom \u22120.45); Gast weak (\u03c1=+0.26, mid-axis) and "
  "\u2248independent of pSom (r=\u22120.11). Joint pSom&Crest-high depleted (0.36) \u2014 inverse gradient, not a hub."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Single monotone axis \u2014 no bifurcation (curve: 2 tips, 0 forks) and no Mixed-type hub, so there is no branch pair "
  "to test for Gast\u2194pSom cross-repression."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Metastatic LUAD (Laughney et al., 2020), 10x \u2014 13 patients / 40,505 cells (master scope); malignant only: "
 "3,128 cells; \u2265100-cell floor \u2192 2,859 (8 samples), minus one unintegrable patient-private island (RU680, 125) \u2192 "
 "2,734 cells / 7 patients on the trajectory (no scoping).")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Laughney\u2019s LUAD malignant manifold is a "
 "single monotone posterior-somitogenesis \u2192 terminal-neural-crest gradient (pSom \u03c1=\u22120.87, Crest \u03c1=+0.26); it "
 "lacks Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub to test (Linear-pSom/Crest class, shared with "
 "Qian / K\u00fcrten / Steele). Two decisive derived calls: integration strength \u03b8=10 by connectivity, and removal of "
 "RU680 \u2014 a patient-private island that stays 16\u00d7 kNN-pure at every \u03b8, which the connectivity test alone had let "
 "pass. No cell-cycle annotation / flat proliferation, so no cycling lobe is scoped (contrast Qian). EMT "
 "terminus-loaded: expressed EMT-TFs lean late, ZEB2 marks the neural-crest terminus, no root-end factor "
 "(contrast Puram\u2019s SNAI1/ZEB1 pair).")
params=[
 ("Cells / patients","2,734 / 7 (\u2265100 floor, \u22121 island)"),
 ("Integration","Harmony \u03b8=10 (connectivity); PCA50"),
 ("Island removed","RU680 (125 cells; 16\u00d7 pure, \u03b8-inv.)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","pSom-high, Crest-low tip"),
 ("EMT-TFs","terminus-loaded (ZEB2); no root factor"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Laughney 2020 LUAD \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
