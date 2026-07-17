"""Generate every figure for *Calculus, Intuitively* as SVG.

Two kinds of figure live here. **Diagrams** (concepts) are hand-authored SVG
emitted from Python string templates. **Plots** (anything quantitative) are
matplotlib, saved transparent with `svg.fonttype: "none"` so their text inherits
the page fonts. Both draw from the palette constants below, which mirror
`assets/style.css` — keep them in sync.

Run with `python figures/make_figures.py`. Each `fig_*()` returns the path it
wrote and is listed in `FIGURES`; `main()` runs them all. The cover and icons
carry the book's visual identity (an abstract chain of connected nodes) and are
written to the assets root.
"""

from __future__ import annotations

import textwrap
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "assets" / "figures"
ASSETS_DIR = ROOT / "assets"

# The book's palette, mirrored from assets/style.css. Keep these in sync.
PAPER = "#f4f3ee"
INK = "#17181b"
INK_SOFT = "#3b3d42"
MUTED = "#6a6d73"
RULE = "#e4e3dd"
RULE_STRONG = "#cfcdc4"
ACCENT = "#274b6d"
ACCENT_SOFT = "#eaf0f6"
AMBER = "#9c6b12"
VIOLET = "#6b4f9c"
BRICK = "#b04a3f"

SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
SERIF = "'Charter', 'Iowan Old Style', 'Palatino Linotype', Palatino, Georgia, serif"
MONO = "'SF Mono', 'SFMono-Regular', ui-monospace, Menlo, Consolas, monospace"


def write_svg(name: str, svg: str) -> Path:
    """Write a raw SVG string to the figures directory and return its path."""
    assert name.endswith(".svg"), f"Figure name must end in .svg, got '{name}'."
    assert svg.lstrip().startswith("<svg"), f"Figure '{name}' is not an SVG document."
    path = OUTPUT_DIR / name
    path.write_text(svg, encoding="utf-8")
    return path


def write_root_asset(name: str, svg: str) -> Path:
    """Write a raw SVG string to the assets root (cover, icon) and return its path."""
    assert name.endswith(".svg"), f"Asset name must end in .svg, got '{name}'."
    assert svg.lstrip().startswith("<svg"), f"Asset '{name}' is not an SVG document."
    path = ASSETS_DIR / name
    path.write_text(svg, encoding="utf-8")
    return path


def svg_doc(width: float, height: float, label: str, body: list[str]) -> str:
    """Wrap SVG body elements in a document with the book's default font.

    `label` becomes the accessible description; keep it plain ASCII so it needs
    no escaping. `body` is the list of element strings, in draw order.
    """
    head = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'font-family="{SANS}" role="img" aria-label="{label}">'
    )
    return "\n".join([head, *body, "</svg>"])


def arrow_marker(color: str, name: str) -> str:
    """Return a `<defs>` block holding one triangular arrowhead marker."""
    return (
        f'<defs><marker id="{name}" viewBox="0 0 10 10" refX="9" refY="5" '
        f'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{color}"/></marker></defs>'
    )


def node_box(
    x: float,
    y: float,
    w: float,
    h: float,
    text: str,
    *,
    fill: str = "#ffffff",
    stroke: str = RULE_STRONG,
    text_fill: str = INK,
    font_size: float = 12,
    weight: int = 400,
) -> list[str]:
    """Return a rounded rectangle with centered text: the book's labelled chip."""
    stroke_attr = "none" if stroke == "none" else stroke
    return [
        f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="6" '
        f'fill="{fill}" stroke="{stroke_attr}"/>',
        f'<text x="{x + w / 2:.1f}" y="{y + h / 2 + font_size * 0.35:.1f}" '
        f'font-size="{font_size}" font-weight="{weight}" text-anchor="middle" '
        f'fill="{text_fill}">{text}</text>',
    ]


def eyebrow(x: float, y: float, text: str, fill: str = MUTED) -> str:
    """Return a small uppercase section label, as used across the diagrams."""
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-size="11" font-weight="700" '
        f'fill="{fill}" letter-spacing="1">{text}</text>'
    )


def style_plot() -> None:
    """Apply the book's typographic style to matplotlib's global state."""
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["DejaVu Sans", "Helvetica", "Arial"],
            "font.size": 9,
            "text.color": INK,
            "axes.edgecolor": RULE_STRONG,
            "axes.labelcolor": INK_SOFT,
            "axes.labelsize": 9,
            "axes.titlesize": 10,
            "axes.titleweight": "bold",
            "axes.spines.top": False,
            "axes.spines.right": False,
            "xtick.color": MUTED,
            "ytick.color": MUTED,
            "xtick.labelsize": 8,
            "ytick.labelsize": 8,
            "grid.color": RULE,
            "grid.linewidth": 0.8,
            "legend.frameon": False,
            "legend.fontsize": 8,
            "svg.fonttype": "none",  # Keep text as text so it inherits page fonts.
        }
    )


def save_plot(fig: plt.Figure, name: str) -> Path:
    """Save a matplotlib figure as a transparent SVG and close it."""
    assert name.endswith(".svg"), f"Figure name must end in .svg, got '{name}'."
    path = OUTPUT_DIR / name
    fig.savefig(path, format="svg", transparent=True, bbox_inches="tight")
    plt.close(fig)
    return path


