import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Hematologic/Caron2020_Hematologic-3"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Caron2020_Hematologic-3"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) integrates all 8 samples; sample-iLISI rises 1.0\u21924.1 of a 6.85 ceiling (plateau \u03b8 5\u201310). The "
  "manifold resolves into a cycling lobe and a low-cycling embryonic lobe; the cycling lobe is SCOPED OUT "
  "(25,788\u219219,800). On the scoped embryonic manifold samples and subtypes intermix on one connected component \u2014 GO."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "On the scoped manifold gastrulation is high at the root and falls along pseudotime (\u03c1=\u22120.65); Crest rises to a "
  "sharp inverse terminal gradient (decile t=0.97) opposing Gast (r=\u22120.74). Gast/pSom cross-repress (r=\u22120.55); pSom "
  "sits mid-axis (decile t=0.45). No resolution into two module-distinct arms \u2014 non-branching GO."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Non-branching topology: on the scoped embryonic manifold the PPT tree yields 2 tips / 0 forks (Gast-high root, "
  "Crest-high terminus) \u2014 no Gast/pSom co-expression hub. A clean fold-free curve (self-approach 3.0) is fit \u2014 no "
  "bifurcation to test \u2014 NA."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Pediatric B/T-cell acute lymphoblastic leukemia (Caron et al., 2020), 10x \u2014 19,800 embryonic blasts "
 "(cycling lobe scoped out) across 8 samples / 3 subtypes (ETV6-RUNX1, HHD, T-ALL). Non-branching Linear.")
verdict=("Pattern reproduces (non-branching / Linear) after scoping out the cycling lobe. A single continuous "
 "gastrulation \u2192 neural-crest embryonic axis on the 19,800-cell embryonic manifold, rooted at the Gast-high pole, "
 "with organised Gast/pSom cross-repression (r=\u22120.55) and a sharp terminal Crest gradient (decile t=0.97). The "
 "proliferation confound is resolved (pt\u2194proliferation \u03c1 +0.62\u2192+0.21). No bifurcation \u2014 Gate 3 NA.")
params=[
 ("Min-cell threshold","\u2265100 (smooth counts) \u2192 8/8 samples, 25,788 malignant cells"),
 ("Integration","Harmony \u03b8=10; n_pcs=20, n_neighbors=30, spread=1.3; 1,332 HVG"),
 ("Compartment scoping","cycling lobe (86.5% cycling) scoped out \u2192 19,800 embryonic cells"),
 ("Geometry","Linear (non-branching); scFates curve N=20, fold-free (3.0); 2 tips / 0 forks"),
 ("Root","curve tip at Gast-high, low-cycling origin (Gast/pSom early, Crest late)"),
 ("Modules recovered","Gast 66/81 \u00b7 pSom 77/98 \u00b7 Crest 93/104"),
 ("EMT-TFs","ZEB2 (early/root) \u2192 ZEB1 (late/terminus); SNAI1 also expressed"),
 ("Confound resolved","pt\u2194proliferation \u03c1 +0.62\u2192+0.21; continuity |corr(t,DC1)|=0.91"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Caron 2020 ALL \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
