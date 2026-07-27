# CCCA Evaluation Audit — Kürten 2021 HNSCC · stratify vs. integrate more strongly

Fifth pass at the first unseen dataset, run fully autonomously. Folds every accumulated fix into one pass
(gap-sensitive Gate-1, pooled failure as routing trigger, integration sweep + second method, non-circular
root) and reaches the same **NOT REPRODUCED** as steered passes -2/-3, on its own.

- **Log:** pooled Gate 1 NO-GO → stratify → HPV+ GO · G2/G3 NO-GO
- **Remit:** the reasoning behind stratifying by HPV rather than integrating the pool more strongly

**Verdict — the stratify decision is not established.** The sweep judged "over-integration" by proximity to
the anchor residual, so any θ strong enough to close the cross-HPV seam was disqualified by definition — it
could only ever conclude "stratify." The one test that separates *two diseases* from *one under-integrated
10x manifold* (integrate the full pool hard, render, fit a tree) was named as decisive and never run.
Stratifying at θ≤3 discarded the 2 HPV− donors without excluding the simpler explanation: the integration
was never strong enough.

## The decision and its flaw

- **Pooled Gate 1 fails** continuity at default Harmony (cross-HPV edge ratio **0.105**).
- **The sweep** (θ∈{default,1,2,3}, Combat) found continuity **does** recover (~0.5 at θ≥2) — but called
  that "over-integration blending two clinically distinct tumors," and read Combat's near-zero ratio as
  proof the axis is "intrinsic, not a batch offset." → **stratify by HPV.**

Because "over-integration" was defined by proximity to the anchor residual, the sweep could only terminate
in "stratify." Two things were therefore never done:

1. **The strong-integration pool was never rendered or tree-fit.** The agent concluded that no θ closes the
   seam without blending the two tumor types together — but that is a claim about mixing scalars, never a
   look at the resulting manifold. Whether θ≥2 gives a coherent one-tumor structure was never checked. This
   is the decisive gap: a linear Gast→pSom→Crest progression is a *subset* of Puram's branching trajectory
   (a fork = a linear path + a bifurcation), so it stays consistent with the in-distribution topology and is
   a Gate-2 pass per spec §1 — **yet at strong integration that same linear collapse reads as
   "over-integration" on the mixing scalars alone.** The label cannot tell a genuine linear topology from
   over-blending; only rendering the manifold can.
2. **The competing hypothesis was never excluded.** A dense 10x cohort needing intense integration would
   look exactly like this — donor-territorial at default θ, continuity recovering only under strong
   correction.

## Did the agent question it?

- **Autonomously — no.** Treated "pooled failure → stratify" as a settled eval-1 mandate; ran the sweep to
  justify the seam, never to test whether the pool could be integrated.
- **Only when prompted** did it concede stratifying "threw away half the cells to fit a premature
  conclusion" and name two follow-up tests — of which the decisive **full-pool integration test was never
  run** (misreported as "mid-flight," corrected only when the reviewer flagged it).

## Most defensible decision

**Do not stratify until the pool is shown un-integratable.**

1. Re-integrate the full 8-donor pool at escalating θ (and a genuine second method).
2. **Render and tree-fit at each rung**; score both the branching fork and the linear Gast→pSom→Crest
   progression — judging "over-integration" from the rendered structure and signature ordering, not the
   anchor residual.
3. Stratify **only** if the seam survives strong integration with donor mixing at or above the anchor. If a
   coherent manifold emerges instead, the routing was wrong and the 2 HPV− donors should not have been
   dropped.

**Bottom line.** This pass fixed the circular root of eval-2 — a real advance — but its foundational move was
decided on θ≤3 scalars against a circular bar, and the strong-integration pool that would settle it was never
built. Until that test runs, "two diseases" is an assumption, not a finding; the likelier reading is that the
integration was never strong enough.
