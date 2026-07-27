# CCCA Evaluation Audit — Kürten 2021 HNSCC · spec compliance

Fourth pass at the first unseen dataset, run fully autonomously. The remit is narrow: why the agent ignored the spec
files. It reached **Gate 1 GO** (HPV+ mixing/continuity) · **Gate 2 NO-GO** · **not reproduced**, and the local
analysis is the cleanest of the four passes. It also ignored an explicit instruction from the spec **twice** — once
on deliverable format, once on the integration sweep — and both lapses have the same cause.

**Verdict.** The agent worked from its own model of the task instead of reading the spec as binding instruction. It
never asked "does this match the document"; it asked "is my own work clean and valid," and answered yes both times.

## The two lapses

**Deliverable format.** The task file specifies the format and contents of the deliverables (notebook set, figure
layout, `summary.pdf` placement matching the Puram2017 calibration). The agent produced its own layout without
re-reading that spec, and the researcher had to say the outputs were "not at all aligned with the required
deliverables formats and contents." Only then did it re-open the task file. Even after, `summary.pdf` was left in the
wrong directory and had to be flagged twice more before it sat where the calibration keeps it.

**Integration sweep.** `03_evaluation-2.md` gave one explicit, sequenced instruction: sweep Harmony θ and PCs, add a
second integration method, and reach NO-GO **only if no configuration reproduces Puram's patient-mixed internal
root**. The agent ran a single default-θ (=2) Harmony pass — the exact "integration run once" that eval-2 named as
the root cause — and went straight to NO-GO on that first fit. No sweep, no second method, verdict before the search.
Unlike the format lapse, this one was never corrected: it surfaced only when the researcher asked directly, at which
point the agent confirmed it had not complied.

## Why, both times

The agent had a validated prior template for each task — a deliverable layout it had produced before, and an analysis
pipeline it had built and trusted — and in both cases it reproduced the template rather than execute the spec. For
deliverables it defaulted to "the format I produced." For integration it ported its validated single-pass pipeline,
which is precisely the configuration the spec told it to replace. The spec was treated as a description of work it had
already done, not as a set of instructions to check the work against.

This is why its self-correction never caught either lapse. The in-run reviewer flagged internal errors (a circular
root test, a softened Gate-1 verdict) and the agent fixed them cleanly — because those checks ask "is my own work
consistent." Neither the format gap nor the sweep omission is an internal inconsistency; both are gaps between the
work and the document, and nothing in the agent's own review compared the two. So the only thing that surfaced them
was the researcher reading the spec back to it.

**Bottom line.** A spec-compliance failure, not a judgment call. Two required instructions — deliverable format and
the θ/PC + second-method sweep — were each executed by reproducing the agent's own prior template instead of the
document. The local mechanics are the best of the four passes, which is the point: the machinery was pointed at
making its own work self-consistent, never at conforming it to the spec.
