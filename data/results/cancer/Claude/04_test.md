# CCCA Autonomous-Run Testing Log

Each attempt on the **testing** datasets is a fully-autonomous run — the analysis is driven by the
spec files alone, with no expert steering. A fresh-context auditor then reviews the run, guided by the
expert. One entry per attempt below records the decisive points only; read alongside the three spec
files. Datasets are sectioned below, attempts ordered within each.

---

## Chen 2020 (NPC, 10x)

Nasopharyngeal carcinoma, 10x, ~3.7k malignant cells — head-and-neck, same tissue family as the
Puram/Kürten ground-truth runs.

### Attempt 1 · Gate 1 NO-GO

- **Fail — `n_pcs=6` under-powers the manifold.** Chord-elbow over-cut the inherited 40; too few PCs force
  a patient-segregated read, so the NO-GO is likely an embedding artifact. (Elbow biases low here; the
  Puram-40 / Kürten-20 precedents are the scale to sanity-check against.)
- **Fail — `summary.pdf` wrong layout.** Verdict-prose + stacked step-PDFs, not the reference gate-ledger →
  figure-grid one-pager.
- **Held.** Spec re-read at each gate/deliverable; threshold, theta sweep, EMT-TF panel, renumbering all sound.
- **Watch.** Gate call stayed metric-led — embedding read as corroboration, not lead.

### Attempt 2 · Gate 1 NO-GO

