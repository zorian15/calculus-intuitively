Picture yourself filling a bathtub.
Two different stories are unfolding at once, and both matter.
There is the story of *how fast* the water is rising — fast when the tap is wide open, slowing to a trickle as you ease it shut.
And there is the story of *how much* water sits in the tub — a total that keeps piling up for as long as any water flows at all.
These feel like separate questions, and for most of history they were studied by separate people.
Calculus is the discovery that they are two views of a single thing, and that each one quietly answers the other.
That discovery turned out to be one of the most useful ideas humans have ever had: nearly everything that moves, grows, cools, spreads, or accumulates is described with the tools you are about to meet.

You do not need to be a "math person" to get this.
You already understand *change* (you feel a car speed up) and you already understand *accumulation* (you know a bigger bill piles up faster).
Calculus just gives those two everyday instincts a precise picture and a way to compute with them.

If you take one idea from this chapter, take this: **calculus studies change and accumulation — how fast and how much — and its deepest surprise is that these two are inverses, each one undoing the other.**
Everything in this book is built from those two questions and that one connection.

## Two questions, one subject

Every quantity that varies has two natural questions attached to it, and calculus is the study of both.

The first question is *how fast?*
When you press the gas, your speed is the rate at which your position changes.
When a savings account earns interest, the rate is how fast the balance grows.
The **rate of change** of a quantity is simply how much it shifts for each small step forward — how steeply it is climbing or falling at a given moment.
The branch of calculus that answers "how fast?" is built around the **derivative**, which is nothing more than a rate of change made exact, pinned down to a single instant.
You will meet the derivative properly in Chapter 5; for now, hold onto the word as "how fast, right now."

The second question is *how much?*
If you know the rate at every moment — how fast the water pours in each second — you can ask how much has collected in total.
This is **accumulation**, the running total built up by a rate acting over an interval.
The tool that answers "how much?" is the **integral**, which adds up a quantity that is changing the whole time it is being added.
The integral is the star of Chapter 9.

<figure>
<img src="assets/figures/change-and-accumulation.svg" alt="Two side-by-side plots sharing the same rising curve. On the left, a straight line touches the curve at one point, its steepness labeled 'how fast — the derivative'. On the right, the region between the curve and the horizontal axis is shaded, labeled 'how much — the integral'.">
<figcaption>The same curve, two questions. The steepness at a point (left) answers "how fast"; the shaded area beneath it (right) answers "how much." Calculus is the study of both, and of how they connect.</figcaption>
</figure>

!!! intuition "Intuition"
    Calculus is the mathematics of anything that changes.
    Where ordinary algebra handles fixed quantities — this price, that distance — calculus handles *moving* ones, and answers the two questions a moving quantity always raises: how fast is it changing, and how much has it added up to?

!!! analogy "Analogy"
    Think of a movie versus a photograph.
    Algebra hands you a photograph: one frozen frame, everything still.
    Calculus hands you the whole movie: it can tell you the speed of any moving object in any single frame (the derivative) and the total distance it travels across the whole reel (the integral).
    The analogy leaks in one place worth naming: a real movie is a stack of separate frames, while calculus imagines change flowing *smoothly*, with no smallest frame at all — which is exactly the subtlety that makes it powerful and, at first, slippery.

!!! note "Note"
    "How fast" and "how much" are not exotic.
    Speed, growth rate, and slope are all the first question wearing different clothes; total distance, area, and accumulated cost are all the second.
    A large part of learning calculus is recognizing an old friend under a new costume.

## Zooming in and adding up

Each of the two questions is answered by one signature move, and once you see the two moves you have seen the shape of the entire subject.

The move for "how fast" is **zoom in until the curve looks straight**.
Steepness is easy to measure on a straight line and hopeless on a curve, because a curve's steepness keeps changing as you slide along it.
So calculus performs a trick: it magnifies the curve near a single point, again and again.
A curve that looks bent from far away looks nearly straight up close, the way the round Earth looks flat from a sidewalk.
Zoom in far enough and the curve and a straight line become indistinguishable — and *that* straight line has a steepness you can just read off.
That steepness is the derivative.

The move for "how much" is **slice thin and add up**.
Suppose you want the area of a region with a curved top, a shape no tidy formula covers.
Calculus chops it into a row of tall, skinny rectangles, each so narrow that its curved top is nearly flat, so its area is just an easy width-times-height.
Add up all the rectangles and you get *close* to the true area.
Make the slices thinner and there are more of them, but the total sharpens toward one exact answer.
That exact total is the integral.

