import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Sarcoma/Jerby-Arnon2021_Sarcoma-1"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Sarcoma/Jerby-Arnon2021_Sarcoma-1"
gates=[
 ("Gate 1 — mixing & continuity","GO (scoped to SmartSeq2)",GREEN,
  "Two platforms (SmartSeq2 TPM, 12 pt; 10x UMI, 3 pt) are an irreducible batch \u2014 technology iLISI stays 1.0/2 "
  "under every Harmony strength and batch key. The SmartSeq2 compartment is one continuous, patient-integrated "
  "manifold (iLISI 1.0\u21926.2 of 11 patients, single component); 10x has only 3 patients and fragments. Per the "
  "biology-before-geometry rule the trajectory is scoped to SmartSeq2."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Signatures collapse onto one axis: smoothed Gast & pSom co-vary (r=+0.23) and both oppose Crest (\u22120.37 / \u22120.35). "
  "Along pseudotime Gast declines (\u03c1 \u22120.47) and Crest rises to a terminal pole (\u03c1 +0.48; Crest-high decile at "
  "t=0.71). No Gast-vs-pSom split \u2192 non-branching (still a GO). Crest enriches the terminus, not the Gast origin \u2192 "
  "no inversion flag."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No bifurcation: a PPT tree only wallpapers the compact cloud (forks grow 6\u21929\u219215 with node count), while the "
  "fold-free principal curve has 0 forks. With no two arms there is no hub to test for mutual Gast\u2194pSom repression."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Synovial sarcoma (Jerby-Arnon 2021); SmartSeq2 + 10x. 12,694 malignant cells merged; trajectory on the "
 "4,338-cell SmartSeq2 manifold (11 patients after thin-sample removal).")
verdict=("The embryonic programme reproduces as a single non-branching developmental axis \u2014 a Gast/pSom-high origin "
 "flowing to a neural-crest-high terminus, with cell cycle orthogonal (\u03c1 \u22120.01). This is the Linear-pSom/Crest "
 "geometry (pSom globally dominant, mean +0.32). No hub, no cross-repressing arms \u2192 Gate 3 NA. EMT axis: PRRX1 "
 "(early/root) \u2192 TWIST2 (late/terminus).")
params=[
 ("Integration scope","SmartSeq2 (technology irreducible: iLISI_tech=1.0/2)"),
 ("Sample threshold","\u226598 cells (mult-gap 296\u219233, 9.0\u00d7); drop SyS10"),
 ("Malignant cells","12,694 merged \u2192 4,338 SmartSeq2 (11 patients)"),
 ("Integration","Harmony \u03b8=10 on sample (iLISI 1.0\u21926.2/11); PCA20, spread 1.3"),
 ("Geometry","Linear-pSom/Crest (0 forks, fold ratio 2.95)"),
 ("Root","curve tip 0 = Gast/pSom-high, Crest-low"),
 ("Gene recovery","Gast 78/81 \u00b7 pSom 95/98 \u00b7 Crest 102/104"),
 ("EMT-TFs","PRRX1 (root) \u2192 TWIST2 (terminus)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Jerby-Arnon 2021 synovial sarcoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
