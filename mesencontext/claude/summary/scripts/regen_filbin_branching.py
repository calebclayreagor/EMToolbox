import sys, os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _branching_panels import regen_branching
regen_branching(
    D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Brain/Filbin2018_Brain-9",
    F="/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Filbin2018_Brain-9",
    samples_title="H3-K27M Glioma \u2014 samples",
    emt=[('PRRX1','tab:blue'),('ZEB1','tab:red')], emt_q=0.80, hub_celltype='Mixed')