# ---------------------------------------------------------------------------
# Chapter figures. Static SVG/matplotlib figures live here; interactive figures
# are separate (see assets/widgets.js). Add each new fig_*() to the FIGURES
# tuple at the bottom.
# ---------------------------------------------------------------------------


def fig_derivative_pair() -> Path:
    """Plot f(x) = x^2 and its derivative f'(x) = 2x on shared axes."""
    import numpy as np

    style_plot()
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    xs = np.linspace(-2.4, 2.4, 400)
    ax.plot(xs, xs**2, color=INK, linewidth=2.2, label="f(x) = x²  (height)")
    ax.plot(xs, 2 * xs, color=ACCENT, linewidth=2.2, label="f'(x) = 2x  (slope)")

    ax.axhline(0, color=RULE_STRONG, linewidth=1.0)
    ax.axvline(0, color=RULE_STRONG, linewidth=1.0)
    # Mark where the derivative crosses zero: the parabola's flat bottom.
    ax.plot([0], [0], marker="o", color=AMBER, markersize=6, zorder=5)
    ax.annotate(
        "slope 0 at the bottom",
        xy=(0, 0),
        xytext=(0.35, -2.6),
        color=AMBER,
        fontsize=8,
    )

    ax.set_xlim(-2.4, 2.4)
    ax.set_ylim(-3.2, 6.0)
    ax.set_xlabel("x")
    ax.legend(loc="upper center")
    return save_plot(fig, "derivative-pair.svg")


def fig_function_machine() -> Path:
    """A function drawn as a machine: input in, fixed rule, one output out."""
    w, h = 560, 340
    body = [
        arrow_marker(INK_SOFT, "fm-arrow"),
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="none"/>',
        eyebrow(30, 40, "A FUNCTION IS A MACHINE"),
    ]

    cy = 130  # Center height of the main flow.

    # Input chip.
    body += node_box(
        30,
        cy - 26,
        92,
        52,
        "input 3",
        fill="#ffffff",
        stroke=RULE_STRONG,
        text_fill=INK,
        font_size=15,
        weight=600,
    )
    # Arrow into the machine.
    body.append(
        f'<line x1="126" y1="{cy}" x2="196" y2="{cy}" stroke="{INK_SOFT}" '
        f'stroke-width="2" marker-end="url(#fm-arrow)"/>'
    )
    # The machine box.
    body.append(
        f'<rect x="200" y="{cy - 58}" width="160" height="116" rx="10" '
        f'fill="{ACCENT_SOFT}" stroke="{ACCENT}" stroke-width="2"/>'
    )
    body.append(
        f'<text x="280" y="{cy - 22}" font-size="13" font-weight="700" '
        f'fill="{ACCENT}" text-anchor="middle" letter-spacing="1">MACHINE f</text>'
    )
    body.append(
        f'<text x="280" y="{cy + 12}" font-size="20" font-weight="700" '
        f'fill="{INK}" text-anchor="middle">f(x) = 2x + 1</text>'
    )
    body.append(
        f'<text x="280" y="{cy + 40}" font-size="12.5" '
        f'fill="{MUTED}" text-anchor="middle">double it, then add one</text>'
    )
    # Arrow out of the machine.
    body.append(
        f'<line x1="364" y1="{cy}" x2="434" y2="{cy}" stroke="{INK_SOFT}" '
        f'stroke-width="2" marker-end="url(#fm-arrow)"/>'
    )
    # Output chip.
    body += node_box(
        438,
        cy - 26,
        92,
        52,
        "output 7",
        fill=AMBER,
        stroke="none",
        text_fill="#ffffff",
        font_size=15,
        weight=600,
    )

    # A little table of more pairs beneath the flow.
    ty = 250
    body.append(
        f'<text x="30" y="{ty}" font-size="12.5" font-weight="700" '
        f'fill="{INK_SOFT}">More of the same rule:</text>'
    )
    pairs = [("0", "1"), ("1", "3"), ("3", "7"), ("5", "11")]
    x0 = 30
    for i, (a, b) in enumerate(pairs):
        px = x0 + i * 132
        py = ty + 30
        body.append(
            f'<text x="{px}" y="{py}" font-size="15" fill="{INK}">'
            f"f({a}) = {b}</text>"
        )
    svg = svg_doc(
        w,
        h,
        "Function machine: input 3 enters the rule f of x equals 2x plus 1 and output 7 leaves.",
        body,
    )
    return write_svg("function-machine.svg", svg)


def fig_graph_pairs() -> Path:
    """Read a graph: up from an input to the curve, across to the height."""
    import numpy as np

    style_plot()
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    xs = np.linspace(-3.4, 3.4, 400)
    ax.plot(xs, xs**2, color=INK, linewidth=2.4, zorder=3)

    ax.axhline(0, color=RULE_STRONG, linewidth=1.0)
    ax.axvline(0, color=RULE_STRONG, linewidth=1.0)

    pairs = [(-1, 1), (2, 4), (3, 9)]
    for a, b in pairs:
        # Dashed guide: up from the input, then across to the height.
        ax.plot(
            [a, a], [0, b], color=ACCENT, linewidth=1.2, linestyle=(0, (4, 3)), zorder=2
        )
        ax.plot(
            [a, 0], [b, b], color=ACCENT, linewidth=1.2, linestyle=(0, (4, 3)), zorder=2
        )
        ax.plot([a], [b], marker="o", color=AMBER, markersize=7, zorder=5)

    # Label the worked pair (2, 4) without crowding the curve.
    ax.annotate(
        "f(2) = 4",
        xy=(2, 4),
        xytext=(2.35, 2.1),
        color=AMBER,
        fontsize=9.5,
        fontweight="bold",
    )
    ax.annotate("input 2", xy=(2, 0), xytext=(2.05, -1.15), color=MUTED, fontsize=8.5)
    ax.annotate("height 4", xy=(0, 4), xytext=(-3.25, 4.35), color=MUTED, fontsize=8.5)

    ax.set_xlim(-3.6, 3.8)
    ax.set_ylim(-1.8, 10.2)
    ax.set_xlabel("input (x)")
    ax.set_ylabel("output (y)")
    ax.set_xticks([-3, -2, -1, 1, 2, 3])
    ax.set_yticks([2, 4, 6, 8, 10])
    return save_plot(fig, "graph-pairs.svg")


