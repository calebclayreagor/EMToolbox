"""Reusable CCCA summary.pdf builder — reference (Puram/Kurten) one-pager layout.
Renders title -> GO/NO-GO GATES -> STEP FIGURES grid -> Dataset/Verdict -> Parameter choices.
Text is passed in verbatim (science unchanged); layout uses fixed margins + wrapping so nothing clips.
"""
import os, re, textwrap
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pypdfium2 as pdfium

BLUE = "#1f5fa8"; GREEN = "#1a9641"; GREY = "#888888"; RED = "#c0392b"

_LEDGER = "/home/caleb/EMToolbox/mesencontext/spec/05_log.md"

def _ledger_attempts(dataset):
    """Total attempts (m) for a dataset from the ledger Attempts column (last col)."""
    key = "Data_" + dataset
    try:
        for ln in open(_LEDGER, encoding="utf-8"):
            if not ln.startswith("| "):
                continue
            cols = [c.strip() for c in ln.strip().strip("|").split("|")]
            if len(cols) >= 13 and cols[3] == key:
                return int(cols[-1])
    except Exception:
        pass
    return None

def run_label_for(dir_path):
    """Dynamic 'run n of m' from the output dir + ledger. base dir -> first run (n=1);
    -N adjudicated dir -> final run (n=m); single-attempt -> run 1 of 1. None if not found."""
    name = os.path.basename(os.path.normpath(dir_path))
    base = re.sub(r"-\d+$", "", name)
    m = _ledger_attempts(base)
    if not m:
        return None
    n = 1 if name == base else m
    return f"run {n} of {m}"

def _png(pdf_path, scale=6.0):
    d = pdfium.PdfDocument(pdf_path)
    img = d[0].render(scale=scale).to_pil()
    return img

