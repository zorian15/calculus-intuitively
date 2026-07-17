Before calculus asks you to do anything hard, it quietly assumes you are comfortable with a few small things.
Not many, and not deep — but if any of them feel shaky, every later chapter feels shaky too, and that is usually what "I'm bad at math" turns out to mean.
So this chapter is a refresher, and it is meant to feel like relief, not a test.
We will look at exactly three things calculus leans on: a **function** (a rule that turns one number into another), the **graph** of a function (a picture of that rule), and the **slope** of a line (a single number for "how steep").
That is the whole toolkit.
If you already know this, you will move fast; if you don't, we start from the ground and assume nothing.

## A function is a machine

Here is the single most useful way to picture a function.
A **function** is a machine: you drop a number in, it does one fixed thing to it, and one number comes out.
Same input, same output, every time — that is the whole promise a function makes.

<figure>
<img src="assets/figures/function-machine.svg" alt="A diagram of a function as a machine. On the left, an input number 3 travels along an arrow into a labeled box marked f, double x plus 1. On the right, an arrow leaves the box carrying the output number 7. Below, three more input-output pairs are listed: 0 goes to 1, 1 goes to 3, and 5 goes to 11.">
<figcaption>A function is a machine with one job. Feed it an input, it applies its fixed rule, and hands back exactly one output. Here the rule is "double it, then add one," so 3 comes out as 7.</figcaption>
</figure>

The machine in the picture doubles its input and adds one.
Feed it $3$ and it hands back $7$.
Feed it $0$ and you get $1$; feed it $5$ and you get $11$.
Nothing surprising — but notice the discipline of it.
The machine never gets to pick; the rule decides.
And it always returns *exactly one* output, never two.
That "exactly one" is the fine print that makes a function a function, and later it is what lets us talk about *the* slope at a point instead of a fistful of them.

!!! intuition "Intuition"
    A function is a reliable machine: one input in, one output out, by a fixed rule. If you can say what the machine *does* to a number, you know the function.

Now the notation, which is genuinely the scariest-looking part of all of this and genuinely the least deep.
We give the machine a name — usually $f$ — and we write $f(3) = 7$ to mean "feed $3$ into the machine $f$, and $7$ comes out."
That is all $f(3)$ ever means: the output when the input is $3$.
This is **function notation**, the shorthand $f(x)$ for "the output of the machine $f$ when you feed it $x$."

!!! warning "Common trap"
    $f(3)$ is **not** $f$ times $3$. Those parentheses are not multiplication; they are the slot you drop the input into. When you see $f(3)$, read it out loud as "$f$ of $3$" — the output at input $3$ — not "$f$ times $3$." Reading it wrong here quietly wrecks everything downstream.

To capture the whole machine in one line, we use a placeholder $x$ standing for "whatever you feed in" and write the rule once:

$$f(x) = 2x + 1.$$

Read that as a recipe, left to right: take your input $x$, double it, add one, and that is the output.
The $x$ is not a specific number and it is not a mystery to solve for — it is just a name for the empty slot.
Swap in a real number and the machine runs: $f(3) = 2 \cdot 3 + 1 = 7$.

!!! probe "Wait, why?"
    *If $x$ is just a placeholder, why not always write the actual number?*
    Because you want to describe the machine before you know what you'll feed it. Writing $f(x) = 2x + 1$ once tells you the output for *every* possible input at a stroke, instead of listing pairs forever. That single line is the machine's blueprint — and in Chapter 5 the derivative will be a way to build a *new* machine, one that reports how fast this one is changing.

## The graph is a picture of every pair at once

Listing input-output pairs works, but your eye is far better at pictures than at tables.
So we draw the function.
The **graph of a function** is the picture you get by treating each input-output pair as a point — the input measured left-to-right, the output measured up-and-down — and plotting all of them at once.

<figure>
<img src="assets/figures/graph-pairs.svg" alt="The graph of f of x equals x squared, an upward-opening parabola on horizontal and vertical axes. Three points on the curve are marked. From the input value 2 on the horizontal axis, a dashed line rises to the curve and then runs left to the value 4 on the vertical axis, showing the pair 2 goes to 4. Similar dashed guides mark the pairs negative 1 goes to 1 and 3 goes to 9.">
<figcaption>Reading the graph of a function. To find the output at an input, go up from that input to the curve, then across to the height you land at. Every point on the curve is one input-output pair, and the curve is all of them together.</figcaption>
</figure>

The convention is worth saying plainly, because it never changes: the input goes on the horizontal direction, the output on the vertical.
People call the horizontal one the $x$-axis and the vertical one the $y$-axis, and they often write $y = f(x)$ to mean "the height $y$ is the output of $f$ at the input $x$."
So a point on the graph is a pair "(input, height)," and to read the graph you go up from an input until you hit the curve, then across to read off the height.
In the picture, the input $2$ sends you up to the curve and across to height $4$, so $f(2) = 4$ for this particular machine, which squares its input.

!!! analogy "Analogy"
    A graph is a machine's fingerprint. A table of a few pairs is like a few smudges; the graph is the whole print at once, so you can see the machine's *character* — where it rises, where it dips, where it flattens — in a single glance. Where the analogy leaks: a real fingerprint is a fixed scatter of dots, while a graph is usually an unbroken curve because most functions we care about have an output for every input in between, with no gaps. We give that no-gaps property a name, **continuity**, and spend Chapter 4 on it.