def fig_rise_over_run() -> Path:
    """Rise over run: a right triangle under a straight line gives its slope."""
    import numpy as np

    style_plot()
    fig, ax = plt.subplots(figsize=(5.6, 3.8))

    # Line f(x) = 0.5 x + 1.
    m, b = 0.5, 1.0
    xs = np.linspace(-0.6, 6.4, 200)
    ax.plot(xs, m * xs + b, color=INK, linewidth=2.4, zorder=3)

    ax.axhline(0, color=RULE_STRONG, linewidth=1.0)
    ax.axvline(0, color=RULE_STRONG, linewidth=1.0)

    # Two points on the line.
    x1, x2 = 1.0, 5.0
    y1, y2 = m * x1 + b, m * x2 + b
    for xx, yy in [(x1, y1), (x2, y2)]:
        ax.plot([xx], [yy], marker="o", color=ACCENT, markersize=7, zorder=5)

    # Run leg (horizontal) and rise leg (vertical) forming the triangle.
    ax.plot([x1, x2], [y1, y1], color=AMBER, linewidth=2.2, zorder=4)
    ax.plot([x2, x2], [y1, y2], color=AMBER, linewidth=2.2, zorder=4)

    ax.annotate(
        "run = 4",
        xy=((x1 + x2) / 2, y1),
        xytext=((x1 + x2) / 2 - 0.5, y1 - 0.55),
        color=AMBER,
        fontsize=10,
        fontweight="bold",
    )
    ax.annotate(
        "rise = 2",
        xy=(x2, (y1 + y2) / 2),
        xytext=(x2 + 0.15, (y1 + y2) / 2 - 0.15),
        color=AMBER,
        fontsize=10,
        fontweight="bold",
    )
    ax.annotate(
        "slope = rise / run = 2/4 = 1/2",
        xy=(0.9, 3.9),
        xytext=(0.2, 4.15),
        color=INK_SOFT,
        fontsize=10,
        fontweight="bold",
    )

    ax.set_xlim(-0.8, 7.0)
    ax.set_ylim(-0.9, 5.0)
    ax.set_xlabel("across")
    ax.set_ylabel("up")
    ax.set_xticks([1, 2, 3, 4, 5, 6])
    ax.set_yticks([1, 2, 3, 4])
    return save_plot(fig, "rise-over-run.svg")


def fig_limit_hole() -> Path:
    """Plot y = x + 1 with a removable hole at (1, 2) and inward approach arrows."""
    import numpy as np

    style_plot()
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    xs = np.linspace(-0.4, 2.4, 400)
    ax.plot(xs, xs + 1, color=INK, linewidth=2.2)

    # The forbidden input: the function is absent here, drawn as an open circle.
    ax.plot(
        [1],
        [2],
        marker="o",
        markersize=9,
        markerfacecolor="white",
        markeredgecolor=ACCENT,
        markeredgewidth=2.0,
        zorder=6,
    )

    # Arrows running along the line, closing in on the hole from both sides.
    ax.annotate(
        "",
        xy=(0.86, 1.86),
        xytext=(0.3, 1.3),
        arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=2.0),
    )
    ax.annotate(
        "",
        xy=(1.14, 2.14),
        xytext=(1.7, 2.7),
        arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=2.0),
    )
    ax.text(0.28, 1.10, "from the left", color=ACCENT, fontsize=8, ha="left")
    ax.text(1.72, 2.64, "from the right", color=ACCENT, fontsize=8, ha="left")

    # Dashed guides from the hole to the axes.
    ax.plot(
        [1, 1],
        [0, 2],
        color=RULE_STRONG,
        linewidth=1.0,
        linestyle=(0, (4, 3)),
        zorder=1,
    )
    ax.plot(
        [-0.4, 1],
        [2, 2],
        color=RULE_STRONG,
        linewidth=1.0,
        linestyle=(0, (4, 3)),
        zorder=1,
    )
    ax.text(1.06, 2.30, "limit = 2", color=AMBER, fontsize=9, fontweight="bold")

    ax.set_xlim(-0.4, 2.4)
    ax.set_ylim(0, 3.4)
    ax.set_xlabel("x")
    ax.set_xticks([1])
    ax.set_xticklabels(["1"])
    ax.set_yticks([2])
    ax.set_yticklabels(["2"])
    return save_plot(fig, "limit-hole.svg")


