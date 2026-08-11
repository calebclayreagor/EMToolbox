import os, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Breast/Griffiths2021_Breast-5"
F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Breast/Griffiths2021_Breast-5"
proc=sc.read_h5ad(os.path.join(D,"processed.h5ad"))
fig,ax=plt.subplots(1,1,figsize=(5,5))
sc.pl.umap(proc,color='sample',size=20,frameon=False,show=False,ax=ax)
ax.invert_yaxis(); ax.invert_xaxis()   # match the other 5 panels exactly
lg=ax.get_legend()
if lg: lg.remove()
ax.set_title('Breast Cancer Samples',size=13)
ax.text(.5,-.05,'Griffiths et al., 2021',ha='center',transform=ax.transAxes)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated Griffiths samples.pdf, legend removed, both inverts kept")
