import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _branching_panels import regen_branching
regen_branching(
    D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Skin/Ji2020_Skin-9",
    F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Skin/Ji2020_Skin-9",
    samples_title="Cutaneous SCC \u2014 samples",
    emt=[('SOX9','tab:blue'),('SNAI2','tab:red')], emt_q=0.80, hub_celltype='Basal')
