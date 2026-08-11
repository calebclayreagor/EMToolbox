import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Skin/Paulson2020_Skin"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Skin/Paulson2020_Skin"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (sample, \u03b8=10) collapses the 3 tumour samples onto ONE continuous component (100%, 0 detached); "
  "per-neighbourhood iLISI 1.0\u21922.25 (cross-patient 1.75/2); every sample traverses the shared embryonic axis "
  "end-to-end (|\u03c1(axis,Crest)|\u22480.87, span 100%) \u2014 mixed & continuous, not a per-patient archipelago."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast & pSom co-vary along one axis (smoothed r=+0.38; joint-high enrichment 1.22 \u2014 no two-arm divergence); Crest "
  "is an inverse TERMINAL gradient (pSom\u2194Crest r=\u22120.70; Crest-high decile mean pt=0.96) peaking at the terminus, not "
  "a Gast arm \u2014 no inversion flag."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Branching-only. No diverging Gast/pSom hub (single fold-free curve, 0 forks) \u2014 no bifurcation to test, so Gate 3 "
  "does not apply."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Merkel cell carcinoma (neuroendocrine skin) (Paulson et al., 2020), 10x \u2014 12,124 malignant cells (3 "
 "tumours, 2 patients); non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces (non-branching): a single continuous gastrulation/somitogenesis \u2192 terminal neural-crest "
 "axis, rooted at the Gast/pSom-high origin. Gate 1 GO / Gate 2 GO / Gate 3 NA. EMT-TFs ZEB1 (body) \u00b7 ZEB2 "
 "(terminus), both origin/body-loaded; only factors >3% floor.")
params=[
 ("Min-cell threshold","\u2265100 floor (smallest sample 2,031); 3/3 kept, 12,124 cells"),
 ("Integration","Harmony on sample \u03b8=10 (swept 2/5/10); one continuous component"),
 ("n_pcs / spread","20 / 1.3 (PC1=0.23 CNV-dominated)"),
 ("Overdispersed genes","2,075 (scFates find_overdispersed)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100 (2 tips, 0 forks, SA 2.83)"),
 ("Root","tip 2 = Gast/pSom-high, Crest-low (Crest is late)"),
 ("Module means (raw)","Gast +0.037 \u00b7 pSom +0.051 \u00b7 Crest \u22120.006"),
 ("EMT-TFs shown","ZEB1 (14.4%) \u00b7 ZEB2 (19.1%); both origin/body-loaded"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Paulson 2020 Merkel cell carcinoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
