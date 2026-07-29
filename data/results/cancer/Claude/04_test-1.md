# CCCA Autonomous-Run Testing Log — Bischoff 2021 (LUAD, 10x)

Fully-autonomous run on the **Bischoff 2021** dataset (lung adenocarcinoma, 10x, ~13.4k malignant
cells) — new biology versus the Puram/Kürten/Chen head-and-neck runs. No expert steering; reviewed
by a fresh-context auditor. One entry per attempt below — decisive points only. Read alongside the
three spec files.

---

## Attempt 1 · Gate 1 GO (contested) / Gate 2 GO (non-branching) / Gate 3 NA

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

---

## Attempt 2 · Gate 1 NO-GO / Gate 2 NA / Gate 3 NA

- **Fail — un-integratable call unsupported by its own sweep.** Gate 1 NO-GO ("not continuous") rests on a
  plateauing diff-sample kNN scalar, yet the sweep's own 16 PC / θ=10 panel shows the gap closing into one
  continuous mass. The mirror of attempt 1 — scalar over embedding — on the opposite gate.
- **Fail — sweep mis-centered.** PCs swept only 12/16/20, and <20 is not robust (precedents ran 20/40), so
  the grid sits below the robust range. The one panel that did converge is its highest PC × highest θ corner,
  so a properly-centered sweep was never run to confirm it.
- **Fail — `summary.pdf` layout regressed from the reference.** Attempt 1 matched the reference one-pager;
  this run redesigned it into a bespoke layout (colored gate chips, new title, an extra lobe-fork block).
