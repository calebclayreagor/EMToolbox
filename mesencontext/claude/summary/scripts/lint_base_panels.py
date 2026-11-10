"""Lint a dataset's base-notebook savefig cells against house panel conventions.
Catches the content-level deviations that aspect/orientation checks miss
(e.g. orange EMT colors, >0 thresholds, non-house cmaps, inline colorbars).
Any panel that FLAGS must be regenerated from the house recipe, not kept."""
import json, re, sys, glob, os
HOUSE_EMT_COLORS = {'tab:blue','tab:red','#1f77b4','#d62728'}
def lint(dsdir):
    flags=[]
    for nb in sorted(glob.glob(f"{dsdir}/*.ipynb")):
        j=json.load(open(nb)); base=os.path.basename(nb)
        for c in j['cells']:
            if c['cell_type']!='code': continue
            s=''.join(c['source'])
            if 'savefig' not in s: continue
            low=s.lower()
            # EMT / expression panel
            if 'expression' in low and 'savefig' in low:
                cols=set(re.findall(r"#[0-9a-fA-F]{6}", s)) | set(re.findall(r"'(tab:\w+)'", s))
                bad=[c for c in cols if c.lower() not in {x.lower() for x in HOUSE_EMT_COLORS}
                     and c.lower() not in {'lightgrey','lightgray','#d3d3d3'}]
                if bad: flags.append((base,'expression','non-house color(s): '+', '.join(sorted(bad))))
                # threshold: must use quantile among expressers, not a bare >0 selection mask
                if re.search(r">\s*0\b", s) and 'quantile' not in low:
                    flags.append((base,'expression','>0 selection threshold (not top-quantile-among-expressers)'))
            # signature panels: plasma cmap + separate colorbar (colorbar_loc=None)
            if 'signature' in low and 'savefig' in low:
                cm=re.findall(r"cmap\s*=\s*'(\w+)'", s)
                if cm and any(x!='plasma' for x in cm): flags.append((base,'signature','cmap '+str(cm)+' (house=plasma)'))
                if re.search(r"colorbar_loc\s*=\s*'(right|left|top|bottom)'", s):
                    flags.append((base,'signature','inline colorbar (house=separate colorbars, colorbar_loc=None)'))
            # pseudotime: cividis
            if ('pseudotime' in low or 'manifold.pdf' in low or "'t'" in s) and 'savefig' in low:
                cm=re.findall(r"cmap\s*=\s*'(\w+)'", s)
                if cm and any(x not in ('cividis',) for x in cm) and 'signature' not in low:
                    flags.append((base,'pseudotime/t','cmap '+str(cm)+' (house=cividis)'))
    return flags
if __name__=="__main__":
    fl=lint(sys.argv[1])
    print(f"LINT {os.path.basename(sys.argv[1])}: {len(fl)} flag(s)")
    for f in fl: print("  FLAG", *f)
