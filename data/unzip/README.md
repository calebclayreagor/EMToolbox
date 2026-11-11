# `data/unzip/`: source data

Extracted datasets, downloaded from public archives or received from collaborators.

**8 datasets · 700 files · 165.6 GB**

## Datasets

| directory | study | source | acquired | modifications | notes |
|---|---|---|---|---|---|
| `CCCA/` | Tyler et al. 2025 | Weizmann 3CA, `https://www.weizmann.ac.il/sites/3CA/` | 2025-02-07–2025-02-09 | — | 129 folders, one per 3CA dataset. Folder layouts vary between datasets at source. 3CA publishes no version identifier, so the acquisition date identifies the snapshot; 127 of 129 folders carry timestamps in that window. |
| `GSE162534/` | Scheibner et al. 2021 | GEO `GSE162534` | 2025-05-15 | 8 directories generated | Holds 8 per-sample archives, which `development/GSE162534/preprocessing.ipynb` extracts on each run; the resulting directories are regenerable. |
| `GSE175435/` | Chatterjee et al. 2022 | GEO `GSE175435` | | — | 1 of the series' 10 samples. |
| `GSE229103/` | Jin et al. 2025 | GEO `GSE229103` | 2025-05-14 | — | — |
| `GSE56287/` | Domazet-Lošo et al. 2014 | GEO `GSE56287`; GEO platform `GPL18477` | 2026-04-24 (`GPL18477/`) | 3 files generated | — |
| `MarBTN/` | Hart et al. 2025 | GitHub `sfhart33/MarBTNtranscriptome` (GPL-3.0); files added to the repository after correspondence with the authors | 2026-04-23 | repo layout flattened | 28 of the repository's `*_ReadsPerGene.out.tab`, plus `gene_translation.txt` and `sample_data.txt`. At source the `.tab` files and `gene_translation.txt` are in `outputs/star/`, `sample_data.txt` in `inputs/`. |
| `NB/` | Thirant et al. 2023 | received from authors | 2026-06-22–2026-07-31 | 1 file generated | Intermediate objects, not publicly deposited. |
| `rRNAModifications/` | Poverennaya et al. 2026 | received from author; reprocessed from GEO `GSE201257` | 2025-05-25 | — | Intermediate objects; not the data deposited under the accession. |

`acquired` is from the download log (`data/logs/`) where one exists, otherwise the filesystem
timestamp; blank where only the source's timestamps survive.

## Generated in place

| output | input | produced by |
|---|---|---|
| `data/unzip/GSE162534/` — 8 directories, 24 files | `data/unzip/GSE162534/`'s 8 per-sample archives | `development/GSE162534/preprocessing.ipynb` |
| `data/unzip/GSE56287/GPL18477/GPL18477_probes.fasta` | `data/unzip/GSE56287/GPL18477/GPL18477_annotation.txt` | `invertebrate/holigactis/scripts/probes/fasta.py` |
| `data/unzip/GSE56287/GPL18477/GPL18477_probes_blastn.tsv` | `data/unzip/GSE56287/GPL18477/GPL18477_probes.fasta`; `data/ref/HydraGenomeProject/` | BLAST (`envs/blast.yaml`), not scripted |
| `data/unzip/GSE56287/GPL18477/GPL18477_probes_genes.csv` | `data/unzip/GSE56287/GPL18477/GPL18477_probes_blastn.tsv`; `data/ref/HydraGenomeProject/HOLI.GeneModels.gff3` | `invertebrate/holigactis/scripts/probes/genes.py` |
| `data/unzip/NB/PDX63.strigentFilters_rmRibo_rmDoub.h5ad` | `data/unzip/NB/PDX63.strigentFilters_rmRibo_rmDoub.rds` | `neuroblastoma/convert.R` |
