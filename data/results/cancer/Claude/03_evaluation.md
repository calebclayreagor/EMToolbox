# CCCA Evaluation Audit — Kürten 2021 HNSCC (first unseen dataset)

The analyst ran the six-step protocol on **Kürten 2021**, the first dataset whose answer was not known
in advance. Reached the expression step, **G1 GO / G2 GO / G3 NA** — the non-branching case (§1). An
expert steered step-by-step and a fresh-context reviewer checked claims. The question is not *did it
pass* but *which passes came from the agent's own reasoning* — the gap a fully-autonomous run must close.

**Verdict.** The pattern reproduces: single embryonic axis, root Gast/pSom-high → terminus Crest-high,
EMT-TFs **FOXC1 → SNAI2** — a strict linear subset of Puram. But at nearly every gate the agent's first
call was wrong, corrected by the expert or reviewer. Cleared as a *supervised* run; not as evidence of
autonomy.

## Six forks

1. **Gate 1.** The agent passed G1 on a mixing scalar and a
   connected-components test; the expert had to redirect attention to the embedding itself, which showed
   a per-patient archipelago the metrics had scored as integrated. *Rule:* judge G1 on the regenerated
   embedding across an integration-strength sweep, with a per-neighborhood metric (iLISI); never on a
   scalar alone.

2. **Lobe identity.** The integrated manifold resolved into two lobes and the
   agent moved to fit one curve across both; the expert required each lobe's biological identity first.
   Only one lobe reproduced the embryonic signature relationships (Gast/pSom co-vary, both oppose Crest);
   the other was a cycling compartment with Gast confounded by proliferation. *Rule:* a manifold resolves
   into sub-regions — settle their biology (signatures and cell cycle) before the G1 GO, and scope the
   trajectory to the region that reproduces the reference relationships.

3. **Root & topology.** The agent rooted at the Crest tip,
   treating neural crest as the progenitor state; developmentally Crest is *late*, so the root belongs at
   the Gast/pSom tip. A non-branching topology is fit with scFates `curve`, not `tree`. *Rule:* root from
   the signatures' developmental order; match the scFates method to the topology.

4. **Continuity.** The agent certified the
   curve as continuous using a metric built from UMAP neighbors, blind by construction to a fold in that
   same UMAP; the reviewer caught the fold. It arose from re-embedding a linear compartment — an elongated
   strip a fresh UMAP folds into a U. *Rule:* do not re-embed a linear compartment, and do not measure
   continuity with a metric that reads its neighbors off the embedding being tested.

5. **EMT-TF readout.** The canonical Snail/Zeb/Twist panel yielded only a terminus factor; FOXC1, the
   root-end factor, surfaced only once the panel was widened. *Rule:* score EMT-TFs on this dataset gated on
   detectable expression, and include other mesenchymal families such as FOXC and PRRX, not only Snail/Zeb/Twist.

6. **Deliverables.** With G3 = NA, the agent began the branching-only
   `04_correlation` / `05_modules` notebooks, which assert structure not found. *Rule:* gate outcomes decide
   which notebooks exist; an NA or NO-GO means the corresponding deliverables are not produced (§6).

## Three lessons for an autonomous run

1. **Biology before geometry.** The scientifically decisive forks were the same failure — a geometric
   result read as biology without the biological check. That check must run and appear in the notebook
   before the GO: G1 against the regenerated embedding, each sub-region's identity before the curve,
   continuity off an independent embedding. The gate stays binary — the agent proposed "Conditional GO"
   twice, and it is not an outcome.

2. **Check against the spec, not memory.** The run's deliverable errors were caught by re-reading the
   binding spec against the notebooks rather than trusting recall — the renumbering rule, the deliverable
   set, and the summary format were each re-verified against the spec text before finalizing. An autonomous
   run should re-read the relevant spec section at each gate and before shipping, and check its outputs
   against the binding text.

3. **Deliverables must be reproducible and consistent.** Each notebook must run end-to-end from raw and
   reach the reviewed result, and the values it produces must match the summary and log that report them.
   Where a step is stochastic (Harmony's KMeans is not seed-deterministic), state the tolerance so a benign
   shift is not read as a changed decision.

## Bottom line

The protocol transferred; the judgment did not. The derivation machinery ran correctly on unseen data
(threshold by gap-finding, `n_pcs` off the scree, detection-gated signatures), but the decisive calls —
which lobe is the manifold, where the trajectory roots, which transcription factors to read — the agent
got wrong on first pass, and the expert corrected each by putting biology ahead of geometry. A fully
autonomous run makes those calls without the expert; the three lessons above are what that takes. The
verifier is the readiest to automate — the reviewer here was already a fresh-context agent — and is the
safeguard that caught the two claims the agent made after asserting the rule against them.
