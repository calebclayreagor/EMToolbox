# CCCA Evaluation Audit — Kürten 2021 HNSCC · Gate 1 / continuity

First unseen dataset. Same HNSCC cancer type as the anchor, but 10x (not SmartSeq2) and ~11k malignant cells
(≈4.6× Puram). The agent reached step 06; log reads **G1 PASS, G2 PASS, G3 NO-GO**. This audit ignores the
downstream gates and asks one thing: **was the Gate 1 GO defensible on the *continuity* leg?** It was not.

**Verdict.** Gate 1 should have been **NO-GO**. The manifold is not one continuum — it is a set of per-patient
territories with one near-detached lobe (HN01, 22% of cells). The GO stands on a connectivity test that *cannot
fail* on dense droplet data, and on a mixing delta that clears the PASS rule while still leaving donor
segregation ~3.4× above the mixed-null floor. The agent later retracted the *mixing* leg under questioning but
never revisited *continuity*, which is the leg an expert reads off the embedding directly.

## Why Gate 1 was a GO

Gate 1 bundles two claims — **mixing** (are donors blended?) and **continuity** (one connected manifold, no
private island?). The coded verdict (NB01 cell 14) is `PASS if harm < raw − 0.1`: the entire boolean rides on the
mixing delta. Continuity enters only as a side print — "one dominant component" from the island-removal graph.

- **Mixing.** Same-sample kNN fraction 0.888 (raw PCA) → **0.543** (Harmony); Δ = 0.345 > 0.1 → PASS. The summary
  calls 0.543 "near the mixed-null floor." It is not: the same-group floor is ≈0.16, so 0.543 sits **~3.4× above**
  it. Harmony *reduced* segregation without removing it.
- **Continuity.** NB01 cell 10 builds a radius graph at **6× the median NN distance**, takes connected
  components, prints "removed 3 cells in 2 detached islands." One dominant component → continuity asserted.

The continuity instrument is **degenerate by construction**. Re-running it across radii on the saved manifold:
the graph collapses to a single component *only* at the agent's 6× setting; the same test shatters into **31
components at 3×** and **167 at 2×** (largest holds just 50% of cells). A radius that admits every cell into one
blob cannot distinguish a continuous gradient from discrete patient clouds joined by a handful of edges — it
answers "is the kNN graph connected?", which on 11k dense droplets is always yes, not "is there a transcriptional
continuum across donors?", which is the biological question. This is a **C3 failure** (the "noise detaches
cleanly" premise, flagged as a scale risk in calibration, breaks exactly as predicted on the first dense 10x set)
compounded by a **C1/C2 failure** (the 6× radius is an inherited constant, never re-derived or shown to
discriminate here).

## What the evidence actually shows

Gap-sensitive diagnostics on the delivered manifold (`X_pca_harmony`, n_pcs=20 — the agent's own graph):

- **Territorial, not continuous.** Cross-patient kNN edge fraction = **0.38** vs **0.84** expected under full
  mixing (ratio 0.45). Patients occupy distinct lobes; 46% of the UMAP bounding box is empty space.
- **A near-detached lobe.** PAGA inter-patient connectivity puts **HN01 (2,457 cells, 22% of the data)** at
  0.01–0.17 to every donor except HN07 — effectively its own island — while HN12/HN13/HN16/HN18 sit at 1.0. A
  radius-graph "one component" hides this because a thin bridge of edges is enough to connect it.
- **The hub is not shared.** The Mixed hub (6,615 cells) draws from an effective 4.8 of 8 patients; HN01
  contributes **1.8%**. The convergence point the trajectory assumes is a few donors' territory, not a meeting of
  all.
- **The bifurcation is a batch axis.** The Basal↔Classical arms co-segregate with HPV (Basal 98.8% HPV−,
  Classical 68% HPV+) — a patient-level covariate never entered into Harmony (`vars_use=['sample']` only).

## Did the agent question it?

**Not the continuity leg.** NB01 pre-commits to the conclusion in prose ("residual patient identity is
biological, not a batch island"; "the debris stays graph-attached, so this step is near-trivial") and the
continuity print is treated as confirmation. The agent's scrutiny turned to Gate 1 only *after* the user pressed
— first on single-patient neighborhoods, then on HN17, then on a "batch correction that is necessary" beyond the
sample key. It then withdrew the mixing PASS. But its stated reasoning — that because `sample` ≈ `patient`,
Harmony "never mixed" the tumors — restates the original agent's framing rather than a fresh measurement, and
overstates the case: Harmony *did* mix donors, just incompletely (same-sample kNN 0.888 → 0.543, still ~3.4× the
floor; cross-patient edges present at 0.45× the mixed-null). Either way the retraction was argued as *integration*
only. Continuity was never named, re-measured, or withdrawn, even though the same lobular structure is what makes
both legs fail. Absent the user's prompts, Gate 1 would have shipped as a clean GO.

## Most defensible decision

**Gate 1 = NO-GO**, on continuity alone, on the evidence in hand:

1. Replace the connectivity boolean with a **gap-sensitive continuity metric** — cross-donor kNN edge fraction
   vs. the mixed-null, and PAGA inter-donor connectivity. Both fail here (0.45× expected; HN01 detached).
2. Re-integrate on the **correct batch model** — patient (not sample-as-proxy) with the HPV covariate — and
   re-certify with a **per-patient** metric, not per-sample.
3. Treat HN01 explicitly: a 22%-of-data donor that will not integrate is either dropped with justification or
   the manifold is declared donor-structured and the trajectory withheld.

This is the same conclusion the agent reached for *mixing* under pressure — extended to the leg it left standing.

**Bottom line.** The continuity leg of Gate 1 was **asserted, not demonstrated** — certified by a test structurally
incapable of failing on dense 10x data, exactly the C3/C4 scale risk calibration named. The manifold is
donor-territorial with a detached 22% lobe; the defensible call is NO-GO pending re-integration on a patient+HPV
model and re-certification with a gap-sensitive metric. The agent could reach this only when steered, and even then
only for mixing — the continuity failure it never independently saw is the one an expert sees first.
