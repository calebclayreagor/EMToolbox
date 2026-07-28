# CCCA Autonomous-Run Testing Log — Chen 2020 (NPC, 10x)

Repeated fully-autonomous attempts on the **Chen 2020** dataset (nasopharyngeal carcinoma, 10x, ~3.7k
malignant cells). Each attempt runs without expert steering and is reviewed by a fresh-context auditor.
One entry per attempt below — decisive points only. Read alongside the three spec files.

---

## Attempt 1 · Gate 1 NO-GO

- **Fail — `n_pcs=6` under-powers the manifold.** Chord-elbow over-cut the inherited 40; too few PCs force
  a patient-segregated read, so the NO-GO is likely an embedding artifact. (Elbow biases low here; the
  Puram-40 / Kürten-20 precedents are the scale to sanity-check against.)
- **Fail — `summary.pdf` wrong layout.** Verdict-prose + stacked step-PDFs, not the reference gate-ledger →
  figure-grid one-pager.
- **Held.** Spec re-read at each gate/deliverable; threshold, theta sweep, EMT-TF panel, renumbering all sound.
- **Watch.** Gate call stayed metric-led — embedding read as corroboration, not lead.

## Attempt 2 · Gate 1 NO-GO

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

## Attempt 3 · Gate 1 GO / Gate 2 NO-GO / Gate 3 NA

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

## Attempt 4 · Stopped pre-analysis (no certification)

- **Fail — no certification, immediate drift.** Never certified the binding re-read (it had slipped behind a
  context fold); drifted into building notebook-execution infrastructure and ran code before any gate.
  Stopped pre-analysis, then cleaned up correctly.
