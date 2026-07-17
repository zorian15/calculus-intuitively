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
    "what-calculus-is": (
        Question(
            prompt="In one sentence, what are the two questions calculus is built to answer?",
            options=(
                "How fast a quantity is changing, and how much of it has accumulated.",
                "What a quantity equals now, and what it equalled before.",
                "Whether a quantity is positive or negative, and how large it is.",
                "How to solve an equation, and how to graph its solution.",
            ),
            answer=0,
            explanation="Calculus is the mathematics of change (rates, answered by the derivative) and accumulation (running totals, answered by the integral). The other options describe algebra-style questions about fixed or static quantities, which is exactly the contrast: algebra handles frozen values, calculus handles moving ones.",
        ),
        Question(
            prompt="Why can't you find the steepness of a curve at a point just by picking the point and reading off a slope, the way you can for a straight line?",
            options=(
                "Because a curve's steepness keeps changing along it, so 'the slope of the curve' has no single value until you narrow the question to one point and zoom in.",
                "Because a curve has no slope at all — steepness is a property that belongs to straight lines alone, and a bending curve never possesses a single slope you could read off at any one of its points.",
                "Because you would need the exact equation of the curve, which is usually unknown.",
                "Because slope is only defined for lines that pass through the origin.",
            ),
            answer=0,
            explanation="A straight line has one steepness everywhere, so any two points give it. A curve bends, so its steepness varies point to point. Calculus's fix is to zoom in until the curve near one point is indistinguishable from a straight line, then read that line's slope. Curves do have slopes; that is the whole point of the derivative.",
        ),
        Question(
            prompt="When calculus finds an area by slicing a curved region into thin rectangles, what does the exact answer actually refer to?",
            options=(
                "The single value the rectangle totals approach as the slices are made ever thinner.",
                "The total you get once the slices are made exactly zero width.",
                "The total from using the thinnest rectangles a computer can store.",
                "The average of the totals from a few different slice widths.",
            ),
            answer=0,
            explanation="The integral is a limit: the value the sums head toward as the slices shrink, never a sum at any fixed width. Setting the width to zero is the trap, since zero-width rectangles have zero area and sum to nothing. This is the same 'approach, never arrive' move that defines the derivative, which is why the limit is the shared engine of both.",
        ),
        Question(
            prompt="What does it mean to say differentiation and integration are inverse operations?",
            options=(
                "Differentiating a running total recovers its rate, and integrating a rate recovers the total, so applying one then the other returns you to where you started.",
                "Differentiating a function always shrinks it toward smaller values while integrating always builds it up into larger ones, so applying one and then the other lands you on a different, rescaled function rather than back where you started.",
                "They can only be applied to different kinds of functions, never the same one.",
                "One is used for straight lines and the other for curves, so they never overlap.",
            ),
            answer=0,
            explanation="This is the Fundamental Theorem of Calculus: rate and accumulated total are two ends of one bridge, and each operation undoes the other, like multiplying then dividing by the same number. Its practical payoff is huge: you can compute a hard area by running the easy rate question backward instead of summing infinitely many slices by hand.",
        ),
        Question(
            prompt="Why is the connection between the derivative and the integral considered surprising rather than obvious?",
            options=(
                "Because 'how steep is this curve here?' and 'how much area sits under it?' look like unrelated questions about slopes versus regions, yet turn out to be exactly linked.",
                "Because both were discovered by the same person on the same day.",
                "Because for any curve the steepness at a given point and the area sitting beneath it always work out to exactly the same number, so there was never really anything surprising to explain.",
                "Because area and slope are just two names for the identical measurement.",
            ),
            answer=0,
            explanation="Steepness is a fact about slopes; area is a fact about regions. There is no obvious reason one should determine the other, and the two were studied separately for centuries. The Fundamental Theorem says they always fit together exactly. Note they are not equal numbers, they are linked operations: the rate of the area function is the height of the curve.",
        ),
        Question(
            prompt="A student says: 'To get the instantaneous rate, just take a step of size zero, since we want a single instant.' What is wrong with this?",
            options=(
                "A step of size zero gives a zero-over-zero ratio, which is meaningless; the rate is instead the value the small-step ratios approach as the step shrinks.",
                "Nothing is wrong; a zero-sized step is exactly how the derivative is defined.",
                "The step should be as large as possible, not zero, to get an accurate rate.",
                "Instantaneous rates cannot be computed at all, only estimated by eye.",
            ),
            answer=0,
            explanation="A rate compares change in output to change in input, so a zero-sized input step divides by zero. Calculus never lands on the zero step; it asks what the ratio heads toward as the step gets tiny, which is a genuine, definite number. Both signature moves of calculus live in the approach, never at the destination itself.",
        ),
    ),
    "functions-first": (
        Question(
            prompt="A classmate reads the symbol f(3) as 'f times 3.' Why is that reading a problem, not just a preference?",
            options=(
                "Because the parentheses mark the input slot, so f(3) means the machine's output when its input is 3, not a product; reading it as multiplication invents a number that has nothing to do with the rule.",
                "Because f(3) is only defined when f is a linear function, and multiplication would wrongly apply it to curved functions too.",
                "Because f must always be multiplied by the input before the rule is applied, so 'f times 3' double-counts the input.",
                "Because the 3 tucked inside the parentheses is really an exponent written in disguise, so the honest reading of f(3) is 'f raised to the third power,' and calling it multiplication throws that hidden exponent away.",
            ),
            answer=0,
            explanation="Function notation reuses the symbols of multiplication but means something entirely different: f(3) is 'evaluate the machine f at input 3.' For f(x) = 2x + 1 that output is 7, whereas 'f times 3' is not even a defined quantity, since f is a rule, not a number. This is why later chapters can write f'(a) or f(a + h) without ambiguity — the parentheses are always 'plug this in.'",
        ),
        Question(
            prompt="Someone claims a certain curve is the graph of a function because it passes the vertical line test. What does that test actually guarantee?",
            options=(
                "That every vertical line meets the curve at most once, so each input has at most one output — the 'exactly one output' rule made visual.",
                "That every horizontal line meets the curve at most once, so no two inputs share an output.",
                "That the curve never crosses the x-axis, so the function is never zero.",
                "That the curve is a straight line, since only straight lines have a single output per input.",
            ),
            answer=0,
            explanation="A function assigns exactly one output to each input, and a vertical line fixes the input while sweeping through all heights — so a second crossing would mean two outputs for one input. The horizontal-line test is a different check (whether a function is one-to-one), and plenty of curved graphs, like a parabola, pass the vertical test while failing the horizontal one.",
        ),
        Question(
            prompt="On the line f(x) = 2x + 1 you compute rise over run between x = 0 and x = 1, then again between x = 3 and x = 10. What happens to the slope?",
            options=(
                "It is 2 in both cases; on a straight line rise over run is identical for every pair of points, which is exactly what makes a line's steepness a single number.",
                "It is 2 for the first pair but larger for the second, because a longer run climbs to a greater height.",
                "It is 2 for the first pair but smaller for the second, because spreading the same rise over a longer run flattens the ratio.",
                "It cannot be found for the second pair without also knowing the y-intercept, since the points are farther from the axis.",
            ),
            answer=0,
            explanation="For y = 2x + 1 the rise is always twice the run, so the ratio is 2 no matter which two points you pick — that constancy is the defining feature of a line. A curve is different: its rise-over-run depends on which pair you choose, and pinning down the steepness 'right here' is precisely the problem the derivative in Chapter 5 solves.",
        ),
        Question(
            prompt="To simplify (x squared minus 1) divided by (x minus 1), a student cancels the x's to get (minus 1) over (minus 1) = 1. Where did they go wrong?",
            options=(
                "You may only cancel a factor of the whole top and whole bottom; factoring the top as (x minus 1)(x plus 1) lets you cancel the shared factor (x minus 1), leaving x plus 1, not 1.",
                "Nothing is wrong; the x terms cancel directly, so the expression equals 1 for every x except 0.",
                "The mistake is arithmetic: minus 1 over minus 1 is actually minus 1, so the simplified value is minus 1.",
                "The expression cannot be simplified at all, because the subtraction sitting in the numerator blocks every possible cancellation, so (x squared minus 1) divided by (x minus 1) is already written in its simplest form.",
            ),
            answer=0,
            explanation="Cancellation removes a common factor — something multiplying the entire numerator and denominator — not a term that is merely added. Here x squared minus 1 factors as (x minus 1)(x plus 1), so the (x minus 1) cancels and leaves x plus 1. This is the exact move that rescues a slope calculation from 0/0 when the run shrinks to zero, as you'll see in Chapters 3 and 5.",
        ),
        Question(
            prompt="Why does a calculus book spend a whole section on the slope of a straight line before ever touching a curve?",
            options=(
                "Because zooming in on a smooth curve makes a tiny piece look nearly straight, so the derivative measures a curve's steepness as the slope of that straight piece — lines are the tool curves get approximated by.",
                "Because most functions in calculus turn out to be straight lines once simplified, so lines cover nearly every case.",
                "Because slope is only needed for lines; curves are handled entirely by area, which is a separate idea with no connection to steepness.",
                "Because a curve's slope at a point is defined as the average of the slopes of every straight line that crosses the curve, so you have to master the slope of a single line before you can average infinitely many of them together.",
            ),
            answer=0,
            explanation="The whole engine of differential calculus is local straightening: any smooth curve, viewed closely enough, is almost a line, and the derivative is the slope of that limiting line. So rise-over-run on a line is not a warm-up you leave behind — it is the quantity the derivative generalizes, which is why getting it solid now pays off in every later chapter.",
        ),
    ),
    "the-limit": (
        Question(
            prompt=(
                "For the function (x squared minus 1) divided by (x minus 1), what "
                "is the limit as x approaches 1, and what is the function's value at "
                "x equals 1?"
            ),
            options=(
                "The limit is 2, but the value at x equals 1 does not exist.",
                "Both the limit and the value at x equals 1 are 2.",
                "The limit does not exist because you get zero divided by zero.",
                "The limit is 0 and the value at x equals 1 is also 0.",
            ),
            answer=0,
            explanation=(
                "Away from x equals 1, the expression simplifies to x plus 1, which "
                "heads to 2 as x nears 1 from both sides, so the limit is 2. But "
                "plugging in x equals 1 gives zero over zero, which is undefined, so "
                "the function has no value there — a hole. The zero-over-zero answer "
                "is the classic trap: it tells you plugging in fails, not that the "
                "limit fails. The limit reads the neighborhood, not the point."
            ),
        ),
        Question(
            prompt=(
                "A function's left-hand limit at x equals 3 is 5, and its right-hand "
                "limit at x equals 3 is 5, but the function is actually defined to "
                "equal 9 at x equals 3. What is the two-sided limit as x approaches 3?"
            ),
            options=(
                "The limit is 5.",
                "The limit is 9, because that is the function's actual value there.",
                "The limit is the average of 5 and 9, which is 7.",
                "The limit does not exist, because the value disagrees with the sides.",
            ),
            answer=0,
            explanation=(
                "The limit depends only on where the two sides are heading, and both "
                "are heading for 5, so the limit is 5 — the value plunked down at the "
                "point is irrelevant to it. This is a removable discontinuity: the "
                "limit exists even though the value is misplaced, and redefining the "
                "point to be 5 would patch it. Choosing 9 is the trap of confusing the "
                "value with the limit; they are separate questions."
            ),
        ),
        Question(
            prompt=(
                "At x equals 2, a function approaches 4 from the left and approaches 7 "
                "from the right. Which statement is correct?"
            ),
            options=(
                "Both one-sided limits exist, but the two-sided limit does not.",
                "The two-sided limit is 4, since the left side is evaluated first.",
                "The two-sided limit exists and equals 5.5, splitting the difference.",
                "Neither one-sided limit exists, so nothing can be said at x equals 2.",
            ),
            answer=0,
            explanation=(
                "Each side settles on a definite number, so both one-sided limits "
                "exist — 4 on the left, 7 on the right. But a two-sided limit requires "
                "the two sides to agree, and 4 is not 7, so it does not exist. This is "
                "a jump, and it is why a jump is not removable: no single dot can sit "
                "at two different heights at once."
            ),
        ),
        Question(
            prompt=(
                "As x approaches 1, the function 1 divided by (x minus 1) squared grows "
                "larger and larger without bound. What is the most accurate way to "
                "describe the limit?"
            ),
            options=(
                "The limit does not exist as a finite number; the function diverges to "
                "positive infinity.",
                "The limit equals infinity, which is a perfectly good numerical answer.",
                "The limit is 1, because the numerator is 1.",
                "The limit is 0, because the denominator becomes huge.",
            ),
            answer=0,
            explanation=(
                "Saying a limit exists and equals L means the function settles near one "
                "finite number, and a blow-up does the opposite — it runs away past "
                "every ceiling. Writing 'equals infinity' is shorthand for how the "
                "limit fails, not a claim that it succeeded; infinity is not a number "
                "the output closes in on. The denominator does shrink toward zero, but "
                "one over a tiny positive number is enormous, not zero."
            ),
        ),
        Question(
            prompt=(
                "Why can't you find the limit of a secant slope by simply setting the "
                "gap h to zero in the difference quotient?"
            ),
            options=(
                "Setting h to zero gives zero divided by zero, which is meaningless; "
                "the limit instead asks what the ratio approaches for tiny nonzero h.",
                "Setting h to zero always gives the wrong sign for the slope.",
                "You can set h to zero; it is just faster to use a table of values.",
                "The gap h can never be exactly zero because distances are always "
                "positive.",
            ),
            answer=0,
            explanation=(
                "At h equals zero the difference quotient becomes the height at the "
                "point minus itself, over zero — zero over zero, which could be "
                "anything. The limit sidesteps this by never touching h equals zero; it "
                "reads the trend of the ratio for small nonzero gaps. This is exactly "
                "the hole situation, and it is why the derivative in Chapter 5 is built "
                "as a limit rather than a plug-in."
            ),
        ),
        Question(
            prompt=(
                "Which single condition guarantees that a two-sided limit exists at a "
                "point?"
            ),
            options=(
                "The left-hand and right-hand limits both exist and equal the same "
                "finite number.",
                "The function is defined at the point.",
                "The function never divides by zero anywhere near the point.",
                "The left-hand and right-hand limits both exist, whatever they are.",
            ),
            answer=0,
            explanation=(
                "A two-sided limit exists exactly when both sides agree on one finite "
                "value — that is the whole definition. Being defined at the point is "
                "neither necessary nor sufficient: the hole example has a limit with no "
                "value, and the jump example can have a value with no limit. And both "
                "sides existing is not enough if they disagree, as a jump shows; they "
                "must match."
            ),
        ),
    ),
    "continuity": (
        Question(
            prompt=(
                "In precise terms, a function f is continuous at an input a exactly "
                "when which condition holds?"
            ),
            options=(
                "The limit of f as x approaches a equals f(a) — the value it heads "
                "toward matches the value it actually takes.",
                "The limit of f as x approaches a exists, whether or not f(a) is "
                "defined.",
                "f(a) is defined, which is all continuity requires.",
                "f approaches the same height from the left and the right, no matter "
                "what f(a) turns out to be.",
            ),
            answer=0,
            explanation=(
                "Continuity packs three demands into one equation: f(a) must be "
                "defined, the limit must exist (both one-sided limits agree), AND the "
                "two must be equal. The other options each keep only part of this. A "
                "limit can exist while f(a) is missing or misplaced (a removable hole), "
                "and matching one-sided limits give you the limit but say nothing about "
                "whether the actual point sits on the curve."
            ),
        ),
        Question(
            prompt=(
                "A function heads toward the height 5 as x approaches 3 from both "
                "sides, but the function is simply not defined at x = 3. Which kind of "
                "discontinuity is this, and can it be fixed by placing a single point?"
            ),
            options=(
                "A removable hole; yes, dropping the point (3, 5) into the gap makes it "
                "continuous.",
                "A jump; no, because the two sides disagree.",
                "A blow-up; no, because the function escapes to infinity there.",
                "Not a discontinuity at all, since the limit exists.",
            ),
            answer=0,
            explanation=(
                "A finite two-sided limit with a missing (or misplaced) value is the "
                "definition of a removable hole, and 'removable' means exactly that one "
                "dab of ink repairs it. It is still a genuine discontinuity even though "
                "the limit exists: continuity needs the limit to equal the value, and "
                "here there is no value at all until you supply one."
            ),
        ),
        Question(
            prompt=(
                "What most sharply distinguishes a jump discontinuity from a removable "
                "hole?"
            ),
            options=(
                "At a jump the left-hand and right-hand limits exist but disagree, so "
                "the full limit does not exist; at a hole they agree and the limit "
                "exists.",
                "At a jump the function is undefined, while at a hole it is defined.",
                "At a jump the function runs off toward infinity, shooting past every "
                "finite height, whereas at a removable hole the function stays "
                "perfectly finite and merely skips over one missing point.",
                "A jump can be fixed by moving one point; a hole cannot.",
            ),
            answer=0,
            explanation=(
                "The deciding fact is whether the two one-sided limits match. They "
                "disagree at a jump (no full limit, a genuine vertical step) and agree "
                "at a hole (the limit exists). Infinity is the mark of a blow-up, not a "
                "jump. And the repairability is backwards in the last option: a hole is "
                "the one a single point fixes; a jump's built-in disagreement cannot be "
                "patched that way."
            ),
        ),
        Question(
            prompt=(
                "Why can't a vertical asymptote (a blow-up) ever be a removable "
                "discontinuity?"
            ),
            options=(
                "Because removing a discontinuity requires a finite limit to land on, "
                "and at a blow-up the function heads to infinity, so no finite limit "
                "exists.",
                "Because the function is defined at the asymptote, leaving nothing to "
                "remove.",
                "Because the left and right sides always agree at an asymptote.",
                "Because a blow-up is really nothing more than a jump discontinuity "
                "with an unusually tall step between its two sides, and like any jump "
                "it simply cannot be repaired by dropping in a single point.",
            ),
            answer=0,
            explanation=(
                "Removability means there is a finite height the curve is aiming at, so "
                "one point can be slid into place. A blow-up has no such target: the "
                "values grow without bound near the line, so the limit does not exist "
                "as a finite number and there is nothing to fill in. It is not a jump "
                "either — a jump steps between two finite heights, while a blow-up never "
                "settles on any."
            ),
        ),
        Question(
            prompt=(
                "The Intermediate Value Theorem lets you prove that x^3 = x + 1 has a "
                "solution between 1 and 2 because f(x) = x^3 - x - 1 is continuous with "
                "f(1) = -1 and f(2) = 5. What exactly does the theorem deliver here?"
            ),
            options=(
                "A guarantee that a solution exists somewhere in the interval, without "
                "telling you its value.",
                "The exact value of the solution.",
                "A guarantee only if the function is also a straight line.",
                "A guarantee that there is exactly one solution in the interval.",
            ),
            answer=0,
            explanation=(
                "The IVT is an existence result: a continuous function running from a "
                "negative value to a positive one must hit 0 in between, so a root "
                "exists. It does not locate the root or count how many there are — "
                "there could be several crossings. That split, proving something exists "
                "before finding it, is one of calculus's recurring moves."
            ),
        ),
        Question(
            prompt=(
                "A parking garage charges $5 for up to two hours and $12 the instant "
                "you pass two hours, so the cost never equals $8. Why does this NOT "
                "violate the Intermediate Value Theorem?"
            ),
            options=(
                "The cost function has a jump at the two-hour mark, so it is not "
                "continuous, and the theorem only applies to continuous functions.",
                "It does violate the theorem, which shows the theorem has exceptions.",
                "$8 lies outside the range of prices, so the theorem never promised it.",
                "The Intermediate Value Theorem applies only to functions that "
                "steadily increase, and because the parking cost sometimes stays flat "
                "for a stretch instead of rising, the theorem never covered a case "
                "like this one.",
            ),
            answer=0,
            explanation=(
                "The IVT's guarantee rests entirely on continuity, and a jump breaks "
                "exactly that assumption — the pen leaps the gap and skips every value "
                "in between, $8 included. This is precisely why the theorem states "
                "'continuous' out loud: it is load-bearing, not decoration. ($8 does sit "
                "between $5 and $12, so it is not out of range; the function simply "
                "jumps over it.)"
            ),
        ),
    ),
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
