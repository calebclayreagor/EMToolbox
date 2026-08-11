import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Head-and-Neck/Kürten2021_Head-and-Neck"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Head-and-Neck/Kürten2021_Head-and-Neck"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "9/20 samples (\u2265182 cells) intermix on one continuous manifold with no per-patient islands (radius-graph: 0 "
  "detached); the low-cycling embryonic lobe (5,955 cells) carries the trajectory."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.33) and decline along pseudotime (\u03c1=\u22120.32 / \u22120.38); Crest anti-correlated "
  "(r=\u22120.77 / \u22120.64), rising to a terminal readout (\u03c1=+0.44; crest-high decile mean pt=0.99)."),
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
dataset=("Head & Neck SCC (K\u00fcrten et al., 2021), 10x \u2014 33 patients / 62,700 cells (master scope); malignant only: "
 "11,122 across 9 samples (\u2265182) enter preprocessing; 5,955 embryonic-lobe cells enter the trajectory. Non-branching "
 "Linear-pSom/Crest.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. K\u00fcrten's malignant manifold is a "
 "single monotone Gast/pSom \u2192 terminal-Crest gradient (non-branching), matching the developmental axis; it lacks "
 "Puram's hub-and-spoke bifurcation, so Gate 3 has no hub to test. EMT-TFs FOXC1 (early/root) \u2192 SNAI2 "
 "(late/terminus); canonical SNAI1/ZEB1 near the detection floor (2.0%/2.3%).")
params=[
 ("Min cells/sample","\u2265182 (keeps 9/20; gap 89\u2192376)"),
 ("Lobe selection","embryonic (low-cycling 0.22) vs 0.46"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Integration","Harmony(sample) \u03b8=10; PCA 50PC; UMAP spread=1.3"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Compartments","Embryonic 5,955 / Cycling 5,167"),
 ("Geometry","Linear (non-branching); no hub"),
 ("EMT-TFs","FOXC1 (early/root) \u2192 SNAI2 (late/terminus); SNAI1/ZEB1 near floor"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"K\u00fcrten 2021 HNSCC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