Why does this matter for calculus?
Because every big idea ahead is really a question about the *shape* of a graph.
Where is it climbing and where is it falling?
How steep is it right here?
How much area sits underneath it?
You will reason about those by looking at curves, and the whole point of a graph is that it turns a rule you have to compute into a shape you can just see.

!!! probe "Wait, why?"
    *Could one input ever send you to two different heights on the graph?*
    Not for a function. That "exactly one output" rule from the last section shows up here as a clean visual test: any vertical line you draw crosses the graph at most once. If a curve doubled back so some input had two heights, it would fail that test and it would not be a function — and calculus's questions like "how steep is it *here*" would have no single answer.

## Lines, slope, and just enough algebra

Of all the shapes a graph can take, the straight line is the one calculus cares about most — not because lines are exciting, but because the entire subject is built on *approximating* curvy things by straight ones.
So we need one number that captures a line completely: its steepness.

Picture walking up a ramp from left to right.
Two things describe your climb: how far you move *across*, and how far you rise *up* over that span.
The **slope** is the second divided by the first — the rise divided by the run — the amount you climb for each step you take sideways.

<figure>
<img src="assets/figures/rise-over-run.svg" alt="A straight line rising from lower left to upper right on x and y axes. Two points on the line are marked. Between them, a right triangle is drawn: a horizontal leg labeled run, spanning 4 units across, and a vertical leg labeled rise, spanning 2 units up. A caption notes that slope equals rise over run equals 2 over 4 equals one half.">
<figcaption>Slope is rise over run: pick any two points on the line, measure how far up (the rise) and how far across (the run) between them, and divide. Here you climb 2 for every 4 you cross, a slope of one-half. On a straight line the answer is the same for every pair you pick.</figcaption>
</figure>

Pick any two points on the line.
Measure how far you go across between them — the **run** — and how far up — the **rise** — and divide:

$$\text{slope} = \frac{\text{rise}}{\text{run}}.$$

The magic of a straight line is that this ratio is the same no matter which two points you choose.
Steeper lines give bigger slopes; a line going downhill has a negative slope; a flat line has slope zero.

!!! intuition "Intuition"
    Slope answers one question: for each step you take to the right, how much do you go up? That is rise over run — a single number for "how steep, and which way."

A line with a fixed slope is called a **linear function**, and it has a tidy standard form.
If a line has slope $m$ and crosses the vertical axis at height $b$ — that crossing height is the **y-intercept**, the output when the input is $0$ — then its rule is

$$f(x) = mx + b.$$

You have already met one: $f(x) = 2x + 1$ from the first section is a line of slope $2$ and $y$-intercept $1$.
Here $m$ is exactly the rise-over-run steepness, and $b$ just slides the whole line up or down.

Now, the reason slope earns a whole section in a calculus book.
A curve does not have *one* slope — it bends, so its steepness keeps changing.
But if you zoom way in on any smooth curve, a tiny piece of it looks nearly straight, and *that* little straight piece has a slope you can measure.
The derivative, the star of Part II, is exactly this: the slope of a curve at a single point, found by measuring rise over run on shorter and shorter straight pieces until the answer settles.
Everything you just refreshed about lines is the ground that idea stands on.

!!! note "Note"
    That's the through-line of the book in one breath: rise over run is easy on a line and impossible-looking on a curve, and calculus is the set of tricks for doing it anyway. Chapter 3 makes "shorter and shorter until it settles" precise with **limits**; Chapter 5 uses that machinery to pin down the slope of a curve.

Two small algebra moves round out the "just enough," because later chapters use them without pausing.
The first is **rearranging** an equation: doing the same thing to both sides to isolate what you want.
If $y = 2x + 1$ and you would rather have $x$ in terms of $y$, subtract $1$ from both sides and divide by $2$: $x = (y - 1)/2$.
Nothing changes about the relationship; you have just solved for the other letter.

The second is **factoring**: rewriting a sum as a product, which is how you find where an expression equals zero and how you cancel a troublesome term.
The pattern you will see most is the difference of two squares,

$$x^2 - 1 = (x - 1)(x + 1),$$

which you can check by multiplying the right side back out.
This exact move is what rescues the derivative from dividing by zero.
When you compute a slope over a tiny run and get something like $\frac{x^2 - 1}{x - 1}$, factoring the top lets you cancel the $x - 1$ and escape the $\frac{0}{0}$ trap — you'll watch it happen in Chapter 3 and again in Chapter 5.

!!! warning "Common trap"
    You can only cancel a factor that multiplies the *whole* top and the *whole* bottom. In $\frac{(x-1)(x+1)}{x-1}$ the $x-1$ cancels because it is a factor of the entire numerator. You may **not** cancel the $x$ in $\frac{x+1}{x}$ to get $1 + 1$ — there, $x$ is not a factor of the whole top, it is only added to the $1$. Canceling terms that are added, rather than factors that multiply, is one of the most common ways an answer silently goes wrong.

None of this is calculus yet.
It is the floor calculus stands on, and now it is solid.
When the next chapters say "the slope of the curve" or "solve for $x$" or "factor and cancel," you will not have to stop and worry — you have already done it here.
