# CCCA Evaluation Audit — Kürten 2021 HNSCC · island removal deleted the trajectory

Sixth pass at the first unseen dataset, run fully autonomously. Reaches step 06, logs **NOT
REPRODUCED**. The verdict is invalid: the removal mis-cut the cell set in both directions — deleting
trajectory, retaining off-trajectory — so every gate ran on the wrong manifold.

- **Log:** G1 GO · G2 PASS (non-branching) · G3 NO-GO → not reproduced
- **Remit:** why the removal cut the wrong subset, whether the agent questioned it, the defensible call

**Verdict — the segmentation is the failure, not the gates.** Read from the signature topology of the
θ=2 integrated embedding, the right lobe is the pSom→Gast→Crest trajectory and the large left lobe is
off-trajectory — the manifold reading the researcher supplied as ground truth; the run itself logs only
which cluster was removed. On that reading, island removal (`removed: ['4'] (797 cells)`) cut the right
lobe's Crest terminus and kept the entire left lobe — a two-sided error:

- **Deleted signal:** losing the Crest terminus truncates the trajectory, so a terminal Crest readout
  reads as a weak gradient — directly corrupting Gate 2/3.
- **Retained noise:** an intact off-trajectory lobe sits inside the manifold the tree is fit on, distorts
  the topology, pulls the root, and can manufacture or mask a bifurcation. This is the more insidious
  half — nothing downstream flags it, and it inflates the very structure the gates test.

The right subset is defined by position on the signature manifold, **not** by a clinical covariate. The
trajectory lobe and the off-trajectory lobe need not split on HPV or any metadata field — proper
subsetting operates on manifold structure, so the absence of a clean clinical separator is not a reason
to retain the off-trajectory lobe or to fall back on covariate stratification.

## Why 10x makes this geometry easy to misread

Kürten is 10x; the anchor (Puram) is SmartSeq2 — the calibration flagged the platform shift as a scale
risk. Sparse, shallow 10x counts drop out the low-expression embryonic signatures, so a trajectory
gradient washes to low dynamic range and its continuous manifold can read as **weakly connected** — a
low-signal tip detaches most easily. The same sparsity lets a distinct off-trajectory transcriptional
state form a **large, clean, well-separated lobe** that looks like legitimate structure rather than
noise. This is why the researcher's reading and the rule diverge: the platform inverts the visual cue
the removal rule leans on, so the real trajectory tip looks detachable while the off-trajectory
population looks like a coherent lobe to keep.

## Why it cut the wrong subset

- **Rule:** over Leiden(1.5), remove clusters with kNN cohesion **>0.90** and size **<8%**. Ranks by
  cohesion and size; never reads position on the signature topology.
- **On Puram:** cohesive small clusters were off-trajectory debris — rule and biology agreed by accident.
- **On Kürten:** by the grid reading the removed cluster is the trajectory's Crest terminus and the
  off-trajectory lobe was retained — the rule inverted the biology on both counts.
- Cohesion+size cannot separate trajectory from off-trajectory; only the signature ordering can. This is
  the C3 "noise detaches cleanly" case the calibration flagged as this decision's top scale risk.
- The agent fixed the anchor's broken instrument (eval-1: radius-graph test can't fail on dense 10x) but
  kept its stance — an island as a topology metric, not a position on the signature manifold.

## Did the agent question it?

- **Autonomously — no.** Run once, logged "anchor step," never checked the removed cluster — or the
  retained lobe — against the signature topology it had rendered.
- **"Seam gone" read as "manifold correct":** θ=2 closed the HPV seam, so the agent treated the embedding
  as settled and stopped interrogating it.
- **Self-consistency read as validation:** every gate agreed because every gate ran on the same mis-cut
  manifold. The eval -1..-4 machinery checks internal consistency; nothing checks whether the cell set is
  right.
- **Only when prompted** — researcher read the trajectory back from the θ=2 grid — did the agent concede
  the removal took the terminus and left the off-trajectory lobe, and retract the verdict.

## Most defensible decision

- **Segment on the signature manifold, not on a topology metric or a covariate.** The pSom→Gast→Crest
  ordering was already rendered — the reading that identifies the trajectory lobe: keep it including its
  terminus, drop the off-trajectory lobe — the inverse of what the rule did on both sides. The subset
  stands on manifold position whether or not a clinical variable happens to separate the two lobes.
- **Do not let cohesion+size make the anatomical call.** On sparse 10x it cannot tell a weakly connected
  trajectory tip from debris, nor a large off-trajectory lobe from real structure; that judgment requires
  the signature ordering, which was in hand.
- **Withhold the verdict.** With the terminus deleted and the off-trajectory lobe retained, no gate reading
  is supported until the manifold is re-segmented and 01–05 re-run.