def fig_limit_failures() -> Path:
    """Contrast a clean limit, a jump, and a blow-up in three small panels."""
    import numpy as np

    style_plot()
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.7))

    # Panel 1: a clean two-sided approach — the limit exists.
    ax = axes[0]
    xs = np.linspace(-1.0, 1.0, 200)
    ax.plot(xs, 1.4 - 0.6 * xs**2, color=INK, linewidth=2.0)
    ax.plot([0], [1.4], marker="o", markersize=7, color=ACCENT, zorder=5)
    ax.annotate(
        "",
        xy=(-0.12, 1.39),
        xytext=(-0.55, 1.22),
        arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=1.6),
    )
    ax.annotate(
        "",
        xy=(0.12, 1.39),
        xytext=(0.55, 1.22),
        arrowprops=dict(arrowstyle="-|>", color=ACCENT, lw=1.6),
    )
    ax.set_title("limit exists", color=INK)
    ax.set_ylim(0, 2)

    # Panel 2: a jump — the two sides head for different heights.
    ax = axes[1]
    xl = np.linspace(-1.0, -0.02, 100)
    xr = np.linspace(0.02, 1.0, 100)
    ax.plot(xl, 0.7 + 0.2 * xl, color=INK, linewidth=2.0)
    ax.plot(xr, 1.4 + 0.2 * xr, color=INK, linewidth=2.0)
    ax.plot(
        [0],
        [0.7],
        marker="o",
        markersize=7,
        markerfacecolor="white",
        markeredgecolor=BRICK,
        markeredgewidth=1.8,
        zorder=5,
    )
    ax.plot(
        [0],
        [1.4],
        marker="o",
        markersize=7,
        markerfacecolor="white",
        markeredgecolor=BRICK,
        markeredgewidth=1.8,
        zorder=5,
    )
    ax.set_title("a jump", color=INK)
    ax.set_ylim(0, 2)

    # Panel 3: a blow-up — the output escapes upward without bound.
    ax = axes[2]
    xl = np.linspace(-1.0, -0.12, 100)
    xr = np.linspace(0.12, 1.0, 100)
    ax.plot(xl, 0.02 / xl**2, color=INK, linewidth=2.0)
    ax.plot(xr, 0.02 / xr**2, color=INK, linewidth=2.0)
    ax.axvline(0, color=RULE_STRONG, linewidth=1.0, linestyle=(0, (4, 3)))
    ax.set_title("a blow-up", color=INK)
    ax.set_ylim(0, 2)

    for ax in axes:
        ax.set_xticks([0])
        ax.set_xticklabels(["a"])
        ax.set_yticks([])
        ax.set_xlim(-1.0, 1.0)
        ax.axhline(0, color=RULE_STRONG, linewidth=0.8)

    fig.tight_layout()
    return save_plot(fig, "limit-failures.svg")


def fig_continuity_condition() -> Path:
    """A continuous curve approaching and landing on the very point it aims at."""
    import numpy as np

    def curve(x):
        return 0.35 * (x - 1.4) ** 3 - 0.6 * (x - 1.4) + 2.4

    style_plot()
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    xs = np.linspace(-0.3, 3.3, 400)
    ax.plot(xs, curve(xs), color=INK, linewidth=2.2)

    a = 2.1
    fa = curve(a)

    # Dashed guides from the point to each axis.
    ax.plot([a, a], [0, fa], color=RULE_STRONG, linewidth=1.0, linestyle=(0, (4, 3)))
    ax.plot(
        [-0.3, a], [fa, fa], color=RULE_STRONG, linewidth=1.0, linestyle=(0, (4, 3))
    )

    # Short arrows creeping in along the curve from each side.
    for x_from in (a - 0.6, a + 0.6):
        ax.annotate(
            "",
            xy=(a, fa),
            xytext=(x_from, curve(x_from)),
            arrowprops=dict(arrowstyle="->", color=ACCENT, lw=1.8),
        )

    ax.plot([a], [fa], marker="o", color=AMBER, markersize=9, zorder=6)

    ax.annotate(
        "approach\nfrom the left",
        xy=(a - 0.6, curve(a - 0.6)),
        xytext=(0.55, 3.9),
        color=ACCENT,
        fontsize=8,
        ha="center",
    )
    ax.annotate(
        "approach\nfrom the right",
        xy=(a + 0.6, curve(a + 0.6)),
        xytext=(3.05, 1.15),
        color=ACCENT,
        fontsize=8,
        ha="center",
    )
    ax.annotate(
        "both sides land on f(a)",
        xy=(a, fa),
        xytext=(a - 0.1, fa + 1.05),
        color=AMBER,
        fontsize=8,
        ha="center",
    )

    ax.set_xticks([a])
    ax.set_xticklabels(["a"])
    ax.set_yticks([fa])
    ax.set_yticklabels(["f(a)"])
    ax.set_xlim(-0.3, 3.5)
    ax.set_ylim(0, 5.4)
    ax.spines["left"].set_visible(True)
    return save_plot(fig, "continuity-condition.svg")


