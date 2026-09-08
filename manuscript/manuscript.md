**EMToolbox uncovers pan-cancer co-option of bifurcated embryonic EMT programs**

Caleb C. Reagor 1, 2, \*, CO-AUTHORS, and Igor Adameyko 1, 3, \*

1 Department of Physiology and Pharmacology, Karolinska Institutet, 17177 Stockholm, Sweden  
2 Howard Hughes Medical Institute and Laboratory of Sensory Neuroscience, The Rockefeller University, New York, NY, USA 10065  
3 Department of Neuroimmunology, Center for Brain Research, Medical University of Vienna, 1090 Vienna, Austria  
\* Correspondence shall be addressed to: [igor.adameyko@ki.se](mailto:igor.adameyko@ki.se); [creagor@rockefeller.edu](mailto:creagor@rockefeller.edu)

**Abstract**

Abstract text here.

**Introduction**

single-cell RNA-sequencing (scRNA-seq)  
epithelial-to-mesenchymal transition (EMT)  
embryonic EMT (e-EMT)  
adult EMT (a-EMT)  
EMT transcription factor (EMT-TF)

**Results**  
**Developmental scRNA-seq data for comparison of e-EMT programs**

We first sought to perform an unbiased, cross-lineage comparison of the transcriptional events encompassing e-EMT by collecting published scRNA-seq data of mouse embryogenesis from our group and others. Although EMT reshapes diverse tissues across development including visceral organs such as the liver, stomach, lungs, and heart, we reasoned that these systems constituted noisier examples of shared e-EMT programs due to the presence of orthogonal transcriptional processes, including terminal lineage commitment and asynchronous EMT-MET cycles [(Thiery *et al.*, 2009; Han *et al.*, 2020\)](https://www.zotero.org/google-docs/?FfJvar). We therefore selected three examples of primary e-EMT—namely, gastrulation (1) [(Scheibner *et al.*, 2021\)](https://www.zotero.org/google-docs/?KXKUHk); posterior somitogenesis (2) [(Jin *et al.*, 2025\)](https://www.zotero.org/google-docs/?F01GWt); and neural crest migration (3) [(Poverennaya *et al.*, 2026\)](https://www.zotero.org/google-docs/?bMcomk)—to facilitate our comparison of the shared transcriptional programs driving EMT across early-to-mid embryogenesis (**Figure 1a**; **Supplementary Table 1**).  
	These datasets comprised several progenitor-cell populations that experienced unique cell-fate bifurcations between mesenchymal and other lineages. During gastrulation (E6.5-7.5), pluripotent epiblast cells underwent a lineage bifurcation between lateral plate mesoderm (LPM) and definitive endoderm (DE; Figure 1a, left) [(Scheibner *et al.*, 2021\)](https://www.zotero.org/google-docs/?eK1AzZ), whereas later epiblast-derived neuromesodermal progenitors (NMPs; E8.5) underwent a bifurcation between the presomitic mesoderm (PSM) and neural tube (Figure 1a, middle) [(Jin *et al.*, 2025\)](https://www.zotero.org/google-docs/?NoqkBM). In the developing head (E8.5-10.5), migratory neural crest cells (NCCs) also underwent a bifurcation between mesenchymal and neuroglial fates (Figure 1a, right) [(Poverennaya *et al.*, 2026\)](https://www.zotero.org/google-docs/?gFEWdY). Together, these datasets presented a detailed description of primary e-EMT across multiple tissues and stages and therefore constituted an important resource for uncovering the shared transcriptional programs driving e-EMT across development.

**Shared transcriptional programs comprise e-EMT across cell types**

To identify shared transcriptional signatures across our selected datasets, we first subset all cell types that contributed to mesenchymal lineages across the observed bifurcations (Figure 1a, dashed boxes). These cells displayed strong expression of several core EMT-TFs including *Snai1*, *Twist1*, and *Zeb2* (**Figure 1b**) [(Yang *et al.*, 2020\)](https://www.zotero.org/google-docs/?hwavGv), with all three datasets exhibiting similar cross-lineage expression patterns between progenitors and mesenchymal populations. Notably, the mesenchymal lineages in gastrulation (1) and posterior somitogenesis (2) displayed nearly identical patterns of EMT-TF expression including early upregulation of *Snai1* and *Zeb2* and later onset of *Twist1*, *Foxc1/2*, and *Prrx2*. However, these cell type-specific expression patterns only provided a coarse readout of the shared transcriptional programs orchestrating e-EMT across developmental lineages.  
	We next employed our group’s computational framework scFates to perform pseudotime analysis across the mesenchymal lineages and identify genes whose expression significantly varied along these trajectories (**Figures 1c, d**) [(Faure *et al.*, 2023\)](https://www.zotero.org/google-docs/?8QJ0dL). Each trajectory comprised a single cell-state gradient originating in pluripotent or multipotent progenitors and terminating in fate-restricted mesenchymal cells along the lineage. Subsequent statistical modeling identified 219, 217, and 215 genes whose expression was significantly associated with the inferred pseudotime trajectories for gastrulation (1) (Figure 1d, left), posterior somitogenesis (2) (Figure 1d, middle), and neural crest migration (3) (Figure 1d, right), respectively. This analysis uncovered many expected early- and late-stage markers for gastrulation (1)—such as *Epcam* (early) and *T*, *Mesp1*, and *Fn1* (late)—and posterior somitogenesis (2)—such as *Cdx2*/*4* (early) and *Tbx6*, *Foxc2*, and *Fn1* (late)—though not for neural crest migration. To identify the shared transcriptional programs across trajectories, we next implemented a deep-conservation filter to select 79 (1), 98 (2), and 104 (3) genes that possessed at least one homolog in the genomes of both *Homo sapiens* and *Drosophila melanogaster*, reasoning these genes might also possess conserved functions across developmental lineages (**Supplementary Table 2**). We subsequently refer to these gene modules as Gast (1), pSom (2), and Crest (3), where each module corresponds to the trajectory from which it was derived.  
	Although these genes are expressed at various pseudotimes along the full trajectories, each module’s relative expression signature—defined as the module’s mean expression relative to the mean expression of the other two modules—forms a similar progression across the three trajectories (Figure 1d, bottom panels). In gastrulation (1) and posterior somitogenesis (2), pSom expression (early) precedes Gast expression (mid) and finally Crest expression (late), while both Gast and pSom expression (early) precede Crest expression (late) in neural crest migration (3). These results suggest that shared transcriptional programs comprise e-EMT across divergent lineages from both ancient germ layers such as mesoderm and newer vertebrate-specific innovations such as NMPs and NCCs [(Sauka-Spengler *et al.*, 2007; Sambasivan and Steventon, 2021\)](https://www.zotero.org/google-docs/?fP1zPZ).

**Distinct e-EMT modules encompass shared signaling pathways**

To further elucidate the functional relationships between shared e-EMT transcriptional programs, we next compared the membership of individual genes across Gast, pSom, and Crest (**Figure 1e**). Although these modules are associated with similar morphogenetic processes, their specific gene-level compositions are largely dissimilar, with Gast and pSom displaying the strongest pairwise similarity (Jaccard index \= 0.18). However, because pseudotime analysis and downstream feature selection can be sensitive to trajectory resolution and parameter choice, we also performed gene ontology (GO) term-enrichment analysis to identify the top biological processes associated with each module (**Figure 1f; Supplementary Tables 3-5**). While Gast and pSom both exhibited strong enrichment for GO terms related to transcriptional regulation, lineage commitment, and Wnt signaling, Crest was enriched for terms related to RNA processing and RNP complex assembly. We also used STRING to analyze the functional enrichment of each module’s protein-protein interaction network, which revealed a striking pathway-level convergence: all three modules contained clusters for Wnt signaling—a canonical EMT-activating upstream pathway—while pSom and Crest both contained clusters for retinoic acid signaling, and Gast contained clusters for TGF-β and Notch signaling (**Figure 1g; Supplementary Figures S1-3**) [(Youssef and Nieto, 2024\)](https://www.zotero.org/google-docs/?oMIsFd). These results suggest that while Gast and pSom are somewhat similar on the level of individual genes, pSom and Crest are more similar at the signaling pathway level despite notable differences in their genes’ biological processes.  
   
**Figure captions**  
**Figure 1:**   
**(a)**   
[Faure, L. *et al.* (2023) “scFates: a scalable python package for advanced pseudotime and bifurcation analysis from single-cell data,” *Bioinformatics*. Edited by O. Vitek, 39(1), p. btac746. Available at: https://doi.org/10.1093/bioinformatics/btac746.](https://www.zotero.org/google-docs/?XoAvOO) 

[Han, L. *et al.* (2020) “Single cell transcriptomics identifies a signaling network coordinating endoderm and mesoderm diversification during foregut organogenesis,” *Nature Communications*, 11(1), p. 4158\. Available at: https://doi.org/10.1038/s41467-020-17968-x.](https://www.zotero.org/google-docs/?XoAvOO) 

[Jin, H. *et al.* (2025) “Dual genetic tracing demonstrates the heterogeneous differentiation and function of neuromesodermal progenitors in vivo,” *Proceedings of the National Academy of Sciences*, 122(14), p. e2402305122. Available at: https://doi.org/10.1073/pnas.2402305122.](https://www.zotero.org/google-docs/?XoAvOO) 

[Poverennaya, I. *et al.* (2026) “Ribosomal modifications are associated with mesenchymal fate selection in the neural crest lineage,” *Nature Communications*, 17(1), p. 2326\. Available at: https://doi.org/10.1038/s41467-026-70375-6.](https://www.zotero.org/google-docs/?XoAvOO) 

[Sambasivan, R. and Steventon, B. (2021) “Neuromesodermal Progenitors: A Basis for Robust Axial Patterning in Development and Evolution,” *Frontiers in Cell and Developmental Biology*, 8, p. 607516\. Available at: https://doi.org/10.3389/fcell.2020.607516.](https://www.zotero.org/google-docs/?XoAvOO) 

[Sauka-Spengler, T. *et al.* (2007) “Ancient Evolutionary Origin of the Neural Crest Gene Regulatory Network,” *Developmental Cell*, 13(3), pp. 405–420. Available at: https://doi.org/10.1016/j.devcel.2007.08.005.](https://www.zotero.org/google-docs/?XoAvOO) 

[Scheibner, K. *et al.* (2021) “Epithelial cell plasticity drives endoderm formation during gastrulation,” *Nature Cell Biology*, 23(7), pp. 692–703. Available at: https://doi.org/10.1038/s41556-021-00694-x.](https://www.zotero.org/google-docs/?XoAvOO) 

[Thiery, J.P. *et al.* (2009) “Epithelial-Mesenchymal Transitions in Development and Disease,” *Cell*, 139(5), pp. 871–890. Available at: https://doi.org/10.1016/j.cell.2009.11.007.](https://www.zotero.org/google-docs/?XoAvOO) 

[Yang, J. *et al.* (2020) “Guidelines and definitions for research on epithelial–mesenchymal transition,” *Nature Reviews Molecular Cell Biology*, 21(6), pp. 341–352. Available at: https://doi.org/10.1038/s41580-020-0237-9.](https://www.zotero.org/google-docs/?XoAvOO) 

[Youssef, K.K. and Nieto, M.A. (2024) “Epithelial–mesenchymal transition in tissue repair and degeneration,” *Nature Reviews Molecular Cell Biology*, 25(9), pp. 720–739. Available at: https://doi.org/10.1038/s41580-024-00733-z.](https://www.zotero.org/google-docs/?XoAvOO) 

