"""Single source of truth for the end-of-chapter "Check yourself" quizzes.

Each chapter closes with a short set of challenging multiple-choice questions.
`build.py` renders it automatically after the References; a small inline script
makes it interactive: the reader picks an option, the choice is marked right or
wrong, the correct answer is revealed, and an explanation appears.

The questions are meant to be *hard* in the way a sharp reviewer's question is
hard. The distractors are plausible misconceptions, stated with the same
confidence and detail as the answer, so that neither length nor specificity ever
signals which option is correct. The renderer shuffles the options on load, so
the position of the answer carries no information either — write the options in
any order and point `answer` at the right one. Each explanation carries a
second-layer detail the prose only gestures at, so the quiz teaches rather than
merely confirms.

Question strings are **plain text**. `build.py` HTML-escapes everything, which
would neutralize MathJax delimiters, so do not write `$...$` or `\\(...\\)`
here; phrase math in words or with plain symbols instead.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Question:
    """One multiple-choice question.

    `options` are shuffled at render time, so their order here does not matter;
    `answer` is the index (into this tuple) of the single correct option.
    `explanation` is revealed after the reader answers and should teach, not
    just confirm. Because the display order is randomized, never write an option
    that refers to another by position (e.g. "same as A").
    """

    prompt: str
    options: tuple[str, ...]
    answer: int
    explanation: str

    def __post_init__(self) -> None:
        assert self.prompt.strip(), "Question has an empty prompt."
        assert len(self.options) >= 3, f"{self.prompt!r}: need at least 3 options."
        assert all(o.strip() for o in self.options), f"{self.prompt!r}: empty option."
        assert (
            0 <= self.answer < len(self.options)
        ), f"{self.prompt!r}: answer index {self.answer} is out of range."
        assert self.explanation.strip(), f"{self.prompt!r}: empty explanation."


_QUIZZES: dict[str, tuple[Question, ...]] = {
    "the-derivative": (
        Question(
            prompt="In plain words, what does the derivative of a function at a single point measure?",
            options=(
                "How steep the graph is right at that point — the slope of the line that just grazes the curve there.",
                "The height of the graph at that point — how far the curve sits above the horizontal axis.",
                "The total area trapped between the curve and the horizontal axis up to that point.",
                "How far the point has moved to the right of where the function starts.",
            ),
            answer=0,
            explanation="The derivative is a slope, not a height and not an area. It answers 'how fast is the output changing as the input nudges forward, right here?', which is the steepness of the tangent line grazing the curve at that point. Height is just the function's value; area is what integration measures.",
        ),
        Question(
            prompt="We build the derivative by drawing a secant line between two points on the curve and then sliding them together. What is happening to the secant as the gap h shrinks toward zero?",
            options=(
                "Its slope closes in on the slope of the tangent line at the point — the secant becomes the tangent in the limit.",
                "Its slope grows without bound, because dividing by a smaller and smaller h always blows up.",
                "Its slope drops to zero, because the two points it connects end up on top of each other.",
                "Its slope stops changing once h is small enough, landing exactly on the tangent after a few steps.",
            ),
            answer=0,
            explanation="Both the rise and the run shrink together, and their ratio settles on a specific number: the tangent's slope. It does not blow up (numerator shrinks too), it is not zero (the ratio is what matters, not the gap), and it never 'lands exactly' after finitely many steps — the tangent is the limit the secants approach, which is the whole point of a limit.",
        ),
        Question(
            prompt="The slope of the secant is (f(a+h) − f(a)) / h. Why can't we just set h = 0 to get the slope at the point?",
            options=(
                "Setting h = 0 makes the expression 0/0, which is undefined; the limit sidesteps this by asking what the ratio approaches, not its value at 0.",
                "Setting h = 0 is allowed and gives the right answer directly; the limit is just a formality mathematicians add for rigor.",
                "Setting h = 0 gives infinity, so we use a limit purely to keep the number finite.",
                "Setting h = 0 changes the point we are looking at, so the limit is needed to move back to the original point.",
            ),
            answer=0,
            explanation="At h = 0 both the top and the bottom are exactly zero, and 0/0 has no meaning on its own. The limit rescues the calculation by watching the ratio for tiny nonzero h and reporting the number it homes in on. It is not a mere formality, and the trouble is 0/0 specifically, not infinity.",
        ),
        Question(
            prompt="Once you can find the slope at every input, you can package those slopes into a new function, the derivative function f'. What does f'(3) tell you?",
            options=(
                "The slope of the original curve at the input x = 3.",
                "The value of the original function, f(3), computed a second way.",
                "The slope of the derivative's own graph at x = 3.",
                "The average slope of the original curve between x = 0 and x = 3.",
            ),
            answer=0,
            explanation="The derivative function is a slope-reporting machine: feed it an input, get back the original curve's steepness there. So f'(3) is the tangent slope of f at x = 3 — not f's height, not the derivative's own steepness, and not an average over an interval (that would be a single secant slope, not the derivative).",
        ),
    ),
}


def _validate(
    quizzes: dict[str, tuple[Question, ...]],
) -> dict[str, tuple[Question, ...]]:
    """Assert each chapter has 4-6 questions."""
    for slug, questions in quizzes.items():
        assert (
            4 <= len(questions) <= 6
        ), f"Quiz for '{slug}' has {len(questions)} questions; expected 4-6."
    return quizzes


QUIZZES: dict[str, tuple[Question, ...]] = _validate(_QUIZZES)
