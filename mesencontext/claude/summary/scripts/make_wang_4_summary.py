import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, RED, GREY
NB='/home/caleb/EMToolbox/mesencontext/claude/Brain/Wang2019_Brain-4'
F='/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Wang2019_Brain-4'
gates=[('Gate 1 — mixing & continuity', 'GO', '#1a9641', '9,916 malignant → 9,650 (7/10 samples, ≥237) → 9,634 on one connected component. Sample iLISI rose 1.0→2.6/7 under Harmony (plateau by θ=10); one 16-cell island removed.'), ('Gate 2 — module geography', 'GO (non-branching)', '#1a9641', 'Shared Gast/pSom gradient (r=+0.16, co-vary) with Crest an inverse terminal readout (r=−0.49 vs Gast, −0.87 vs pSom). Curve fold-free (0 forks); Crest-high decile at pseudotime 0.85.'), ('Gate 3 — hub cross-repression', 'NA', '#888888', 'Gast/pSom co-vary (not compete) — single collapsed axis, no bifurcation to test.')]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),("Pseudotime",os.path.join(F,"manifold.pdf")),("Gastrulation",os.path.join(F,"Gast_signature.pdf")),("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),("Neural Crest",os.path.join(F,"Crest_signature.pdf")),("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset='Glioblastoma (Wang et al., 2019); 10x, 10 samples; 9,916 malignant raw → 9,634 final after threshold + island removal. IDH-wildtype primary GBM (single 10x leaf).'
verdict='Pattern reproduces as a non-branching embryonic axis: pSom-high origin → Crest-high terminus (pSom ρ=−0.62, Crest ρ=+0.49 along pseudotime; Gast flat, ρ=−0.06), continuity confirmed on a diffusion embedding independent of the fitted UMAP (r=0.98). Linear (single collapsed axis; GBM states NPC/OPC → AC/MES span it). Not branching. Gate 1 GO / Gate 2 GO / Gate 3 NA. EMT-TFs ZEB1 (early/root) → PRRX1 (late).'
params=[('Min cells/sample', '237 (mult-gap 396→143; 7/10)'), ('Integration', 'Harmony θ=10; PCA20; spread=1.3'), ('Geometry', 'Linear / non-branching (curve)'), ('Trajectory', 'scFates curve N=20 λ=0.3 μ=100'), ('Root node', 'pSom-high / Crest-low tip'), ('EMT-TFs', 'ZEB1 (early/root) → PRRX1 (late)')]
build_summary(os.path.join(NB,"summary.pdf"),'Wang 2019 Glioblastoma — analysis summary',gates,panels,dataset,verdict,params,run_label='run 5 of 8')
print("built")