def fig_continuity_breaks() -> Path:
    """Three panels side by side: a removable hole, a jump, and a blow-up."""
    import numpy as np

    style_plot()
    fig, axes = plt.subplots(1, 3, figsize=(7.6, 2.9))

    # Panel A: removable hole — one point missing from an otherwise smooth line.
    ax = axes[0]
    xs = np.linspace(-2.2, 2.2, 400)
    ax.plot(xs, 0.5 * xs + 1.6, color=INK, linewidth=2.0)
    a = 0.6
    ax.plot(
        [a],
        [0.5 * a + 1.6],
        marker="o",
        markersize=8,
        markerfacecolor="white",
        markeredgecolor=INK,
        markeredgewidth=1.8,
        zorder=6,
    )
    ax.set_title("Removable hole", color=INK_SOFT)
    ax.set_xlim(-2.4, 2.4)
    ax.set_ylim(0, 3.2)

    # Panel B: jump — two sides heading to different heights.
    ax = axes[1]
    xl = np.linspace(-2.2, 0.0, 200)
    xr = np.linspace(0.0, 2.2, 200)
    ax.plot(xl, 0.35 * xl + 1.1, color=INK, linewidth=2.0)
    ax.plot(xr, 0.35 * xr + 2.15, color=INK, linewidth=2.0)
    ax.plot(
        [0],
        [1.1],
        marker="o",
        markersize=8,
        markerfacecolor=INK,
        markeredgecolor=INK,
        zorder=6,
    )
    ax.plot(
        [0],
        [2.15],
        marker="o",
        markersize=8,
        markerfacecolor="white",
        markeredgecolor=INK,
        markeredgewidth=1.8,
        zorder=6,
    )
    ax.set_title("Jump", color=INK_SOFT)
    ax.set_xlim(-2.4, 2.4)
    ax.set_ylim(0, 3.2)

    # Panel C: blow-up — the curve races a vertical asymptote to infinity.
    ax = axes[2]
    xn = np.linspace(-2.2, -0.16, 200)
    xp = np.linspace(0.16, 2.2, 200)
    ax.plot(xn, 0.4 / xn + 1.6, color=INK, linewidth=2.0)
    ax.plot(xp, 0.4 / xp + 1.6, color=INK, linewidth=2.0)
    ax.axvline(0.0, color=BRICK, linewidth=1.3, linestyle=(0, (4, 3)))
    ax.set_title("Blow-up", color=INK_SOFT)
    ax.set_xlim(-2.4, 2.4)
    ax.set_ylim(0, 3.2)

    for ax in axes:
        ax.set_xticks([])
        ax.set_yticks([])
        ax.axhline(0, color=RULE_STRONG, linewidth=0.9)

    fig.subplots_adjust(wspace=0.18)
    return save_plot(fig, "continuity-breaks.svg")


def fig_intermediate_value() -> Path:
    """A continuous curve forced to cross a target height between its endpoints."""
    import numpy as np

    style_plot()
    fig, ax = plt.subplots(figsize=(6.0, 3.6))
    xs = np.linspace(0.5, 4.5, 400)
    ys = 0.9 + 0.9 * (xs - 0.5) - 0.28 * np.sin(1.6 * (xs - 0.5))
    ax.plot(xs, ys, color=INK, linewidth=2.2)

    a, b = 0.5, 4.5
    fa, fb = ys[0], ys[-1]
    N = 2.6
    c = xs[int(np.argmin(np.abs(ys - N)))]

    ax.plot([a, b], [0, 0], color=RULE_STRONG, linewidth=0.9)
    ax.axhline(N, color=ACCENT, linewidth=1.2, linestyle=(0, (4, 3)))
    ax.plot([c, c], [0, N], color=RULE_STRONG, linewidth=1.0, linestyle=(0, (4, 3)))

    ax.plot([a], [fa], marker="o", color=INK, markersize=7, zorder=6)
    ax.plot([b], [fb], marker="o", color=INK, markersize=7, zorder=6)
    ax.plot([c], [N], marker="o", color=AMBER, markersize=9, zorder=7)

    ax.annotate(
        "f(a)", xy=(a, fa), xytext=(a + 0.12, fa + 0.35), color=INK_SOFT, fontsize=9
    )
    ax.annotate(
        "f(b)", xy=(b, fb), xytext=(b - 0.6, fb - 0.1), color=INK_SOFT, fontsize=9
    )
    ax.annotate(
        "target height N",
        xy=(0.6, N),
        xytext=(0.6, N + 0.32),
        color=ACCENT,
        fontsize=9,
    )
    ax.annotate(
        "crossing guaranteed",
        xy=(c, N),
        xytext=(c + 0.15, N - 1.25),
        color=AMBER,
        fontsize=8,
        ha="center",
    )

    ax.set_xticks([a, c, b])
    ax.set_xticklabels(["a", "c", "b"])
    ax.set_yticks([])
    ax.set_xlim(0.2, 4.9)
    ax.set_ylim(0, 5.2)
    ax.spines["left"].set_visible(False)
    return save_plot(fig, "intermediate-value.svg")


