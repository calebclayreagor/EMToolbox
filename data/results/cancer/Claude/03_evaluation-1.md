# CCCA Evaluation Audit — Kürten 2021 HNSCC · Gate 1 re-analysis / stratification

Second pass at the first unseen dataset, run fully autonomously to implement the fixes in `03_evaluation.md`. The
agent reached preprocessing + expression only; the log reads **G1 NO-GO**. Three questions: why NO-GO, did the
agent question it, and what was the defensible call.

**Verdict.** The Gate 1 mechanics are right — a continuity metric that can fail, the HPV/site confound
identified. The decision is wrong: **Gate 1 gates a manifold, not a dataset.** A pool that fails because its
dominant axis is a clinical covariate is the *trigger* for stratified analysis, not a dataset verdict. The agent
stamped the whole dataset NO-GO and stopped — the reference audit's error in a new form.

## Why the pool failed, and why that means stratify

The pool fails both Gate 1 legs. **Mixing:** same-patient kNN 0.983 raw → 0.605 Harmony vs. mixed-null floor 0.158
→ residual **+0.447**; forcing integration (θ=2, or joint `[patient,HPV]`) only reaches +0.21 / +0.13.
**Continuity:** cross-HPV edge weight **0.047 vs. 0.415 expected (0.11×)**; Leiden donor-territorial. The cause is
structural: of 8 retained donors only HN01 (Oral Cavity) and HN07 (Larynx) are HPV−/keratinizing, the rest HPV+
oropharyngeal, so the Basal↔Classical split co-segregates with HPV — never entered into Harmony. The pooled
"bifurcation" **is** that seam between two diseases (the prior run's Basal 98.8% HPV− ↔ Classical 68% HPV+ arms),
and no integration removes an axis this strong. This does not license abandoning the dataset; it specifies which
manifold to build — and the strata are not equivalent:

- **HPV+ (6 oropharyngeal donors, 7,872 cells)** — analysis-grade: cross-patient edge ratio 0.44, *more* connected
  than the pool (PAGA max 0.306 / median 0.078 vs. 0.183 / 0.042). Should be considered for passing Gate 1.
- **HPV− (2 donors, 3,279 cells)** — underpowered (edge ratio 0.08). Report as insufficient-n; do not gate.

## Did the agent question it?

Three beats, and the failure is in the third.

**It missed stratification.** The agent reached the pooled NO-GO on its own but never proposed subsetting by HPV,
despite holding every diagnostic that flagged the confound. Stratification is the standing next step once a
clinical covariate dominates a pooled manifold; the agent did not take it, and the researcher had to prompt it.

**Prompted, it stratified correctly.** It re-integrated each stratum from scratch (the 0.44 / 0.08 ratios above)
rather than arguing from the pooled fit — the right procedure, executed properly.

**Then it fell back into the prior failure mode.** Asked to judge the strata, it read each as connected, took the
absence of fragmentation as evidence *for* a continuum, and leaned toward retracting the NO-GO — the very
connected-components judgement the re-run was built to discard, the prior run's mistake in mirror image.
Single-connectedness is not continuity; the +0.447 mixing residual and the HPV confound that actually carry the
NO-GO are untouched by whether a stratum is connected. Having stratified correctly, the agent certified the
result with the one metric it had just been corrected for trusting.

The agent did attempt to push the analysis further, but only after prompting and only until external input halted
it — the completion path was never its own, which fails the autonomy requirement. (A smaller deliverable lapse in
the same vein: the summary PDF did not initially follow the calibration-run template — an explicit deliverable
requirement — and was reformatted only when the researcher pointed it out.)

## Most defensible decision

Not a dataset verdict but a routing decision: **no blanket NO-GO.** The pooled failure diagnoses a confounded
manifold, so stratify on HPV/site and re-enter the pipeline per stratum — **HPV+ considered for passing Gate 1**
on its within-stratum metrics rather than failed with the pool, HPV− reported as insufficient-n. A dataset-level
"G1 NO-GO" conflates *this pool is not analyzable* with *this dataset has no trajectory*, the exact conflation the
gating exists to prevent. Whether HPV+ then clears Gates 2/3 is a separate, untested question — the agent's read
that its tree is proliferation/stress-organized rather than the embryonic hub is a hypothesis, not a verdict.
