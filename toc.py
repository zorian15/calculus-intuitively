"""Single source of truth for the book's structure.

`build.py` imports `BOOK` from this module and generates one HTML file per
entry, plus the landing page. To reorder, rename, or add a chapter, edit this
file and rerun the build. If a chapter has a matching `content/<slug>.md`, that
prose is rendered; otherwise a stub page is synthesized from the `outline`
declared here, so the whole book is always navigable even before it is written.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Chapter:
    """One page of the book.

    `slug` is the file stem (used for `content/<slug>.md` and `<slug>.html`).
    `label` is the display number shown in navigation and section numbering:
    a digit for chapters, a letter for appendices, or an empty string for
    unnumbered front matter. `outline` is a list of (section_title, note)
    pairs describing what the chapter should eventually cover; it is only used
    to synthesize the stub when no drafted markdown exists yet.
    """

    slug: str
    label: str
    title: str
    outline: tuple[tuple[str, str], ...]


@dataclass(frozen=True)
class Part:
    """A titled group of chapters, rendered as a heading in the sidebar."""

    title: str
    chapters: tuple[Chapter, ...]


PREFACE = Chapter(
    slug="preface",
    label="",
    title="Preface",
    outline=(),
)


BOOK: tuple[Part, ...] = (
    Part(
        title="I · Limits and Continuity",
        chapters=(
            Chapter(
                slug="what-calculus-is",
                label="1",
                title="What Calculus Is Really About",
                outline=(
                    (
                        "Two questions, one subject",
                        "Calculus is the mathematics of change and accumulation: "
                        "how fast, and how much.",
                    ),
                    (
                        "Zooming in and adding up",
                        "The two moves that run through the whole book, previewed "
                        "with pictures, no formulas.",
                    ),
                ),
            ),
            Chapter(
                slug="functions-first",
                label="2",
                title="Functions, Graphs, and Just Enough Algebra",
                outline=(
                    (
                        "A function is a machine",
                        "Input in, output out; the graph is a picture of every "
                        "input-output pair at once.",
                    ),
                    (
                        "The algebra you actually need",
                        "Lines, slopes, and rearranging — refreshed gently, with "
                        "nothing assumed.",
                    ),
                ),
            ),
            Chapter(
                slug="the-limit",
                label="3",
                title="The Limit: Getting Arbitrarily Close",
                outline=(
                    (
                        "Approaching without arriving",
                        "What it means for a value to head toward a number it may "
                        "never reach.",
                    ),
                    (
                        "When limits misbehave",
                        "Jumps, gaps, and blow-ups, and how to read them off a "
                        "graph.",
                    ),
                ),
            ),
            Chapter(
                slug="continuity",
                label="4",
                title="Continuity and Its Breaks",
                outline=(
                    (
                        "Drawing without lifting the pen",
                        "The intuitive picture of continuity and its precise "
                        "cousin.",
                    ),
                    (
                        "Why continuity matters",
                        "The guarantees it buys you, previewed for later chapters.",
                    ),
                ),
            ),
        ),
    ),
    Part(
        title="II · Derivatives",
        chapters=(
            Chapter(
                slug="the-derivative",
                label="5",
                title="The Derivative",
                outline=(
                    (
                        "Slope at a single point",
                        "How an average rate of change becomes an instantaneous "
                        "one in the limit.",
                    ),
                    (
                        "The derivative as a function",
                        "Reading the slope everywhere at once.",
                    ),
                ),
            ),
            Chapter(
                slug="rules-of-differentiation",
                label="6",
                title="Rules for Finding Derivatives",
                outline=(
                    (
                        "The shortcuts",
                        "Power, product, and quotient rules, and where they come "
                        "from.",
                    ),
                    (
                        "Why the shortcuts are safe",
                        "Each rule as a packaged limit you never have to redo.",
                    ),
                ),
            ),
            Chapter(
                slug="chain-rule",
                label="7",
                title="The Chain Rule",
                outline=(
                    (
                        "Rates that stack",
                        "Composing functions and multiplying their rates of " "change.",
                    ),
                    (
                        "Reading a composition",
                        "Spotting the inside and the outside function.",
                    ),
                ),
            ),
            Chapter(
                slug="using-derivatives",
                label="8",
                title="Using Derivatives: Optimization and Change",
                outline=(
                    (
                        "Finding the best",
                        "Maxima and minima where the slope goes flat.",
                    ),
                    (
                        "Related rates",
                        "When one changing quantity drags another along.",
                    ),
                ),
            ),
        ),
    ),
    Part(
        title="III · Integrals",
        chapters=(
            Chapter(
                slug="the-integral",
                label="9",
                title="The Integral: Adding Up Infinitely Many Slices",
                outline=(
                    (
                        "Area as a sum",
                        "Approximating with rectangles, then letting them get " "thin.",
                    ),
                    (
                        "The definite integral",
                        "The limit of those sums, and what it measures.",
                    ),
                ),
            ),
            Chapter(
                slug="fundamental-theorem",
                label="10",
                title="The Fundamental Theorem of Calculus",
                outline=(
                    (
                        "The two moves are inverses",
                        "Why differentiating undoes integrating, and the shock of "
                        "it.",
                    ),
                    (
                        "Computing integrals the easy way",
                        "Antiderivatives turn area into arithmetic.",
                    ),
                ),
            ),
            Chapter(
                slug="techniques-of-integration",
                label="11",
                title="Techniques of Integration",
                outline=(
                    (
                        "Substitution",
                        "Running the chain rule backwards.",
                    ),
                    (
                        "Integration by parts",
                        "Trading one integral for an easier one.",
                    ),
                ),
            ),
            Chapter(
                slug="using-integrals",
                label="12",
                title="Using Integrals: Area, Volume, and Accumulation",
                outline=(
                    (
                        "Beyond area",
                        "Volumes, averages, and totals as integrals.",
                    ),
                    (
                        "Accumulation in the wild",
                        "Reading real quantities as running sums.",
                    ),
                ),
            ),
        ),
    ),
    Part(
        title="IV · Sequences and Series",
        chapters=(
            Chapter(
                slug="sequences",
                label="13",
                title="Sequences: Lists That Go Somewhere",
                outline=(
                    (
                        "Does it settle?",
                        "Convergence and divergence of an endless list.",
                    ),
                    (
                        "Limits again",
                        "The same approaching idea, now for lists.",
                    ),
                ),
            ),
            Chapter(
                slug="series",
                label="14",
                title="Series: Adding Infinitely Many Terms",
                outline=(
                    (
                        "A sum that never ends",
                        "How an infinite sum can land on a finite number.",
                    ),
                    (
                        "Tests for convergence",
                        "Quick ways to tell whether a series settles.",
                    ),
                ),
            ),
            Chapter(
                slug="power-series",
                label="15",
                title="Power Series",
                outline=(
                    (
                        "Polynomials that never stop",
                        "Series with an x in them, and where they converge.",
                    ),
                    (
                        "Functions in disguise",
                        "Familiar functions written as power series.",
                    ),
                ),
            ),
            Chapter(
                slug="taylor-series",
                label="16",
                title="Taylor Series: Functions as Infinite Polynomials",
                outline=(
                    (
                        "Matching a function locally",
                        "Building a polynomial that hugs a curve near a point.",
                    ),
                    (
                        "Why it works",
                        "Each term fixes one more derivative.",
                    ),
                ),
            ),
        ),
    ),
    Part(
        title="V · Multivariable Calculus",
        chapters=(
            Chapter(
                slug="several-variables",
                label="17",
                title="Functions of Several Variables",
                outline=(
                    (
                        "Surfaces instead of curves",
                        "Graphs that live in three dimensions.",
                    ),
                    (
                        "Reading a contour map",
                        "Slicing a surface into level curves.",
                    ),
                ),
            ),
            Chapter(
                slug="partial-derivatives",
                label="18",
                title="Partial Derivatives",
                outline=(
                    (
                        "One direction at a time",
                        "Holding every variable but one fixed.",
                    ),
                    (
                        "The slope in any direction",
                        "Directional derivatives, previewed.",
                    ),
                ),
            ),
            Chapter(
                slug="gradients-and-optimization",
                label="19",
                title="Gradients and Optimization",
                outline=(
                    (
                        "The direction of steepest ascent",
                        "What the gradient vector points at, and why.",
                    ),
                    (
                        "Peaks, valleys, and saddles",
                        "Finding and classifying critical points.",
                    ),
                ),
            ),
            Chapter(
                slug="multiple-integrals",
                label="20",
                title="Multiple Integrals",
                outline=(
                    (
                        "Adding over a region",
                        "Volume under a surface as a double sum, then integral.",
                    ),
                    (
                        "Changing coordinates",
                        "When polar or other coordinates make it easy.",
                    ),
                ),
            ),
        ),
    ),
    Part(
        title="VI · Vector Calculus",
        chapters=(
            Chapter(
                slug="vector-fields",
                label="21",
                title="Vector Fields",
                outline=(
                    (
                        "An arrow at every point",
                        "Flows, forces, and how to picture them.",
                    ),
                    (
                        "Divergence and curl, intuitively",
                        "Spreading out versus swirling.",
                    ),
                ),
            ),
            Chapter(
                slug="line-integrals",
                label="22",
                title="Line Integrals and Flow",
                outline=(
                    (
                        "Adding along a path",
                        "Work done moving through a field.",
                    ),
                    (
                        "When the path does not matter",
                        "Conservative fields and potentials.",
                    ),
                ),
            ),
            Chapter(
                slug="big-theorems",
                label="23",
                title="Green's, Stokes', and the Divergence Theorem",
                outline=(
                    (
                        "The boundary tells the story",
                        "One idea behind the three great theorems: the inside is "
                        "measured by the edge.",
                    ),
                    (
                        "The fundamental theorem, grown up",
                        "How these generalize the one from Chapter 10.",
                    ),
                ),
            ),
        ),
    ),
)


APPENDICES: tuple[Chapter, ...] = (
    Chapter(
        slug="precalculus-survival-kit",
        label="A",
        title="A Precalculus Survival Kit",
        outline=(
            (
                "The algebra and trig you will lean on",
                "A compact, friendly reference to reach for when a step assumes "
                "something you have not touched in a while.",
            ),
        ),
    ),
    Chapter(
        slug="glossary",
        label="B",
        title="Glossary",
        outline=(),
    ),
)


def all_pages() -> tuple[Chapter, ...]:
    """Return every page in reading order: preface, chapters, then appendices."""
    pages: list[Chapter] = [PREFACE]
    for part in BOOK:
        pages.extend(part.chapters)
    pages.extend(APPENDICES)
    slugs = [page.slug for page in pages]
    assert len(slugs) == len(
        set(slugs)
    ), "Duplicate slug detected in the table of contents."
    return tuple(pages)