def fig_change_and_accumulation() -> Path:
    """Contrast the two questions: steepness at a point vs. area beneath a curve."""
    import numpy as np

    style_plot()
    fig, (axl, axr) = plt.subplots(1, 2, figsize=(6.6, 3.2))
    xs = np.linspace(0, 5, 400)

    def f(x):
        return 0.18 * x**2 + 0.4 * x + 0.6

    # Left: steepness at a single point (the derivative).
    axl.plot(xs, f(xs), color=INK, linewidth=2.2)
    x0 = 3.2
    slope = 0.36 * x0 + 0.4  # f'(x0).
    tx = np.linspace(x0 - 1.4, x0 + 1.4, 2)
    axl.plot(tx, f(x0) + slope * (tx - x0), color=ACCENT, linewidth=2.0)
    axl.plot([x0], [f(x0)], marker="o", color=ACCENT, markersize=6, zorder=5)
    axl.set_title("how fast", color=INK)
    axl.text(
        0.5,
        0.93,
        "steepness at a point\n= the derivative",
        transform=axl.transAxes,
        ha="center",
        va="top",
        fontsize=8.5,
        color=ACCENT,
    )

    # Right: area beneath the curve (the integral).
    axr.plot(xs, f(xs), color=INK, linewidth=2.2)
    axr.fill_between(xs, 0, f(xs), color=AMBER, alpha=0.18)
    axr.set_title("how much", color=INK)
    axr.text(
        0.5,
        0.93,
        "area beneath the curve\n= the integral",
        transform=axr.transAxes,
        ha="center",
        va="top",
        fontsize=8.5,
        color=AMBER,
    )

    for ax in (axl, axr):
        ax.set_xlim(0, 5)
        ax.set_ylim(0, f(5) * 1.05)
        ax.set_xticks([])
        ax.set_yticks([])

    fig.tight_layout()
    return save_plot(fig, "change-and-accumulation.svg")


def fig_two_moves() -> Path:
    """Show calculus's two moves: zoom-until-straight and slice-and-add."""
    import numpy as np
    from mpl_toolkits.axes_grid1.inset_locator import inset_axes, mark_inset

    style_plot()
    fig, (axl, axr) = plt.subplots(1, 2, figsize=(6.6, 3.2))

    # Left: zoom in until the curve looks straight.
    xs = np.linspace(0, 5, 400)

    def g(x):
        return 0.5 * np.sin(0.7 * x) + 0.16 * x + 1.6

    axl.plot(xs, g(xs), color=INK, linewidth=2.2)
    x0 = 1.0
    axl.plot([x0], [g(x0)], marker="o", color=ACCENT, markersize=5, zorder=5)
    axl.set_title("zoom in until curved looks straight", color=INK, fontsize=9)
    axin = inset_axes(axl, width="40%", height="40%", loc="lower right", borderpad=1.1)
    zw = 0.04  # A tiny window, so the magnified piece is visibly straight.
    zx = np.linspace(x0 - zw, x0 + zw, 60)
    axin.plot(zx, g(zx), color=ACCENT, linewidth=2.4)
    axin.set_xlim(x0 - zw, x0 + zw)
    axin.set_xticks([])
    axin.set_yticks([])
    axin.set_facecolor("white")  # A solid panel so the magnifier reads clearly.
    for spine in axin.spines.values():
        spine.set_visible(
            True
        )  # style_plot() hides top/right; a magnifier needs a full box.
        spine.set_edgecolor(INK_SOFT)
        spine.set_linewidth(1.2)
    axin.text(
        0.5,
        0.86,
        "zoomed in",
        transform=axin.transAxes,
        ha="center",
        va="top",
        fontsize=7,
        color=MUTED,
    )
    mark_inset(axl, axin, loc1=2, loc2=1, fc="none", ec=MUTED, lw=1.0)
    axl.set_xlim(0, 5)
    axl.set_ylim(0, g(xs).max() * 1.12)
    axl.set_xticks([])
    axl.set_yticks([])

    # Right: slice thin and add up.
    xr = np.linspace(0, 5, 400)

    def h(x):
        return 0.16 * x**2 + 0.3 * x + 0.8

    axr.plot(xr, h(xr), color=INK, linewidth=2.2)
    edges = np.linspace(0, 5, 13)
    lefts = edges[:-1]
    widths = np.diff(edges)
    heights = h(lefts + widths / 2)
    axr.bar(
        lefts,
        heights,
        width=widths,
        align="edge",
        color=AMBER,
        alpha=0.22,
        edgecolor=AMBER,
        linewidth=0.8,
    )
    axr.set_title("slice thin and add up", color=INK, fontsize=9)
    axr.set_xlim(0, 5)
    axr.set_ylim(0, h(5) * 1.08)
    axr.set_xticks([])
    axr.set_yticks([])

    fig.subplots_adjust(left=0.02, right=0.98, top=0.9, bottom=0.04, wspace=0.12)
    return save_plot(fig, "two-moves.svg")


