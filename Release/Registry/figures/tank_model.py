"""Reference tank model for Registry v0.3.2 (definition decisions, 30 October 2026, section 8).

dN/dt = b (1 - s_r) v N (1 - N/K) - (m + c_a) N + P

Illustrative parameters only; not fitted to any species.
The predation terms s_r (recruits) and c_a (adults) are part of the model but are
zero in every plotted scenario.
Run:  python3 tank_model.py   (writes corrective-dependency-tank-model.png beside this file)
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

K = 1.0        # capacity (stock normalized to capacity)
B = 0.30       # per-capita renewal potential, 1/yr
M = 0.05       # natural loss rate of long-lived adults, 1/yr
V_OPEN = 1.0   # valve open: host access intact
V_SHUT = 0.10  # valve nearly shut: host access obstructed
PUMP = 0.01    # managed renewal (stocking), capacity units/yr
T_END = 150.0
T_RESTORE = 20.0
T_PUMP_OFF = 60.0
N0 = K * (1 - M / (B * V_OPEN))  # start at the healthy equilibrium (~0.83)


def rhs(t, n, v_of_t, p_of_t, s_r=0.0, c_a=0.0):
    v = v_of_t(t)
    p = p_of_t(t)
    return B * (1 - s_r) * v * n * (1 - n / K) - (M + c_a) * n + p


def run(v_of_t, p_of_t, **kw):
    t = np.linspace(0, T_END, 1501)
    sol = solve_ivp(rhs, (0, T_END), [N0], t_eval=t, args=(v_of_t, p_of_t),
                    max_step=0.5, rtol=1e-8, atol=1e-10)
    return sol.t, sol.y[0]


def scenarios():
    shut = lambda t: V_SHUT
    none = lambda t: 0.0
    return {
        "No correction (extinction debt)": run(shut, none),
        "Substitution continues": run(shut, lambda t: PUMP),
        "Substitution stopped at t = 60": run(shut, lambda t: PUMP if t < T_PUMP_OFF else 0.0),
        "Pathway restored at t = 20": run(lambda t: V_OPEN if t >= T_RESTORE else V_SHUT, none),
    }


# Reference palette (dataviz skill, light mode): categorical slots 1-4; ordinal blue ramp.
SURFACE = "#fcfcfb"
TEXT = "#0b0b0b"
TEXT2 = "#52514e"
GRID = "#e4e3df"
CAT = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"]
RAMP = ["#86b6ef", "#2a78d6", "#104281"]


def style(ax, title):
    ax.set_facecolor(SURFACE)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(GRID)
    ax.tick_params(colors=TEXT2, labelsize=8, length=0)
    ax.grid(axis="y", color=GRID, linewidth=0.6)
    ax.set_xlim(0, T_END)
    ax.set_ylim(0, 1.0)
    ax.set_xlabel("Years", color=TEXT2, fontsize=8.5)
    ax.set_title(title, color=TEXT, fontsize=10, loc="left", pad=8)


def main(out=Path(__file__).with_name("corrective-dependency-tank-model.png")):
    fig, (a, b) = plt.subplots(1, 2, figsize=(10, 4.2), dpi=200, facecolor=SURFACE)

    # Panel A: four scenarios
    style(a, "Stock under four scenarios")
    a.set_ylabel("Stock (fraction of capacity)", color=TEXT2, fontsize=8.5)
    labels_y = {}
    for (name, (t, n)), color, ls in zip(scenarios().items(), CAT, ["-", "-", (0, (4, 2)), "-"]):
        a.plot(t, n, color=color, linewidth=1.6, linestyle=ls, label=name, solid_capstyle="round")
        labels_y[name] = n[-1]
    for x, txt in ((T_RESTORE, "valve reopened"), (T_PUMP_OFF, "pump stopped")):
        a.axvline(x, color=TEXT2, linewidth=0.6, linestyle=":")
        a.text(x + 1.5, 0.97, txt, color=TEXT2, fontsize=7, va="top")
    # direct labels at the right edge, nudged apart
    short = {
        "No correction (extinction debt)": "No correction",
        "Substitution continues": "Substitution continues",
        "Substitution stopped at t = 60": "Substitution stopped",
        "Pathway restored at t = 20": "Pathway restored",
    }
    placed = []
    for name, y in sorted(labels_y.items(), key=lambda kv: kv[1]):
        y_lab = y
        for p in placed:
            if abs(y_lab - p) < 0.06:
                y_lab = p + 0.06
        placed.append(y_lab)
        a.text(T_END + 2, y_lab, short[name], color=TEXT, fontsize=7.5, va="center", clip_on=False)
    a.legend(loc="upper right", fontsize=7, frameon=False, labelcolor=TEXT2, bbox_to_anchor=(1.0, 0.72))

    # Panel B: extinction-debt tail lengthens as the net rate approaches zero
    style(b, "Extinction debt: the tail lengthens as net rate nears zero")
    t = np.linspace(0, T_END, 1501)
    for r, color in zip((-0.08, -0.03, -0.01), RAMP):
        n = N0 * np.exp(r * t)
        half = np.log(2) / abs(r)
        b.plot(t, n, color=color, linewidth=1.6, solid_capstyle="round",
               label=f"net rate {r:+.2f}/yr, half-life {half:.0f} yr")
        b.plot([half], [N0 / 2], marker="o", markersize=4.5, color=color,
               markeredgecolor=SURFACE, markeredgewidth=1.2, zorder=3)
        b.text(half + 2.0, N0 / 2 + 0.02, f"{half:.0f} yr", color=TEXT, fontsize=7.5, va="bottom")
    b.axhline(N0 / 2, color=TEXT2, linewidth=0.6, linestyle=":")
    b.text(T_END - 1, N0 / 2 + 0.015, "half of starting stock", color=TEXT2, fontsize=7, va="bottom", ha="right")
    b.legend(loc="upper right", fontsize=7, frameon=False, labelcolor=TEXT2)

    fig.text(0.01, 0.005,
             "Illustrative parameters (b = 0.30/yr, m = 0.05/yr, valve 1.0 open / 0.10 obstructed, pump 0.01/yr); "
             "predation terms s_r and c_a are in the model but set to zero here; not fitted to any species. "
             "Registry v0.3.2, decision record §8.",
             color=TEXT2, fontsize=6.5)
    fig.tight_layout(rect=(0, 0.03, 0.93, 1))
    fig.subplots_adjust(wspace=0.42)
    fig.savefig(out, facecolor=SURFACE)
    return out


if __name__ == "__main__":
    print(main())
