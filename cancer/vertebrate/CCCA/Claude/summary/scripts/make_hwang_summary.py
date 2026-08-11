import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Pancreas/Hwang2022_Pancreas-3"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Pancreas/Hwang2022_Pancreas-3"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Pre-Harmony the 29 tumours form a per-patient archipelago (iLISI 1.0 of 29; same-sample neighbour frac 0.95). "
  "Harmony on sample intermixes them into one continuous mass \u2014 iLISI 8.8, same-sample 0.17, a single kNN-graph "
  "component after complete island removal (107 detached-speck nuclei \u2192 63,997). \u03b8=2 from the sweep (mixing "
  "saturates by \u03b8=2; geography \u03b8-invariant). Three density lobes, all 2\u20138% cycling \u2014 no proliferation compartment."),
 ("Gate 2 — module geography","NO-GO",RED,
  "Judged on geography vs an explicit null, not the means (flattest in the atlas: Gast \u22120.004 / pSom \u22120.002 / Crest "
  "+0.003). The embryonic modules carry NO coherent territory: each module\u2019s Moran\u2019s I sits at/below its own "
  "size-matched union-pool null (Gast I=0.06 z=\u22120.4 p=0.65; pSom z=\u22120.2 p=0.55; Crest z=\u22120.5 p=0.59). Gast\u2194pSom "
  "spatial r=\u22120.15, far short of the passing same-tissue PDAC bar (Peng/Steele/Moncada/Lin, \u22120.53 to \u22120.68); no "
  "terminal Crest (module-high deciles mid-pseudotime). The manifold is organized by PDAC meta-programs "
  "(EMT/Hypoxia/Chromatin), not the developmental axis \u2192 the embryonic pattern is absent."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable \u2014 Gate 2 did not pass, so there is no Gast/pSom hub and no bifurcation to test. The branching-only "
  "04_correlation / 05_modules notebooks are not produced (\u00a76); the EMT-TF step is the final notebook (04)."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime / curve",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("PDAC (Hwang et al., 2022), 10x snRNA-seq \u2014 43 tumours / 224,988 cells (master scope); malignant only: "
 "64,538 nuclei \u2192 63,997 across 29 samples (\u2265100-cell floor; the multiplicative count gap is degenerate, sitting "
 "in the speck tail). Whole malignant manifold; three density lobes, not scoped.")
verdict=("The embryonic pattern does NOT reproduce. Gate 1 passes \u2014 one continuous, sample-integrated malignant "
 "manifold \u2014 but the developmental modules have no coherent geography (all at/below random-null level), no "
 "Gast\u2194pSom cross-repression axis (spatial r=\u22120.15 vs passing PDAC \u22120.53..\u22120.68), and no terminal Crest. The "
 "manifold is structured by PDAC meta-programs, not gastrulation/somitogenesis. EMT-TFs FOXC1 (blue) and ZEB1 "
 "(red) mark the manifold descriptively; canonical SNAI1/TWIST are below the detection floor. G1 GO / G2 NO-GO / "
 "G3 NA. Stopped at Gate 2 per \u00a76; 01\u201303 + expression(04) produced.")
params=[
 ("Sample threshold","\u2265100-cell floor (gap 2.67\u00d7 in speck tail \u2192 degenerate); 29/43 kept"),
 ("Overdispersed genes","1,645 (scFates find_overdispersed); no sc.pp.scale"),
 ("Integration","Harmony on sample, \u03b8=2 (iLISI 1.0\u21928.8; geography \u03b8-invariant)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 107 specks removed; 1 kNN comp"),
 ("Geometry","Non-trajectory (Gate 2 NO-GO); probe curve 2 tips/0 forks, no hub"),
 ("Module means (raw)","Gast \u22120.004 \u00b7 pSom \u22120.002 \u00b7 Crest +0.003 (geography decides)"),
 ("Root","curve tip 0 (max Gast+pSom\u2212Crest); ordering does not reproduce"),
 ("EMT-TFs shown","FOXC1 (3.6%) \u00b7 ZEB1 (15.7%); SNAI1/TWIST <0.1%; VIM excluded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Hwang 2022 PDAC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
