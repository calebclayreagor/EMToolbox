import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Steen2021_Hematologic"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Steen2021_Hematologic"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Whole malignant manifold (2,478 cells, 3 tumours) is one connected component (0 islands). Harmony (\u03b8=10) lifts "
  "per-neighbourhood mixing from iLISI 1.00\u21921.88 of 3 samples; the regenerated embedding shows one continuous cloud "
  "with samples intermixed \u2014 no per-patient archipelago."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "A distinct proliferative lobe (513 cells, 95.5% cycling) confounds Gastrulation on the whole manifold "
  "(Gast\u2194cycling r=\u22120.74). Scoping to the low-cycling lobe restores the reference relationships: Gast/pSom co-vary "
  "(r=+0.6) and both oppose Crest (Crest\u2194Gast r=\u22120.9). One (Gast/pSom)\u2192Crest axis \u2014 Gast \u03c1=\u22120.94, pSom \u03c1=\u22120.73 "
  "decline; Crest rises to a terminal tip (\u03c1=+0.87, Crest-high decile pt 0.95; joint pSom&Crest enrichment 0.26<1). "
  "Single axis, no bifurcation \u2014 GO."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Not applicable: the manifold is non-branching (principal curve, 2 tips / 0 forks, fold-free self-approach 2.9 "
  "across Nodes=15/20/30). With no Gast/pSom hub there is no bifurcation to test."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Diffuse large B-cell lymphoma (Steen et al., 2021), 10x \u2014 2,522 malignant cells \u2192 2,478 after threshold "
 "(3 tumours) \u2192 1,963 scoped to the low-cycling developmental lobe. Non-branching Linear-pSom/Crest.")
verdict=("Pattern reproduces (non-branching). Malignant DLBCL cells recapitulate a single gastrulation/somitogenesis "
 "\u2192 neural-crest developmental axis once the proliferative compartment (513 cells, 95.5% cycling) is scoped out. "
 "Gate 1 GO, Gate 2 GO, Gate 3 NA (no bifurcation). EMT-TFs ZEB2 (early/root) \u2192 ZEB1 (late/terminus).")
params=[
 ("Min-cell threshold","127 (geo-mean of 8.4\u00d7 cliff 371\u219244); drops thin DLBCL111B \u2192 3 tumours, 2,478 cells"),
 ("Integration","Harmony on sample \u03b8=10 (mixing floor by \u03b8=5); n_pcs=20, spread=1.3"),
 ("Scope","low-cycling Leiden lobe (res=0.15): 1,963 cells; excludes 95.5%-cycling lobe"),
 ("Geometry / root","principal curve (ElPiGraph, non-branching); root Gast/pSom-high tip; Linear-pSom/Crest"),
 ("EMT-TFs","ZEB2 (61%) & ZEB1 (26%) \u2014 only factors above 3% floor; rest near-silent in B-cell tumour"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Steen 2021 DLBCL \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