def fig_inverse_pair() -> Path:
    """Diagram: accumulation and rate as inverse operations (differentiate/integrate)."""
    w, h = 680, 300
    body = [
        f'<rect width="{w}" height="{h}" fill="none"/>',
        arrow_marker(ACCENT, "arrow-inverse"),
    ]

    # Two boxes: "how much" on the left, "how fast" on the right.
    lx, rx, by, bw, bh = 50, 400, 100, 230, 100
    for x, eb, l1, l2 in (
        (lx, "HOW MUCH", "Total accumulated", "(the integral)"),
        (rx, "HOW FAST", "Rate of change", "(the derivative)"),
    ):
        body.append(
            f'<rect x="{x}" y="{by}" width="{bw}" height="{bh}" rx="8" '
            f'fill="#ffffff" stroke="{RULE_STRONG}"/>'
        )
        cx = x + bw / 2
        body.append(eyebrow(cx - 44, by + 28, eb))
        body.append(
            f'<text x="{cx:.1f}" y="{by + 58:.1f}" font-size="16" font-weight="600" '
            f'text-anchor="middle" fill="{INK}">{l1}</text>'
        )
        body.append(
            f'<text x="{cx:.1f}" y="{by + 80:.1f}" font-size="13" '
            f'text-anchor="middle" fill="{MUTED}">{l2}</text>'
        )

    # Top arc: differentiate, left box to right box.
    body.append(
        f'<path d="M {lx + bw + 6} {by + 26} C 320 78, 360 78, {rx - 6} {by + 26}" '
        f'fill="none" stroke="{ACCENT}" stroke-width="2" marker-end="url(#arrow-inverse)"/>'
    )
    body.append(
        f'<text x="340" y="70" font-size="13" font-weight="600" text-anchor="middle" '
        f'fill="{ACCENT}">differentiate</text>'
    )
    # Bottom arc: integrate, right box to left box.
    body.append(
        f'<path d="M {rx - 6} {by + bh - 26} C 360 {by + bh + 34}, 320 {by + bh + 34}, '
        f'{lx + bw + 6} {by + bh - 26}" fill="none" stroke="{ACCENT}" stroke-width="2" '
        f'marker-end="url(#arrow-inverse)"/>'
    )
    body.append(
        f'<text x="340" y="{by + bh + 30:.0f}" font-size="13" font-weight="600" '
        f'text-anchor="middle" fill="{ACCENT}">integrate</text>'
    )
    body.append(
        f'<text x="340" y="{by + bh + 78:.0f}" font-size="13" text-anchor="middle" '
        f'fill="{INK_SOFT}">each undoes the other</text>'
    )

    label = "Diagram: total accumulated and rate of change linked by two arrows, differentiate and integrate, each undoing the other."
    return write_svg("inverse-pair.svg", svg_doc(w, h, label, body))


# ---------------------------------------------------------------------------
# The cover and the icons.
#
# The book's identity is a curve with a straight tangent line grazing it at one
# point, over a lightly shaded area — the derivative (the tangent) and the
# integral (the area) in a single mark, which is the whole book in a picture.
# ---------------------------------------------------------------------------


def _curve_geometry(
    x_left: float,
    x_right: float,
    y_bottom: float,
    y_top: float,
    t0: float = 0.66,
    n: int = 80,
) -> tuple[
    list[tuple[float, float]], list[tuple[float, float]], tuple[float, float], float
]:
    """Return the motif geometry in a box: the curve points, the tangent segment
    endpoints, the tangency point, and the baseline y.

    The curve is the parabola value = t**2 for t in [0, 1] mapped into the box
    (y grows downward, as in SVG). The tangent is taken at t0, where the parabola
    has slope 2*t0. All coordinates are in the target coordinate space, so the
    same geometry drives the SVG cover/icon and the matplotlib touch icon.
    """
    span_x = x_right - x_left
    span_y = y_bottom - y_top

    def cx(t: float) -> float:
        return x_left + t * span_x

    def cy(value: float) -> float:
        return y_bottom - value * span_y

    curve = [(cx(i / n), cy((i / n) ** 2)) for i in range(n + 1)]
    value0 = t0 * t0
    slope = 2 * t0
    dt = 0.26
    t_a, t_b = t0 - dt, t0 + dt
    tangent = [
        (cx(t_a), cy(value0 + slope * (t_a - t0))),
        (cx(t_b), cy(value0 + slope * (t_b - t0))),
    ]
    return curve, tangent, (cx(t0), cy(value0)), cy(0.0)


def curve_tangent_svg(
    x_left: float,
    x_right: float,
    y_bottom: float,
    y_top: float,
    *,
    stroke_w: float,
    node_r: float,
    axes: bool = False,
) -> str:
    """Emit the identity motif — shaded area, curve, tangent line, and dot."""
    curve, tangent, dot, baseline = _curve_geometry(x_left, x_right, y_bottom, y_top)
    curve_d = " L ".join(f"{x:.1f} {y:.1f}" for x, y in curve)
    parts = []
    if axes:
        parts.append(
            f'<line x1="{x_left:.1f}" y1="{baseline:.1f}" x2="{x_right + 14:.1f}" '
            f'y2="{baseline:.1f}" stroke="{RULE_STRONG}" stroke-width="1.5"/>'
        )
        parts.append(
            f'<line x1="{x_left:.1f}" y1="{baseline:.1f}" x2="{x_left:.1f}" '
            f'y2="{y_top - 14:.1f}" stroke="{RULE_STRONG}" stroke-width="1.5"/>'
        )
    # Shaded area under the curve.
    parts.append(
        f'<path d="M {x_left:.1f} {baseline:.1f} L {curve_d} '
        f'L {x_right:.1f} {baseline:.1f} Z" fill="{ACCENT_SOFT}" stroke="none"/>'
    )
    # The curve itself.
    parts.append(
        f'<path d="M {curve_d}" fill="none" stroke="{ACCENT}" '
        f'stroke-width="{stroke_w:.2f}" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    # The tangent line, then the tangency point on top.
    (tax, tay), (tbx, tby) = tangent
    parts.append(
        f'<line x1="{tax:.1f}" y1="{tay:.1f}" x2="{tbx:.1f}" y2="{tby:.1f}" '
        f'stroke="{AMBER}" stroke-width="{stroke_w:.2f}" stroke-linecap="round"/>'
    )
    parts.append(
        f'<circle cx="{dot[0]:.1f}" cy="{dot[1]:.1f}" r="{node_r:.1f}" fill="{AMBER}"/>'
    )
    return "\n".join(parts)


def fig_cover() -> Path:
    """The book cover: title over the curve-and-tangent motif, framed like a monograph."""
    width, height = 640, 960
    # Wrap the title (large serif) and subtitle (small sans) to the cover width
    # so any book's title fits without hand-tuning.
    title = "Calculus, Intuitively"
    subtitle = "The ideas behind Calc 1–3, built from pictures and plain words — for anyone who never liked math."
    title_lines = textwrap.wrap(title, width=14) or ["Untitled"]
    subtitle_lines = textwrap.wrap(subtitle, width=42)[:3]

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'role="img" aria-label="Book cover: Calculus, Intuitively. A rising curve '
        f'with a straight tangent line grazing it at one point, over a shaded area.">',
        f'<rect width="{width}" height="{height}" fill="{PAPER}"/>',
        f'<rect x="26" y="26" width="{width - 52}" height="{height - 52}" '
        f'fill="none" stroke="{RULE_STRONG}" stroke-width="1.5"/>',
        f'<text x="72" y="152" font-family="{SANS}" font-size="16" '
        f'font-weight="650" letter-spacing="5" fill="{ACCENT}">A TEXTBOOK</text>',
    ]
    for i, line in enumerate(title_lines):
        parts.append(
            f'<text x="68" y="{232 + i * 72}" font-family="{SERIF}" font-size="58" '
            f'font-weight="700" fill="{INK}">{line}</text>'
        )

    parts.append(
        curve_tangent_svg(96, 544, 720, 468, stroke_w=3.5, node_r=13, axes=True)
    )

    parts.append(
        f'<path d="M 72 830 L 148 830" stroke="{RULE_STRONG}" stroke-width="1.5"/>'
    )
    for i, line in enumerate(subtitle_lines):
        parts.append(
            f'<text x="72" y="{862 + i * 23}" font-family="{SANS}" font-size="15.5" '
            f'fill="{MUTED}">{line}</text>'
        )
    parts.append("</svg>")
    return write_root_asset("cover.svg", "\n".join(parts))