<figure>
<img src="assets/figures/two-moves.svg" alt="Two panels. Left: a curve with a small inset box magnifying a tiny piece of it, and inside the magnified box the piece looks like a straight line — labeled 'zoom in until curved looks straight'. Right: the region under a curve filled with many thin vertical rectangles that follow the curve's shape — labeled 'slice thin and add up'.">
<figcaption>The two moves of calculus. Zoom in and any smooth curve looks straight, so its steepness becomes readable (left, the derivative). Slice a curved region into thin rectangles and their areas sum toward an exact total (right, the integral).</figcaption>
</figure>

Both moves lean on the same quiet trick: do something *almost* right at a finite scale, then let the scale shrink toward zero and watch the answer settle.
"Almost straight" becomes exactly straight; "almost the area" becomes exactly the area.
The careful name for "the value an answer settles toward as you shrink the scale" is the **limit**, and it is the single idea holding all of calculus together.
It gets its own chapter next (Chapter 3), because getting it right is what separates calculus from wishful thinking.

!!! probe "Wait, why?"
    *A curve isn't actually straight, and a region's top isn't actually flat. Doesn't pretending they are just give a wrong answer?*
    At any fixed zoom or any fixed slice width, yes — you get an approximation, deliberately.
    The escape is that you never stop at a fixed scale.
    You ask what your approximations *head toward* as the scale shrinks without limit, and that target is a single, exact number.
    You are not claiming the curve is straight; you are claiming its steepness is whatever the ever-straighter zoomed pictures agree on.
    "Exact" here means the limit of the approximations, not any one of them.

!!! warning "Common trap"
    "Slice thin and add up" is not the same as "just make the slices zero-width."
    A rectangle of zero width has zero area, so a sum of them is zero — useless.
    The integral is not what you get *at* zero width; it is what the growing pile of ever-thinner slices *approaches* as their width shrinks.
    Same for the derivative: you never actually divide by a zero-sized step.
    Both moves live in the approach, never at the destination itself — which is precisely why the limit (Chapter 3) has to come first.

## The two moves are secretly one

Here is the twist that makes calculus a single subject rather than two tricks that happen to share a textbook: the two moves undo each other.

Return to the bathtub.
The rate the water pours in (a "how fast" story) and the total water collected (a "how much" story) are locked together.
Given the rate at every instant, you can accumulate it to recover the total — that is integration.
Given the total at every instant, you can measure how fast it is climbing to recover the rate — that is differentiation.
Do one and then the other and you arrive back where you started.
They are inverse operations, the way multiplying by three and dividing by three send you on a round trip home.

<figure>
<img src="assets/figures/inverse-pair.svg" alt="Two boxes side by side. The left box reads 'how much: total accumulated (the integral)'. The right box reads 'how fast: rate of change (the derivative)'. A curved arrow labeled 'differentiate' points from the left box to the right; a second curved arrow labeled 'integrate' points from the right box back to the left. A caption below reads 'each undoes the other'.">
<figcaption>Accumulation and rate are two ends of one bridge. Differentiating a total gives back its rate; integrating a rate gives back the total. Each operation undoes the other — the heart of the Fundamental Theorem of Calculus.</figcaption>
</figure>

This round trip has a name: the **Fundamental Theorem of Calculus**, the statement that differentiation and integration are inverse processes [@strang2010].
It is the payoff of the whole book, and it earns its own chapter (Chapter 10).
Its practical magic is enormous: it means the hard question — adding up infinitely many shrinking slices to get an exact total — can be answered by running the *easy* question backward, without ever summing a single slice by hand.
"How much" gets solved by undoing "how fast."

!!! probe "Wait, why?"
    *Why is it surprising that these two are connected? Shouldn't a subject's parts fit together?*
    What is surprising is *how tightly* they fit.
    "How steep is this curve here?" and "how much area sits under that curve?" look like completely unrelated geometry questions — one is about slopes, the other about regions.
    There is no obvious reason a fact about steepness should hand you a fact about area.
    The Fundamental Theorem says it always does, exactly, for every reasonable curve.
    Two questions people studied separately for centuries turned out to be one question asked from two sides.

!!! note "Note"
    This is why the book is ordered the way it is.
    Part I builds the limit, the shared engine of both moves.
    Part II uses it to answer "how fast" (derivatives), Part III to answer "how much" (integrals), and the Fundamental Theorem ties the two together.
    Everything after extends the same two questions to new settings — infinite sums, several variables, whole fields of vectors — but never leaves them behind.

So when the algebra gets thick later on, keep this chapter's map in your pocket.
Underneath every technique you will learn, there are only ever two questions — how fast, and how much — and one beautiful fact that they are the same question in disguise.
