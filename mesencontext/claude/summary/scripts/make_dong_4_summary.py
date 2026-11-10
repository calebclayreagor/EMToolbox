import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, RED, GREY
NB='/home/caleb/EMToolbox/mesencontext/claude/Prostate/Dong2020_Prostate-4'
F='/home/caleb/EMToolbox/figures/mesencontext/claude/Prostate/Dong2020_Prostate-4'
gates=[('Gate 1 — mixing & continuity', 'GO', '#1a9641', 'Samples intermix per-neighbourhood (iLISI 1.93 of 4 at θ=10, up from 1.0 pre-Harmony) on ONE connected component (kNN + independent UMAP radius graph); 9,698 malignant cells, no islands removed.'), ('Gate 2 — module geography', 'GO (non-branching)', '#1a9641', 'Shared Gast/pSom gradient (smoothed r=+0.90, co-vary) with Crest an inverse terminal readout (r=−0.39 / −0.53). Curve fold-free (0 forks); Crest-high decile at pseudotime 0.98.'), ('Gate 3 — hub cross-repression', 'NA', '#888888', 'Gast/pSom co-vary (not compete) → single collapsed axis, no bifurcation to test.')]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),("Pseudotime",os.path.join(F,"manifold.pdf")),("Gastrulation",os.path.join(F,"Gast_signature.pdf")),("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),("Neural Crest",os.path.join(F,"Crest_signature.pdf")),("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset='Prostate cancer (Dong et al., 2020), 10x — 4 malignant-bearing patients (5 adeno + 1 small-cell NEPC by clinical histology). 9,698 malignant cells; luminal & neuroendocrine states are poles of one continuous manifold.'
verdict='Pattern reproduces as a non-branching embryonic axis: Gast/pSom-high origin → Crest-high terminus; developmental order pSom ρ=−0.71, Crest ρ=+0.79 along pseudotime, checked off a diffusion embedding independent of the fitted UMAP. Linear geometry (pSom globally strongest module). Gate 1 GO / Gate 2 GO / Gate 3 NA. EMT-TFs SOX9 (root) → TWIST1 (terminus).'
params=[('Min cells/sample', '≥100 (no low-count gap; 4/4 kept)'), ('Integration', 'Harmony θ=10; PCA20; spread=1.3'), ('Scope', 'whole manifold (luminal+NE)'), ('Trajectory', 'scFates curve N=20 λ=0.3 μ=100'), ('Root node', 'Gast/pSom-high tip'), ('EMT-TFs', 'SOX9 (root) → TWIST1 (terminus)')]
build_summary(os.path.join(NB,"summary.pdf"),'Dong 2020 Prostate — analysis summary',gates,panels,dataset,verdict,params,run_label='run 5 of 6')
print("built")
