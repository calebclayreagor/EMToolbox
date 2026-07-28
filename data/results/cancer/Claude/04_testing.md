# CCCA Autonomous-Run Testing Log — Chen 2020 (NPC, 10x)

Repeated fully-autonomous attempts on the **Chen 2020** dataset (nasopharyngeal carcinoma, 10x, ~3.7k
malignant cells). Each attempt runs without expert steering and is reviewed by a fresh-context auditor.
One entry per attempt below — decisive points only. Read alongside the three spec files.

---

## Attempt 1 · Gate 1 NO-GO

- **Fail — `n_pcs=6` under-powers the manifold.** Chord-elbow over-cut the inherited 40; too few PCs force
  a patient-segregated read, so the NO-GO is likely an embedding artifact. (Elbow biases low; bound against
  Puram 40 / Kürten 20.)
- **Fail — `summary.pdf` wrong layout.** Verdict-prose + stacked step-PDFs, not the reference gate-ledger →
  figure-grid one-pager.
- **Held.** Spec re-read at each gate/deliverable; threshold, theta sweep, EMT-TF panel, renumbering all sound.
- **Watch.** Gate call stayed metric-led — embedding read as corroboration, not lead.
