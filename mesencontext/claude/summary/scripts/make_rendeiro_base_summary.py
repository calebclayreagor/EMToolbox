import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Rendeiro2020_Hematologic"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Rendeiro2020_Hematologic"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Harmony(\u03b8=10) integrates all 7 samples: same-sample neighbour fraction 0.97 \u2192 0.22, iLISI median 1.00 "
  "\u2192 4.95 of 7. 205 cells in 3 detached islands removed; one connected component. Read on the regenerated "
  "embedding + per-neighbourhood iLISI, not a scalar: samples intermix AND the manifold is continuous."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Non-branching case: a single (Gast)\u2192Crest developmental gradient. Gast opposes Crest in space (smoothed "
  "r=\u22120.75; pSom weakly opposes both). Along pseudotime Gast falls (\u03c1 \u22120.64) while Crest rises to a "
  "terminal tip (Crest-high decile pt=0.74) and pSom rises (\u03c1 +0.46). Joint Gast&Crest enrichment 0.27 "
  "(<1 = inverse gradient, not a co-expression hub)."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks; a PPT tree throws 6\u20137 "
  "spurious forks on this near-round cloud). No bifurcation, so the branching-only hub cross-repression test is "
  "not run (correlation / modules notebooks not produced, per spec)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("CLL peripheral blood (Rendeiro et al., 2020), 10x \u2014 18,452 malignant cells over 4 patients "
 "(7 longitudinal samples); single diffuse-cycling body (~44% cycling, cell-cycle-free axis).")
verdict=("Pattern reproduces in the non-branching form (Linear-pSom/Crest): one continuous gastrulation \u2192 "
 "neural-crest axis, Crest terminal. Gate 1 GO / Gate 2 GO / Gate 3 NA. CLL barely expresses EMT-TFs \u2014 only "
 "ZEB2 and ZEB1 clear the detection floor, both root-skewed (no terminus EMT-TF).")
params=[
 ("Sample threshold","geom-mean 284 (cliff 1012\u219280, ratio 12.6) \u2192 7/11 samples; 18,452 cells"),
 ("Overdispersed genes","528 (scFates find_overdispersed)"),
 ("Integration","Harmony on sample, \u03b8=10 (mixing plateau; patient-private CLL batch)"),
 ("Embedding","n_pcs=20, n_neighbors=30, spread=1.3; 205 cells / 3 islands removed"),
 ("Geometry","Non-branching scFates curve N=20 \u03bb=0.3 \u03bc=100; 2 tips/0 forks, SA 2.58; corr(x_lin,t)=0.92"),
 ("Root","tip 0 = Gast/pSom-high, Crest-low origin"),
 ("Module means (raw)","Gast \u22120.020 \u00b7 pSom +0.008 \u00b7 Crest +0.010 (Linear-pSom/Crest)"),
 ("Cell cycle","43.8% cycling, diffuse single lobe; axis cell-cycle-free"),
 ("EMT-TFs shown","ZEB2 + ZEB1, both root-skewed (no terminus EMT-TF); >3% gate"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Rendeiro 2020 CLL \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