def build_summary(out_pdf, title, gates, panels, dataset, verdict, params, cite_absent=False, branching=False, run_label=None):
    """
    gates: list of (name_html, decision, color, body)   e.g. ("Gate 1 — mixing & continuity","GO",GREEN,"...")
    panels: list of (caption, image_pdf_path)  length up to 6 (2 rows x 3)
    params: list of (key, value) pairs (rendered as 2-col x N rows)
    branching: if True, expects exactly 7 panels = 6 embedding strips + 1 square
               modules panel (last). Draws the 6 strips in a left 3-col x 2-row
               block with the square anchored in the right column spanning both rows.
    """
    if run_label is None:
        try: run_label = run_label_for(os.path.dirname(os.path.abspath(out_pdf)))
        except Exception: run_label = None
    fig = plt.figure(figsize=(8.5, 11)); fig.subplots_adjust(0,0,1,1)
    ax = fig.add_axes([0,0,1,1]); ax.axis('off'); ax.set_xlim(0,1); ax.set_ylim(0,1)
    L, R = 0.07, 0.93; y = 0.965
    # ---- Title + rule ----
    fig.canvas.draw(); _rend0 = fig.canvas.get_renderer(); _inv0 = ax.transData.inverted()
    # draw the run-label pill first (right-aligned), measure it, then shrink the title to clear it
    _Rtitle = R
    if run_label:
        # pill colour encodes status: approved (final/accepted run, n==m) -> green; superseded (n<m) -> red
        _mm = re.search(r'(\d+)\s+of\s+(\d+)', run_label.lower())
        _approved = bool(_mm) and (_mm.group(1) == _mm.group(2))
        _pc  = GREEN if _approved else RED
        _pfc = '#e6f4ea' if _approved else '#fdecea'
        _rl = ax.text(R, y, run_label.upper(), size=11, weight='bold', color=_pc, va='top', ha='right',
                      bbox=dict(boxstyle='round,pad=0.3', fc=_pfc, ec=_pc, lw=0.8))
        fig.canvas.draw()
        _Rtitle = _inv0.transform((_rl.get_window_extent(renderer=_rend0).x0, 0))[0] - 0.03
    _tsz = 19.0
    _tt = ax.text(L, y, title, size=_tsz, weight='bold', va='top')
    _x1 = _inv0.transform((_tt.get_window_extent(renderer=_rend0).x1, 0))[0]
    while _x1 > _Rtitle and _tsz > 11.0:
        _tsz -= 0.5
        _tt.set_size(_tsz)
        fig.canvas.draw()
        _x1 = _inv0.transform((_tt.get_window_extent(renderer=_rend0).x1, 0))[0]
    y -= 0.030
    ax.plot([L,R],[y,y], color='black', lw=1.4); y -= 0.022
    # ---- GO/NO-GO GATES header ----
    ax.text(L, y, "GO / NO-GO GATES", size=13, weight='bold', color=BLUE, va='top'); y -= 0.024
    fig.canvas.draw(); rend = fig.canvas.get_renderer(); inv = ax.transData.inverted()
    gates_start = y
    # ==== measure-then-draw: one balanced font scale for gate bodies + params ====
    BOTTOM_MARGIN = 0.03
    ds_lines = textwrap.wrap(dataset, width=112)
    vd_lines = textwrap.wrap(verdict, width=112)
    # panel grid geometry — panels always FILL their column width (no horizontal gaps)
    imgs = [_png(p) for _,p in panels]
    cap_h = 0.013; row_gap = 0.014
    if branching:
        # 6 embedding strips (left 3-col x 2-row) + square modules (right col, spans both rows)
        sqw0 = 0.235; gapc = 0.012
        strip_cw = (R-L - sqw0 - gapc)/3; pw = strip_cw*0.97
        phs = [pw*(im.size[1]/im.size[0])*(8.5/11.0) for im in imgs[:6]]
        strip_ph = max(phs)
        grid_h = 2*(cap_h + strip_ph) + row_gap
        sq_w = sqw0; sq_ar = imgs[6].size[1]/imgs[6].size[0]
        sq_h = sq_w*sq_ar*(8.5/11.0)
        sq_avail = grid_h - cap_h       # leave caption headroom (matches the strips)
        if sq_h > sq_avail:             # cap square to the caption-adjusted two-row height
            sq_h = sq_avail; sq_w = sq_h/(sq_ar*(8.5/11.0))
    else:
        cols = 4 if len(panels) > 6 else (3 if len(panels) > 2 else max(1, len(panels))); cw = (R-L)/cols; pw = cw*0.94; row_gap = 0.018
        phs  = [pw*(im.size[1]/im.size[0])*(8.5/11.0) for im in imgs]
        row1_h = cap_h + (max(phs[0:cols]) if phs[0:cols] else 0) + row_gap
        row2_h = cap_h + (max(phs[cols:2*cols]) if phs[cols:2*cols] else 0) + row_gap
        grid_h = row1_h + row2_h
    # equal, wide two-column param table
    mid = (L+R)/2; keyw = 0.155
    colx = [L, L+keyw, mid, mid+keyw]
    # value column must WRAP before the next key column starts, with a small gutter
    val_w = (mid - (L+keyw)) - 0.015            # value-column width (page fraction), both equal
    def _cw_chars(fpt, frac): return max(14, int(frac*612/(0.58*fpt)))
    def _measure(f):
        lh = f*0.00167
        pcw = _cw_chars(f, val_w)
        pl = 0
        for i in range(0, len(params), 2):
            a = textwrap.wrap(params[i][1], width=pcw)
            b = textwrap.wrap(params[i+1][1], width=pcw) if i+1 < len(params) else []
            pl += max(1, len(a), len(b))
        nrows = len(params)//2 + (len(params)%2)
        params_h = pl*lh + nrows*0.011
        bottom_h = (0.020 + 0.016 + len(ds_lines)*0.015 + 0.008
                    + 0.016 + len(vd_lines)*0.015 + 0.012 + 0.020 + params_h)
        gcw = _cw_chars(f, (R-L-0.015))
        gl = sum(len(textwrap.wrap(b, width=gcw)) for *_ , b in gates)
        gates_h = len(gates)*0.021 + len(gates)*0.009 + gl*lh
        return gates_h, bottom_h
    chosen = 6.0
    for f in [9.0, 8.5, 8.0, 7.5, 7.0, 6.5, 6.0]:
        gh, bh = _measure(f)
        if (gates_start - gh - 0.022 - grid_h - bh) >= BOTTOM_MARGIN:
            chosen = f; break
    f = chosen; lh = f*0.00167
    # scale the panel grid down to fit the remaining vertical budget (square/tall panels can overrun)
    gh, bh = _measure(f)
    avail_grid = gates_start - gh - 0.022 - bh - BOTTOM_MARGIN
    if grid_h > avail_grid and avail_grid > 0:
        s = avail_grid / grid_h
        pw = pw * s
        phs = [p*s for p in phs]
        if branching:
            strip_ph = max(phs); sq_h = sq_h*s; sq_w = sq_w*s
            grid_h = 2*(cap_h + strip_ph) + row_gap
        else:
            row1_h = cap_h + (max(phs[0:cols]) if phs[0:cols] else 0) + row_gap
            row2_h = cap_h + (max(phs[cols:2*cols]) if phs[cols:2*cols] else 0) + row_gap
            grid_h = row1_h + row2_h
    gcw = _cw_chars(f, (R-L-0.015)); pcw = _cw_chars(f, val_w)
    gname_sz = max(9.5, min(11, f+2.5))
    # ---- draw gates ----
    for name, dec, col, body in gates:
        head = name + "  \u2192  "
        t = ax.text(L, y, head, size=gname_sz, weight='bold', va='top')
        x_dec = inv.transform((t.get_window_extent(renderer=rend).x1, 0))[0]
        ax.text(x_dec, y, dec, size=gname_sz, weight='bold', color=col, va='top')
        y -= 0.021
        for ln in textwrap.wrap(body, width=gcw):
            ax.text(L+0.015, y, ln, size=f, va='top'); y -= lh
        y -= 0.009
    # ---- STEP FIGURES ----
    y -= 0.004
    ax.text(L, y, "STEP FIGURES", size=13, weight='bold', color=BLUE, va='top'); y -= 0.018
    grid_top = y
    if branching:
        strip_cw = (R-L - sq_w - gapc)/3
        strip_row_h = cap_h + strip_ph
        for idx in range(6):
            r = idx//3; c = idx%3
            cx = L + c*strip_cw; cy = grid_top - (0 if r==0 else strip_row_h + row_gap)
            cap = panels[idx][0]
            ax.text(cx+strip_cw/2, cy, cap, size=9, weight='bold', color=BLUE, ha='center', va='top')
            iax = fig.add_axes([cx+(strip_cw-pw)/2, cy-cap_h-strip_ph, pw, strip_ph]); iax.axis('off')
            iax.imshow(imgs[idx])
        # square modules panel — right column. Caption sits at grid_top (va='top',
        # identical to the strip captions); the panel is centered in the space below,
        # capped to grid_h - cap_h so its lower edge never crosses the rule.
        sqx = L + 3*strip_cw + gapc
        cap = panels[6][0]
        ax.text(sqx+sq_w/2, grid_top, cap, size=9, weight='bold', color=BLUE, ha='center', va='top')
        avail = grid_h - cap_h                      # vertical room under the caption
        pad = max(0.0, (avail - sq_h)/2)
        sq_bottom = grid_top - cap_h - pad - sq_h
        iax = fig.add_axes([sqx, sq_bottom, sq_w, sq_h]); iax.axis('off')
        iax.imshow(imgs[6])
    else:
        for idx,(cap, ppath) in enumerate(panels):
            r = idx//cols; c = idx%cols
            cx = L + c*cw; cy = grid_top - (0 if r==0 else row1_h)
            ax.text(cx+cw/2, cy, cap, size=9, weight='bold', color=BLUE, ha='center', va='top')
            ph = phs[idx]
            iax = fig.add_axes([cx+(cw-pw)/2, cy-cap_h-ph, pw, ph]); iax.axis('off')
            iax.imshow(imgs[idx])
    y = grid_top - grid_h - 0.004
    # ---- rule ----
    ax.plot([L,R],[y,y], color=GREY, lw=0.8); y -= 0.020
    # ---- Dataset ----
    ax.text(L, y, "Dataset.", size=10.5, weight='bold', va='top'); y -= 0.016
    for ln in ds_lines:
        ax.text(L, y, ln, size=8.7, va='top'); y -= 0.0150
    y -= 0.008
    # ---- Verdict ----
    ax.text(L, y, "Verdict.", size=10.5, weight='bold', va='top'); y -= 0.016
    for ln in vd_lines:
        ax.text(L, y, ln, size=8.7, va='top'); y -= 0.0150
    y -= 0.012
    # ---- Parameter choices ----
    ax.text(L, y, "Parameter choices", size=12, weight='bold', va='top'); y -= 0.020
    # value columns start at a fixed x, but if a key is wider than its slot, push the
    # value right (measured) so key and value never touch; wrap value to remaining width.
    GUT = 0.012
    def _key_end(x0, ktext):
        t = ax.text(x0, 1.5, ktext, size=f, weight='bold', va='top')  # off-canvas measure
        xe = inv.transform((t.get_window_extent(renderer=rend).x1, 0))[0]
        t.remove(); return xe
    for i in range(0, len(params), 2):
        left = params[i]; right = params[i+1] if i+1 < len(params) else None
        # left column
        ax.text(colx[0], y, left[0], size=f, weight='bold', va='top')
        vx1 = max(colx[1], _key_end(colx[0], left[0]) + GUT)
        w1 = max(10, int((mid - 0.010 - vx1)*612/(0.58*f)))
        lw = textwrap.wrap(left[1], width=w1)
        for j,ln in enumerate(lw):
            ax.text(vx1, y-j*lh, ln, size=f, va='top')
        rw = []
        if right:
            ax.text(colx[2], y, right[0], size=f, weight='bold', va='top')
            vx2 = max(colx[3], _key_end(colx[2], right[0]) + GUT)
            w2 = max(10, int((R - vx2)*612/(0.58*f)))
            rw = textwrap.wrap(right[1], width=w2)
            for j,ln in enumerate(rw):
                ax.text(vx2, y-j*lh, ln, size=f, va='top')
        nlines = max(1, len(lw), len(rw))
        y -= lh*nlines + 0.011
    with PdfPages(out_pdf) as pp:
        pp.savefig(fig)
    plt.close(fig)
    return out_pdf
