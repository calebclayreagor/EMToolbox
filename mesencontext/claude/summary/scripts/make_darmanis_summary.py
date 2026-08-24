import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Brain/Darmanis2017_Brain-1"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Darmanis2017_Brain-1"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "4 patients intermix on one continuous manifold (iLISI 2.68 / 4 vs 1.16 pre-Harmony; \u03b8=10, 20 PCs); radius-graph "
  "finds 0 detached islands; all 3 sub-lobes reproduce the embryonic relationships."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast & pSom co-vary spatially (r = +0.72); Crest is the inverse terminal gradient (r = \u22120.92 vs Gast, \u22120.59 vs "
  "pSom; Crest-high decile at pseudotime 0.98). Single (Gast/pSom)\u2192Crest axis \u2014 non-branching case, passes, no "
  "bifurcation."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Non-branching manifold: a principal tree shows no Gast-vs-pSom arm divergence (all tips pSom-high, Gast-low), so "
  "there is no hub to test. Gate 3 is branching-only \u2014 NA."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Glioblastoma (Darmanis et al., 2017), SmartSeq2 full-length scRNA-seq \u2014 1,091 malignant cells across 4 "
 "patients. Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces as a single non-branching embryonic axis: a Gast/pSom-high origin resolving into a "
 "neural-crest-high terminus. The curve is fit on the integrated PCA representation so the axis reaches the Crest "
 "pole, not the pSom edge of the 2-D UMAP. Geometry Linear-pSom/Crest (pSom the globally strongest module). "
 "EMT-TFs FOXC1 (early/root) \u2192 PRRX1 (late/terminus).")
params=[
 ("Sample threshold","all 4 kept (\u2265100-cell floor; no clean low-end gap)"),
 ("HVG selection","scanpy Seurat top-2000 (pagoda2 overdispersion degenerates on pre-log TPM)"),
 ("Integration","Harmony on sample \u03b8=10, 20 PCs (iLISI plateaus after \u03b8=5; 1.16\u21922.68/4)"),
 ("Trajectory","ElPiGraph curve on X_pca_harmony (2 tips, 0 forks, 2.97); non-branching"),
 ("Root","curve tip max Gast+pSom\u2212Crest (developmental origin; neural crest late)"),
 ("Geometry","Linear-pSom/Crest (Gast \u03bc +0.010 \u00b7 pSom \u03bc +0.099 \u00b7 Crest \u03bc +0.041)"),
 ("EMT-TFs","FOXC1 (early/root) \u2192 PRRX1 (late/terminus); 10-factor panel"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Darmanis 2017 GBM \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
