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
