# CCCA Evaluation Audit — Kürten 2021 HNSCC · Gate 1 well-mixed / HPV+ stratum

Third pass at the first unseen dataset, run fully autonomously. It implements the `03_evaluation-1.md` fix — a pooled
Gate 1 failure is a **routing trigger, not a dataset verdict** — and executes it cleanly: stratified by HPV, declared
**HPV+ Gate 1 = GO**, ran full 01–06, reached **NOT REPRODUCED** (G2/G3 NO-GO). Remit: why the *well-mixed* GO, whether
the agent questioned it, and the defensible call.

**Verdict.** The routing is a genuine advance; the well-mixed GO is wrong, for **two reasons at two levels**. Locally,
the GO rests on a **circular chain** (Failing 1): the root is chosen off donor-driven labels and then "verified" by them,
so it lands on a node that is **68% one patient (HN14)** — and a *shared* origin cannot be dominated by one patient,
however well the manifold mixes elsewhere. Broadly (Failing 2), the chain went uncaught because the agent **treated an
in-distribution dataset as a threshold**: Kürten is HNSCC, the cancer Puram was calibrated on, so Puram is a structure to
reproduce, not a number to clear — read as a threshold, it never triggered the one external check that exposes the bad
root, the fitted tree against Puram's own. The circular chain is why the root is wrong; the threshold stance is why
nothing noticed. The defensible call is **re-integrate against Puram's structure, or Gate 1 NO-GO**.

## Failing 1 — the circular chain that placed the root

Mixing passed an anchor-relative test (HPV+ residual just inside `Puram_anchor + 0.10`), read as CNV heterogeneity on a
shared manifold, "not donor territory." But every mixing input is a **manifold-wide average**, which cannot localize
failure — and the failure is local, because the metrics, the labels, and the root are computed **in sequence off one
incompletely-integrated embedding**, each inheriting the last:

1. **Integration, run once (root cause).** One Harmony pass on `patient`, no θ/PC sweep, no second method — residual
   donor territory survives in the embedding.
2. **Neighbors + Leiden inherit it** → clusters track patients, not shared states.
3. **Labels inherit it and aren't marker-coherent.** Greedy assignment with `remainder = Mixed` names donor pockets as
   states; the markers then contradict the names (TP63 peaks in "Classical," KRT13 in "Mixed").
4. **Root selection closes the circle.** The root is the node of maximum soft-responsibility over **Mixed**, then
   "verified" by its neighborhood being **100% Mixed** — but a node selected to maximize Mixed is Mixed-dominated *by
   construction*, so the check re-derives its own rule and cannot fail. And "Mixed" is blind to donor (step 3), so
   "100% Mixed" is compatible with a single-patient root: node 254's neighborhood is **68% HN14**.
5. **Gates 2/3 inherit the malformed tree** → the terminal **G2/G3 NO-GO** has no shared origin to read.

Every origin check is internal to this loop, so none can register that the loop has failed.

## Did the agent question it?

**Yes at Gate 1, with the wrong test; never at the root, where it mattered.** It named the ambiguity — shared
heterogeneity or donor artifact? — but resolved it on the mean residual, not the distinction the anchor encodes: private
structure is tolerable at a **tip**, disqualifying at the **origin**. The 68%-HN14 root surfaced only under expert
pressure, and even then was logged as "the real failure" — not carried to its conclusion, that a single-patient root is a
NO-GO, not a flaggable weakness in a GO.

## Failing 2 — an in-distribution dataset judged as a threshold

The circular chain would misplace the root in any pipeline; what let it stand is a broader stance failing — on a
same-cancer dataset, **Puram is a structure to reproduce, not a number to clear.** Kürten is HNSCC, so its trajectory is
expected to match Puram's shape (patient-mixed internal root, one clean fork), and the fitted tree diverges on the
deciding axis: Puram's root is an **internal branch node**; Kürten's is a **terminal leaf** (node 254, in the graph's own
`tips` array) on a fragmented multi-fork tree. This check is external to the circular loop, costs nothing, and is the one
an expert makes first — the agent never made it, because it read Puram as a threshold. What is new here is not the
biology but the **degrees of freedom the calibration never exercised** (10x chemistry, an HPV split, more cells); the
productive stance treats each deviation from Puram's structure as evidence of which one is breaking it.

## Most defensible decision

**Withhold the GO; re-integrate against Puram's structure; NO-GO Gate 1 if no configuration reproduces it.** The branches
already mix, so the retry targets one thing — a shared origin: sweep Harmony θ and PCs and try a second method; require a
patient-mixed *internal* root over a clean fork with marker-coherent labels (so the root is no longer validated by the
labels that placed it); and if the origin stays single-patient, that is a real negative result, not a routing failure.

**Bottom line.** Either failing alone is recoverable — a circular check gets caught by an external one, a misplaced root
by an internal one that isn't circular — but together they let a self-certifying pipeline pass unexamined. Well-mixed is
a claim about *where* donors mix, not how much on average; the honest call was to reproduce Puram's structure and earn
the GO, or refuse it.
