import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _branching_panels import regen_branching
regen_branching(
    D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Head-and-Neck/Puram2017_Head-and-Neck",
    F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Head-and-Neck/Puram2017_Head-and-Neck",
    samples_title="HNSCC \u2014 samples",
    emt=[('ZEB1','tab:red'),('PRRX1','tab:blue')], emt_q=0.90, hub_celltype='Mixed')