def fig_icon() -> Path:
    """The favicon: the curve-and-tangent motif alone on a rounded paper tile."""
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180" role="img" '
        'aria-label="Site icon: a curve with a tangent line grazing it at a point.">',
        f'<rect width="180" height="180" rx="36" fill="{PAPER}"/>',
        curve_tangent_svg(34, 150, 140, 40, stroke_w=6, node_r=10),
        "</svg>",
    ]
    return write_root_asset("icon.svg", "\n".join(parts))


def fig_touch_icon() -> Path:
    """The apple-touch-icon: the favicon motif, full-bleed PNG (iOS rounds it).

    iOS does not accept SVG here, so matplotlib re-draws the same geometry as
    `fig_icon` at exactly 180 by 180 pixels.
    """
    from matplotlib.lines import Line2D
    from matplotlib.patches import Circle, Polygon, Rectangle

    dpi = 100
    fig = plt.figure(figsize=(1.8, 1.8), dpi=dpi)
    ax = fig.add_axes((0.0, 0.0, 1.0, 1.0))
    ax.set_xlim(0, 180)
    ax.set_ylim(180, 0)  # Flip y so the geometry matches the SVG coordinates.
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Rectangle((0, 0), 180, 180, facecolor=PAPER, edgecolor="none"))

    px = 72 / dpi  # One SVG stroke pixel is this many matplotlib points.
    curve, tangent, dot, baseline = _curve_geometry(34, 150, 140, 40)

    # Shaded area under the curve.
    area = [(34, baseline)] + curve + [(150, baseline)]
    ax.add_patch(Polygon(area, closed=True, facecolor=ACCENT_SOFT, edgecolor="none"))

    xs = [p[0] for p in curve]
    ys = [p[1] for p in curve]
    ax.add_line(
        Line2D(
            xs,
            ys,
            color=ACCENT,
            linewidth=6 * px,
            solid_capstyle="round",
            solid_joinstyle="round",
        )
    )
    ax.add_line(
        Line2D(
            [tangent[0][0], tangent[1][0]],
            [tangent[0][1], tangent[1][1]],
            color=AMBER,
            linewidth=6 * px,
            solid_capstyle="round",
        )
    )
    ax.add_patch(Circle(dot, radius=10, facecolor=AMBER, edgecolor="none"))

    path = ASSETS_DIR / "apple-touch-icon.png"
    fig.savefig(path, dpi=dpi, facecolor=PAPER)
    plt.close(fig)
    return path


FIGURES = (
    # Ch 1 · What Calculus Is Really About
    fig_change_and_accumulation,
    fig_two_moves,
    fig_inverse_pair,
    # Ch 2 · Functions, Graphs, and Just Enough Algebra
    fig_function_machine,
    fig_graph_pairs,
    fig_rise_over_run,
    # Ch 3 · The Limit
    fig_limit_hole,
    fig_limit_failures,
    # Ch 4 · Continuity and Its Breaks
    fig_continuity_condition,
    fig_continuity_breaks,
    fig_intermediate_value,
    # Ch 5 · The Derivative
    fig_derivative_pair,
    # Cover and icons
    fig_cover,
    fig_icon,
    fig_touch_icon,
)


def main() -> None:
    """Regenerate every figure and report where it went."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for make in FIGURES:
        path = make()
        assert (
            path.exists()
        ), f"Figure function '{make.__name__}' did not write its file."
        print(f"  wrote {path.relative_to(ROOT)}")
    print(f"Generated {len(FIGURES)} figures.")


if __name__ == "__main__":
    main()
