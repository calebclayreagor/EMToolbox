import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, RED, GREY
NB='/home/caleb/EMToolbox/mesencontext/claude/Breast/Bassez2021_Breast-4'
F='/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Bassez2021_Breast-4'
gates=[('Gate 1 — mixing & continuity', 'GO', '#1a9641', '41 samples intermixed on one continuous manifold; sample iLISI 6.1→9.1 (of 41) after Harmony θ=10; 363 island cells removed; cycling orthogonal to modules.'), ('Gate 2 — module geography', 'GO (non-branching)', '#1a9641', 'Single collapsed axis: pSom/Gast developmental origin → Crest terminal (pSom↔Crest r=−0.82). No Gast arm at any tip; PPT tree over-branches — not a bifurcation.'), ('Gate 3 — hub cross-repression', 'NA', '#888888', 'Non-branching geometry — no Gast/pSom competing arms to test.')]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),("Pseudotime",os.path.join(F,"manifold.pdf")),("Gastrulation",os.path.join(F,"Gast_signature.pdf")),("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),("Neural Crest",os.path.join(F,"Crest_signature.pdf")),("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset='Breast Cancer (Bassez et al., 2021), 10x — 41 samples, 65,519 malignant cells.'
verdict='Pattern reproduces as the non-branching case — one embryonic axis, pSom/Gast origin → Crest terminus. Gate 1 GO / Gate 2 GO / Gate 3 NA. Module means (raw): Gast −0.014 / pSom +0.022 / Crest −0.005. EMT-TFs PRRX1 (early/root) · ZEB2 (late/terminus).'
params=[('Sample threshold', '16 (gap-finding) → 41/42 kept'), ('Embedding', 'overdispersed 2498; n_pcs 20; Harmony θ=10 on sample; n_neighbors 30; UMAP spread 1.3; islands 363 removed'), ('Trajectory', 'scFates curve on diffusion rep, Nodes=15, λ=0.3, μ=100; fold-free (self-approach 2.56)'), ('Root', 'pSom/Gast-high tip (pt 0.28); Crest terminal (0.74)'), ('Annotation', 'Bassez2021 malignant meta-programs (EMT I dominant) + data-derived compartments'), ('Module means', 'Gast −0.014 / pSom +0.022 / Crest −0.005 (raw)'), ('EMT-TFs', 'PRRX1 (root) · ZEB2 (terminus)')]
build_summary(os.path.join(NB,"summary.pdf"),'Bassez 2021 Breast Cancer — analysis summary',gates,panels,dataset,verdict,params,run_label='run 5 of 6')
print("built")
