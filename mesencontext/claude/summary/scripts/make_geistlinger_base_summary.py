import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Ovarian/Geistlinger2020_Ovarian"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Ovarian/Geistlinger2020_Ovarian"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "5 patients share ONE continuous manifold (single kNN component; iLISI 1.87/5, limited by 54% T59 dominance). "
  "\u03b8=5 resolves a T59-only under-integration lobe seen at \u03b8=2. Judged on the embedding."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Embryonic pattern present, non-branching: pSom\u2194Crest single inverse axis (r=\u22120.95 smoothed); Gast co-varies "
  "with pSom (+0.61), both oppose Crest. Crest is the terminal gradient (crest-high decile at pseudotime 0.98). "
  "Not a proliferation artifact \u2014 pSom\u2194Crest holds in non-cycling cells (r=\u22120.62). Crest at the terminus, "
  "not the Gast arm \u2014 no flag."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Branching-only. No bifurcation (fold-free 2-tip curve; PPT branch-node counts unstable 3\u20138, no reproducible "
  "fork; Gast\u22a5pSom, r\u22480) \u2014 no hub cross-repression test. Non-branching case, per \u00a71\u20132."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("High-Grade Serous Ovarian Carcinoma (Geistlinger et al., 2020), 10x \u2014 5,914 malignant cells "
 "(5 patients). Harmony integration on sample (\u03b8=5), principal-curve trajectory (scFates) on the whole manifold.")
verdict=("The embryonic-program pattern REPRODUCES as the non-branching case: one continuous "
 "gastrulation/somitogenesis \u2192 neural-crest developmental axis, rooted at the Gast/pSom-high origin, with Crest "
 "an inverse terminal gradient \u2014 a strict linear subset of the Puram branching hub. Gate 1 GO, Gate 2 GO "
 "(non-branching), Gate 3 NA. No hub / no cross-repression (branching-only).")
params=[
 ("Min-cell threshold","\u2265100 floor \u2192 5/5 kept (gap at head 3180\u21921298; precedent floor)"),
 ("n_pcs / integration","20 PCs \u00b7 Harmony \u03b8=5 (merges T59 under-integration lobe)"),
 ("Island removal","radius-CC, 17-cell speck (740-cell \u03b8=2 lobe was under-integration, kept)"),
 ("Geometry","Non-branching \u00b7 scFates curve (fold-free 2-tip, self-approach 2.97)"),
 ("Root","Gast/pSom-high tip (Crest-low); Crest developmentally late"),
 ("Subtype annotation","TCGA + 3CA MPs + Leiden (~85% DIF, continuous gradient)"),
 ("EMT-TFs shown","PRRX2 \u00b7 ZEB1 (both root/mesenchymal-enriched, opposite Crest)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Geistlinger 2020 HGSOC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
