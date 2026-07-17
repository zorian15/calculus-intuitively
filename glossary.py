"""Single source of truth for the book's glossary.

The convention is: **every term or abbreviation is defined inline the first time
it appears in the prose, and also added here**. `build.py` renders the
`glossary` appendix from `GLOSSARY`, alphabetically.

Keep each definition to one or two plain sentences aimed at the book's reader —
enough to unblock them, not a textbook entry. Cross-reference other terms by
name rather than restating them.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Term:
    """One glossary entry.

    `term` is shown as written (keep the canonical casing, e.g. "RNA-seq");
    sorting is case-insensitive. `definition` is one or two plain sentences.
    """

    term: str
    definition: str

    def __post_init__(self) -> None:
        assert self.term.strip(), "Glossary term is empty."
        assert self.definition.strip(), f"Term {self.term!r} has an empty definition."
        assert not self.term.startswith(" "), f"Term {self.term!r} has leading space."


_TERMS: tuple[Term, ...] = (
    Term(
        "Function",
        "A rule that turns each input number into exactly one output number; its graph is the picture of every input-output pair at once.",
    ),
    Term(
        "Slope",
        "How steep a line is: the amount the output rises for each step the input takes to the right (rise over run).",
    ),
    Term(
        "Secant line",
        "A straight line drawn through two points on a curve. Its slope is the average rate of change of the function between those two points.",
    ),
    Term(
        "Tangent line",
        "The straight line that just grazes a curve at a single point, matching its direction there. Its slope is the derivative at that point.",
    ),
    Term(
        "Limit",
        "The single value a quantity heads toward as its input is nudged ever closer to some target, whether or not it ever exactly arrives.",
    ),
    Term(
        "Derivative",
        "The instantaneous rate of change of a function — the slope of its tangent line — obtained as the limit of secant slopes as the two points merge.",
    ),
    Term(
        "Instantaneous rate of change",
        "How fast a function's output is changing at one exact instant, as opposed to averaged over an interval; another name for the derivative.",
    ),
    Term(
        "Continuity",
        "The property of a function whose graph has no jumps, gaps, or holes — you could draw it without lifting your pen.",
    ),
    Term(
        "Rate of change",
        "How much a quantity shifts for each small step forward in its input — how steeply it is climbing or falling. Made exact at a single instant, it is the derivative.",
    ),
    Term(
        "Integral",
        "The exact running total of a quantity that is changing while it is being added up, obtained by slicing an interval into ever-thinner pieces and adding their contributions; geometrically, the area beneath a curve.",
    ),
    Term(
        "Accumulation",
        "The total a rate builds up when it acts over an interval — for example, the total distance built up by a speed over time. Accumulation is what the integral computes.",
    ),
    Term(
        "Fundamental Theorem of Calculus",
        "The central fact that differentiation and integration are inverse operations: differentiating an accumulated total recovers its rate, and integrating a rate recovers the total.",
    ),
    Term(
        "Function notation",
        "The shorthand f(x) for 'the output of the function f when the input is x'; f(3) means the output at input 3, and the parentheses mark the input slot, not multiplication.",
    ),
    Term(
        "Graph of a function",
        "The picture formed by plotting every input-output pair as a point, with the input measured horizontally and the output vertically; the curve is all the pairs at once.",
    ),
    Term(
        "Linear function",
        "A function whose graph is a straight line, written f(x) = mx + b, where m is the slope and b is the y-intercept.",
    ),
    Term(
        "y-intercept",
        "The height at which a graph crosses the vertical axis — the output of the function when the input is 0.",
    ),
    Term(
        "Factoring",
        "Rewriting a sum or difference as a product, such as x squared minus 1 = (x minus 1)(x plus 1); it reveals where an expression is zero and lets a shared factor cancel.",
    ),
    Term(
        "One-sided limit",
        "The single value a function approaches as its input closes in on a target "
        "from just one direction — from the left (inputs below the target) or from "
        "the right (inputs above it). The two-sided limit exists only when both "
        "one-sided limits exist and agree.",
    ),
    Term(
        "Removable discontinuity",
        "A break where the function heads toward a finite height (the limit exists) "
        "but the point there is missing or sits at the wrong height. It is fixable by "
        "placing or moving a single point; also called a removable hole.",
    ),
    Term(
        "Diverge to infinity",
        "What a function does when its output grows without bound as the input nears "
        "a target, racing off toward positive or negative infinity. The limit does "
        "not exist as a finite number; 'infinity' names how it fails, not a value "
        "the output approaches.",
    ),
    Term(
        "Discontinuity",
        "A point where a function fails to be continuous — a place where you must "
        "lift your pen. The three kinds are a removable hole, a jump, and a blow-up.",
    ),
    Term(
        "Jump discontinuity",
        "A break where the function approaches one height from the left and a "
        "different height from the right, so the two one-sided limits disagree and the "
        "graph shows a vertical step.",
    ),
    Term(
        "Vertical asymptote",
        "A vertical line x = a that a graph races alongside, growing without bound "
        "toward positive or negative infinity as x nears a, without ever touching the "
        "line. It marks a blow-up (an infinite discontinuity).",
    ),
    Term(
        "Intermediate Value Theorem",
        "The guarantee that a continuous function on an interval takes every height "
        "between its starting and ending values at least once — so if it starts below "
        "a target and ends above it, it must cross that target somewhere in between.",
    ),
)


def _sorted(terms: tuple[Term, ...]) -> tuple[Term, ...]:
    """Return terms sorted case-insensitively, failing on duplicates."""
    seen: set[str] = set()
    for term in terms:
        key = term.term.lower()
        assert key not in seen, f"Duplicate glossary term: {term.term!r}."
        seen.add(key)
    return tuple(sorted(terms, key=lambda t: t.term.lower()))


GLOSSARY: tuple[Term, ...] = _sorted(_TERMS)
