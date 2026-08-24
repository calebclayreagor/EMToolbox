#%%
import os
import pandas as pd
import pyranges as pr

pth = os.path.join('..', '..', '..', '..', 'data')
pth_in = os.path.join(pth, 'unzip', 'GSE56287', 'GPL18477')
pth_ref = os.path.join(pth, 'ref', 'HydraGenomeProject')

colnames = [
    'probe',
    'Chromosome',
    'pident',
    'length',
    'mismatch',
    'evalue',
    'bitscore',
    'qstart',
    'qend',
    'sstart',
    'send']

# load blast results
fn = os.path.join(pth_in, 'GPL18477_probes_blastn.tsv')
blast = pd.read_csv(fn, sep = '\t', header = None, names = colnames)
blast['Start'] = blast[['sstart', 'send']].min(axis = 1) - 1
blast['End'] = blast[['sstart', 'send']].max(axis = 1)
blast['Strand'] = ((blast['sstart'] < blast['send'])
                   .map({True: '+', False: '-'}))
probes = pr.PyRanges(blast)

colnames = [
    'Chromosome',
    'source',
    'Feature',
    'Start',
    'End',
    'score',
    'Strand',
    'frame',
    'attributes']

# load holigactis genes
holi = pd.read_csv(os.path.join(pth_ref, 'HOLI.GeneModels.gff3'),
                   sep = '\t', comment = '#', header = None,
                   names = colnames, skip_blank_lines = True)
holi = holi.loc[holi.Feature == 'gene'].copy()
holi['gene_id'] = holi.attributes.str.extract(r'ID=([^;]+)')
holi['Start'] = holi.Start - 1
holi = holi[['Chromosome', 'Start', 'End', 'Strand', 'gene_id']]
holi_pr = pr.PyRanges(holi)

# join: probes, genes
result = (probes.join(holi_pr, report_overlap = True, suffix = '_gene')
          .df.sort_values(['probe', 'Overlap'], ascending = [True, False])
          .drop_duplicates('probe').set_index('probe'))

# save results
result.to_csv(os.path.join(pth_in, 'GPL18477_probes_genes.csv'))

# %%