- **Fail — integration strength too low.** Settled `theta=2` and swept only `theta 0→3`, dismissing
  `theta=3` as over-integration without a null test to justify the cutoff. The 10x precedent (Kürten)
  reached `theta=10`, so stronger integration was left untested before the NO-GO. The sweep covered `n_pcs`
  well (attempt-1's issue) but not integration strength.
- **Fail — figure deliverables diverge from the reference.** `samples.pdf` is a bespoke 3-panel diagnostic
  (patient UMAP + cell-cycle + `n_pcs×theta` sweep) built to argue the audit narrative, not the reference's
  single sample-colored manifold UMAP; and `summary.pdf` was written to the figures root, not the notebook
  dir where the reference keeps it.
- **Held.** Both attempt-1 defects fixed: `n_pcs=20` (matches the Kürten/Puram scale) and the `summary.pdf`
  layout now follows the reference. Gate 1 led with the embedding. Spec re-read/certified throughout.

### Attempt 3 · Gate 1 GO / Gate 2 NO-GO / Gate 3 NA

- **Fail — trajectory mis-specified.** Fit a branching `tree` on a manifold it had itself called
  non-branching (should be a `curve`), and rooted at a proliferation state rather than the developmental
  origin the signatures imply — the same root error flagged on Kürten.
- **Fail — signature scores not smoothed.** Read geography and the Gast/pSom correlation from raw per-cell
  scores; the Kürten 10x reference graph-smooths the scores (knn-connectivity averaging in 02_manifold)
  before reading geography, so the raw read is noise-dominated here.
- **Fail — EMT-TF panel degenerate.** The display cutoff was unset, so the color scale is outlier-dominated
  and washed out; and VIM was shown as an EMT-TF, but vimentin is a mesenchymal marker, not a transcription
  factor.
- **Fail — island removal incomplete.** Its metric was degenerate, so detached islands were left in the
  manifold and Gate 1 was still called continuous.
- **Held.** Deliverables now correct in format and location. Traced the two prior Gate-1 NO-GO calls to an
  `sc.pp.scale` step before PCA absent from the reference protocol — a correct diagnosis, and why the chain
  finally ran past Gate 1. Spec re-read/certified throughout.

### Attempt 4 · Stopped pre-analysis (no certification)

- **Fail — no certification, immediate drift.** Never certified the binding re-read (it had slipped behind a
  context fold); drifted into building notebook-execution infrastructure and ran code before any gate.
  Stopped pre-analysis, then cleaned up correctly.

### Attempt 5 · Gate 1 GO / Gate 2 NO-GO / Gate 3 NA

- **Fail — linear curve fit to a visibly tree-shaped manifold.** Called the clearly Y-shaped manifold
  "robustly non-branching" on a PPT metric (0 branch nodes across 12 param combos) and fit one curve through
  it. The inverse of attempt 3's tree-on-a-strip; same cause — topology read from the metric, not the embedding.
- **Fail — figure deliverables still diverge from the reference layouts, despite the spec re-read.** Re-reading
  the spec prose did not become a check of the outputs against the binding reference figures themselves.
- **Fail — Gate 2 built toward GO, then reversed to NO-GO on a scalar comparison.** The module geography was
  legible in the signature embeddings; the call was driven by the scalar comparison instead.
- **Held.** Binding re-read certified at start and at the gate (attempt-4 lesson landed); deliverables in the
  correct locations; no `sc.pp.scale`; `n_pcs≈19`, theta swept.

### Attempt 6 · Gate 1 GO / Gate 2 GO (non-branching) / Gate 3 NA

- **Fail — folded curve, never caught by any post-hoc visualization.** The committed curve W-folds back
  through the cloud; `manifold.pdf` draws pseudotime color but not the curve edges, so topology was judged on
  signature↔pseudotime correlations, blind to the fold (the Kürten §4 failure mode). Surfaced only when the
  expert asked for a curve render in the debrief.
- **Fail — figure deliverables again diverge; format, content, and tidiness are BINDING.** manifold/samples
  retitled with milestone and legend labels overlaid on the cloud, not the reference's single panel + external
  colorbar; an extra `gate2_diagnostics.pdf` left in the figures dir, outside the §6 set (scratch, as in attempt 2).
- **Held.** Certified the binding re-read; reached Gate 2 GO (non-branching) matching Kürten; overturned its
  provisional tree→curve on biology (Gast/pSom co-vary, Crest inverse), not geometry.

### Attempt 7 · Gate 1 GO / Gate 2 GO (non-branching) / Gate 3 NA

- **Held — science lands (first fully-autonomous success).** Correct non-branching read: a fold-free curve
  rooted at the Gast/pSom-high developmental origin, Gate 2 GO on biology, Gate 3 NA. The Kürten lessons
  landed — curve not tree, root at origin, fold checked, no re-embedding.
- **Fail — figure style diverges from the binding reference.** Panels square, not the house `(3.5,1.5)`
  linear-trajectory aspect; signature UMAPs plot graph-smoothed scores where the reference shows raw (smoothing
  aids the analysis but misleads as a deliverable); EMT-TF marker size doesn't match the other panels.
- **Fail — `summary.pdf` clips text; tidiness not fully observed.** Verdict and Geometry lines run past the
  page box, cut off mid-sentence.
- **Watch — one residual island.** A P03-dominated detached lobe survives island removal (39-cell speck
  stripped, not this); not fatal to the continuous-manifold call.

---

## Bischoff 2021 (LUAD, 10x)

Lung adenocarcinoma, 10x, ~13.4k malignant cells — new biology versus the Puram/Kürten/Chen
head-and-neck runs.

### Attempt 1 · Gate 1 GO (contested) / Gate 2 GO (non-branching) / Gate 3 NA

- **Fail — pre-Gate-1 error: two-blob manifold passed as continuous.** The manifold splits into two
  blobs. The agent saw the gap but dismissed it as a UMAP artifact because the kNN graph is one
  component — deciding a visual gate on a connectivity scalar. The real cause was never settled: either
  under-integration (a higher θ, rejected for smoothing the gap, may merge the blobs) or a scoping
  failure (identify each lobe's biology and fit the trajectory only on the lobe reproducing the
  reference — the Kürten evaluation's lobe-identity fork).
- **Fail — `summary.pdf` rule strikes through the title.** The header underline crosses the title
  descenders (and the Gate-3 "exclusivity" line); otherwise the deliverable matches the reference exactly.
- **Held — deliverables land.** Correct §6 set in the correct locations, no scratch, house `(3.5,1.5)`
  manifold aspect, raw signature scores shown. Binding re-read certified at start and each gate.

### Attempt 2 · Gate 1 NO-GO / Gate 2 NA / Gate 3 NA

- **Fail — un-integratable call unsupported by its own sweep.** Gate 1 NO-GO ("not continuous") rests on a
  plateauing diff-sample kNN scalar, yet the sweep's own 16 PC / θ=10 panel shows the gap closing into one
  continuous mass. The mirror of attempt 1 — scalar over embedding — on the opposite gate.
- **Fail — sweep mis-centered.** PCs swept only 12/16/20, and <20 is not robust (precedents ran 20/40), so
  the grid sits below the robust range. The one panel that did converge is its highest PC × highest θ corner,
  so a properly-centered sweep was never run to confirm it.
- **Fail — `summary.pdf` layout regressed from the reference.** Attempt 1 matched the reference one-pager;
  this run redesigned it into a bespoke layout (colored gate chips, new title, an extra lobe-fork block).

### Attempt 3 · Gate 1 GO / Gate 2 GO (non-branching) / Gate 3 NA

- **Held — science lands (first Bischoff success).** Correct non-branching call, and it settles the Gate-1
  question both prior attempts got wrong: the two density lobes are poles of one continuous manifold, shown on
  both the embedding and the sweep. Deliverables land — correct §6 set, no scratch, reference layout restored.
- **Fail — `summary.pdf` step figures low-resolution.** The six embedded panels were saved at low DPI, so
  their in-panel text blurs against the sharp vector text of the summary itself.

---

## Sun 2021 (HCC, 10x)

Hepatocellular carcinoma, 10x, ~2.3k malignant cells — new biology versus the Puram/Kürten/Chen/Bischoff
head-and-neck and lung runs.

### Attempt 1 · Gate 1 GO / Gate 2 GO (non-branching) / Gate 3 NA

- **Held — science lands (first liver success).** Correct non-branching read on new biology: one continuous
  gastrulation→neural-crest axis rooted at the Gast-high pole. Checked each lobe's biology before certifying
  (the Kürten fork), kept the full manifold, and self-caught three reviewer findings before re-running.
- **Fail — EMT-TF panel in the wrong plotting style.** A continuous single-gene colormap, not the reference
  categorical overlay of thresholded expressers on a grey manifold; the overlay branch was coded but bypassed.
- **Fail — `summary.pdf` redesigned, not the reference layout.** Bespoke one-pager,
  not the certified "GO/NO-GO GATES → STEP FIGURES → Parameter choices" format. Build
  scratch also left in the notebook dir.
- **BINDING — verify deliverables against the reference visually.** Compare every deliverable to the
  reference output directly, not spec prose alone: each panel must match the reference plotting style, and
  `summary.pdf` its exact layout. Correct science with divergent panels or layout is not a pass.
