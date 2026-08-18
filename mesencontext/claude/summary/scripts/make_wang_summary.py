import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Brain/Wang2019_Brain-7"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Brain/Wang2019_Brain-7"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "7/10 samples (\u2265237 cells; mult-gap 396\u2192143) on one connected component; sample iLISI 2.60/7 across "
  "\u03b8=5\u201320. Cell-cycle & metaprograms scattered \u2014 no per-sample archipelago."),
 ("Gate 2 — module geography","NO-GO",RED,
  "RAW module scores are ~85% noise (spatial-structure ratio 0.12\u20130.15 vs 0.23\u20130.39 in the Neftel GBM GO "
  "ref) and near-flat across all 3 lobes. Under a NEUTRAL control all three modules co-vary POSITIVELY "
  "(Gast-pSom +0.62, Crest-Gast +0.47, Crest-pSom +0.37) \u2014 no Crest opposition. The union-pool "
  "pSom\u2194Crest \u22120.61 was a control-pool artifact amplified by smoothing. No hub/arms."),
 ("Gate 3 — hub cross-repression","NA",GREY,
  "No embryonic geometry present \u2192 no trajectory forced, no bifurcation to test."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Glioblastoma (Wang et al., 2019), 10x \u2014 10 samples; 9,916 malignant raw \u2192 9,650 after \u2265237-cell "
 "threshold (7/10 samples) \u2192 9,634 after island removal (16 cells, 1 detached speck).")
verdict=("\u2717 Pattern does NOT reproduce. The malignant manifold integrates and is continuous (Gate 1 GO), but the "
 "embryonic module geography is absent: raw Gast/pSom/Crest scores are noise-dominated and near-uniform, with no "
 "hub, no arms, and no Crest opposition once the union-pool scoring artifact is removed. Honest Gate 2 NO-GO \u2014 "
 "no trajectory forced.")
params=[
 ("Min cells/sample","\u2265237 (mult-gap 396\u2192143; 7/10)"),
 ("Integration","Harmony \u03b8=10; PCA20; spread=1.3"),
 ("Embedding","native X_umap (no re-embedding)"),
 ("Gate 2 test","raw scores + neutral-control null"),
 ("Scope","whole manifold (no embryonic lobe)"),
 ("EMT-TFs","ZEB1, ZEB2 (detectable; no order)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Wang 2019 GBM \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
