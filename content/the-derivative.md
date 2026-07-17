Speed is a stranger idea than it looks. Your car's speedometer reads 60 miles per hour at the instant you glance at it — but "miles per hour" is a comparison stretched across a whole hour, and your glance took no time at all. How can something that seems to need an interval to even define have a value at a single frozen instant? The derivative is calculus's answer. And it turns out to be the very same question as: how steep is a curve at a single point?

If you take one idea from this chapter, take that one: **a derivative is a slope, and a slope is a rate of change.** Everything below is just making that precise without letting the "single instant" part fall apart in our hands.

## Slope at a single point

Start with something friendlier than speed: the steepness of a hill, drawn as a graph. For a straight line, steepness is easy. Pick any two points, measure how much you climb (the *rise*) and how far you walk across (the *run*), and divide. That ratio, rise over run, is the **slope**, and for a straight line it is the same no matter which two points you pick.

A curve is not so obliging. Its steepness changes as you move along it — gentle here, brutal there — so "what is the slope of this curve?" has no single answer. We have to ask a sharper question: what is the slope *right here*, at one specific point?

!!! intuition "Intuition"
    The derivative is nothing more than "how steep is the curve, right at this point?" — the slope of the straight line that grazes the curve there without cutting across it.

Here is the trick that makes it work, and it is the whole of differential calculus in one move. We cannot measure steepness at a single point directly, because slope needs *two* points to compare. So we cheat, and then we fix the cheat. Pick your point and call its input $a$. Now pick a *second* point a little to the right, a gap of $h$ away, at input $a + h$. Draw the straight line through those two points. That line is a **secant**, and its slope is something we can actually compute:

$$\text{secant slope} = \frac{f(a+h) - f(a)}{h}.$$

That is the *average* steepness between the two points — not quite what we want, but close. And now the move: **slide the second point toward the first.** Shrink $h$. As the gap closes, the secant pivots, and it settles toward one particular line — the **tangent**, the line that touches the curve at just that one point. The slope the secant settles on is the derivative.

Try it. In the figure below, drag the sliders: move the point $a$ anywhere along the curve $f(x) = x^2$, and shrink the gap $h$ toward zero. Watch the blue secant swing into the amber tangent, and watch the two slope numbers close in on each other.

<figure class="widget" data-widget="tangent-secant">
<figcaption>The secant slope (blue) is the average steepness across a gap of width h. As you shrink h, the secant pivots into the tangent (amber), and the secant slope closes in on the derivative — which for this curve is always exactly 2a.</figcaption>
</figure>

!!! analogy "Analogy"
    Your speedometer does exactly this. It cannot read your speed at a frozen instant either, so it watches how far you travel over a tiny sliver of time and divides. Make the sliver short enough and the answer stops wobbling — that settled number is your instantaneous speed, which is precisely the derivative of your position.

!!! probe "Wait, why?"
    *If I need two points just to define a slope, how can a slope at a single point mean anything at all?*
    It means the number that the two-point slopes are heading toward as the points merge. No single pair of points hands it to you — but the *trend* of all those shrinking pairs does, and that trend is a perfectly definite number. "The slope at one point" is shorthand for "the value the nearby average slopes are closing in on."

There is one move you are *not* allowed to make, and it is the tempting one.

!!! warning "Common trap"
    You cannot simply set $h = 0$ in the secant formula to jump to the answer. Do it and you get $\frac{f(a) - f(a)}{0} = \frac{0}{0}$, which is meaningless — zero divided by zero could be anything at all. The limit is not a fancy way of writing "plug in zero"; it is the careful way of asking what the ratio *approaches* for tiny nonzero $h$, which sidesteps the $0/0$ completely.

For $f(x) = x^2$ you can watch the escape happen in symbols. The secant slope is

$$\frac{(a+h)^2 - a^2}{h} = \frac{2ah + h^2}{h} = 2a + h.$$

Once we cancel, the $h$ in the denominator is *gone*, and letting $h$ shrink to zero is now completely safe: the slope approaches $2a$. That is why, no matter where you drag the point, the widget's tangent slope always reads exactly twice the value of $a$.

## The derivative as a function

Notice what we actually found. At *every* point $a$, the slope of $x^2$ turned out to be $2a$. We did not solve a one-off problem; we found a rule that works everywhere. Feed in any input, get back the steepness of the curve there. That rule is itself a function — the **derivative function**, written $f'$ and read "f prime."

So the function $f(x) = x^2$ has derivative $f'(x) = 2x$. The original reports *heights*; its derivative reports *slopes*. Where the parabola is falling, on its left side, $f'$ is negative. At the very bottom, where the curve flattens for an instant, $f'$ passes through zero. On the climbing right side, $f'$ is positive and grows as the climb steepens. The derivative is a running commentary on how the original function is changing [@strang2010].

<figure>
<img src="assets/figures/derivative-pair.svg" alt="Two curves on the same axes: the upward-opening parabola f of x equals x squared, and the straight line f prime of x equals 2x through the origin. Where the parabola falls the line is below zero; under the parabola's flat bottom the line crosses zero; where the parabola climbs steeply the line is high.">
<figcaption>The parabola reports heights; its derivative reports slopes. The straight line crosses zero exactly beneath the parabola's flat bottom, and climbs as the parabola steepens.</figcaption>
</figure>

Reading a function and its derivative together, like this, is the skill the rest of Part II is built on. Every shortcut in the next chapter is really a way to get from the height-function to the slope-function *without* redoing the sliding-secant limit by hand every single time.
