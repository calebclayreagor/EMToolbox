import sys, os
sys.path.insert(0,"/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/MesenCoder/cancer/vertebrate/CCCA/Claude/Neuroendocrine/Dong2020_Neuroendocrine"
F ="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Neuroendocrine/Dong2020_Neuroendocrine"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "13/13 tumours (\u2265100 cells) intermix on one continuous manifold (1 kNN component; iLISI source 1.00\u21921.38, sample "
  "3.38 of 13). The two capture groups mix through the body; the small near-pure pockets are the two largest "
  "MYCN-amplified tumours \u2014 genuine CNV states, not a per-patient archipelago."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single pSom\u2192Crest axis: pSom high across the body, Crest anti-correlated (r=\u22120.65) as an inverse gradient (joint "
  "pSom&Crest-high enrichment 0.38); Gast marks the origin, declining along pseudotime (\u03c1=\u22120.63). No hub-and-spoke "
  "divergence \u2014 gradient, not hub."),
 ("Gate 3 — cross-repression","NA",GREY,
  "Non-branching: PPT forks scale with node count and the curve is 2-tip / 0-fork, so there is no bifurcation and no "
  "Mixed-type hub to test."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Neuroblastoma (Dong et al., 2020), 10x \u2014 13 tumours / 55,190 cells; malignant only: 47,384 cells (all 13 "
 "tumours \u2265100) enter preprocessing. Captured in two panels; the joint manifold is built on the 12,113-gene shared "
 "panel so all tumours share one feature space.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. The neuroblastoma malignant manifold is "
 "one continuous gastrulation/somitogenesis \u2192 neural-crest-inverse axis (low-cycling origin \u2192 proliferative "
 "terminus), matching developmental order; it lacks Puram\u2019s hub-and-spoke bifurcation, so Gate 3 has no hub. The "
 "curve tracks proliferation (pt\u2194cycling \u03c1=+0.80), but the modules are cell-cycle-free (Gast 0/81, Crest 0/104 "
 "cc-genes) and pSom\u2194Crest anti-correlation survives in non-cycling cells (r=\u22120.60) \u2014 developmental, so the whole "
 "manifold is kept (cycling co-variation a caveat). EMT-TFs PRRX2 (early) \u2192 FOXC1 (late, \u03c1=+0.15).")
params=[
 ("Min cells","\u2265100 floor (13/13; gap 1.06\u00d7)"),
 ("Integration","Harmony \u03b8=10; 20 PCs; spread=1.3"),
 ("Scope","whole manifold (no scoping)"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("Root node","tip 0 = Gast/pSom-high, Crest-low"),
 ("Compartments","Body 35,196 / Cycling 12,188 (modules cc-free)"),
 ("Geometry","Linear (non-branching); 2 tips / 0 forks"),
 ("EMT-TFs","PRRX2 (early) \u2192 FOXC1 (late); Group2 whole-transcriptome"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Dong 2020 neuroblastoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
