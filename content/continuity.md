Here is a test you already know how to run, even if no one ever called it math. Look at the graph of a function and ask: could I have drawn this whole thing without lifting my pen off the paper? If the answer is yes, the function is *continuous* — it flows, with no sudden gaps, no jumps, no places where it flies off to infinity. **Continuity** is exactly that unbroken quality, and it is the quiet promise that makes almost everything in the rest of this book safe to do. This chapter takes the pen-and-paper picture, sharpens it into something precise using the limit you met in Chapter 3, catalogs the three ways a function can break, and then shows why we care so much that it doesn't.

## Drawing without lifting the pen

Start with the picture, because the picture is the whole idea. A continuous function is one whose graph you can trace in a single unbroken stroke. Where it goes up, it goes up smoothly through every height in between; where it turns, it turns without snapping; and at no point does your pen have to hop over a gap or leap to a new level. That is not yet a definition a mathematician would accept, but it is the right thing to hold in your head, and every precise statement below is just this picture said carefully.

!!! intuition "Intuition"
    A function is continuous at a point if the graph doesn't break there — if you can draw straight through that point without lifting your pen.

Now let's make it sharp, and here is where Chapter 3 pays off. Recall that the **limit** of a function as $x$ approaches some input $a$ is the height the function is *heading toward* as you slide your input closer and closer to $a$ — not the height it necessarily reaches, but the one it is aiming at. Continuity is the case where the aim and the arrival agree. The curve is heading toward exactly the height it actually has when it gets there. Nothing surprising happens at the last moment.

Said in plain words: a function is continuous at $a$ when the value it approaches as you near $a$ is the same as the value it actually takes at $a$. In the notation from Chapter 3, that single sentence becomes

$$\lim_{x \to a} f(x) = f(a).$$

Look at how much that little equation is quietly demanding. For it to even make sense, three separate things all have to go right, and it is worth pulling them apart:

- **The point exists.** $f(a)$ has to be an actual number — the function is defined at $a$, so there is a dot on the graph there at all.
- **The limit exists.** As you approach $a$ from the left and from the right, the function has to be heading toward one single height, not two different ones. (Approaching from just one side gives a **one-sided limit**; the full limit exists only when the left-hand and right-hand one-sided limits agree.)
- **They match.** The height it's heading toward and the height it actually has are the *same* number.

Knock out any one of those three and the pen has to lift. The next section is really just a tour of the three ways to knock one out.

<figure>
<img src="assets/figures/continuity-condition.svg" alt="A smooth curve with a point marked at input a. Arrows along the curve approach the point from the left and from the right, both arriving at a single filled dot at height f of a. Dashed guide lines drop from the dot to the axes, marking the input a and the value f of a.">
<figcaption>Continuity in one glance: the curve approaches from both sides and lands on the very dot it was aiming at. The height it heads toward equals the height it actually has, so the limit equals the value and the pen never lifts.</figcaption>
</figure>

!!! probe "Wait, why?"
    *Doesn't the limit always equal the value? Isn't that just what plugging in $x = a$ does?*
    For the nice, unbroken functions you meet most often, yes — and that is exactly why continuity feels invisible until it fails. But the limit and the value are answers to two genuinely different questions. The limit asks "where is the function *headed* near $a$?" and never actually visits $a$ to find out; the value asks "what does the function *equal* at $a$?" and looks only at that one point. Continuity is the special, common, but not guaranteed situation where those two answers happen to coincide. When they don't, plugging in gives you the wrong picture of what's happening nearby — which is the whole reason Chapter 3 built the limit as a separate tool in the first place.

## The three ways it breaks

When a function fails to be continuous at a point, we call that point a **discontinuity** — a place where the pen must lift. There are exactly three flavors, and telling them apart is a genuinely useful skill, because each one fails a *different* one of the three requirements above. Look at them side by side.

<figure class="wide">
<img src="assets/figures/continuity-breaks.svg" alt="Three small graphs side by side. Left, labeled removable hole: a smooth curve with a single open circle where one point is missing. Middle, labeled jump: a curve that rises to a filled dot, then restarts at a higher open dot, leaving a vertical gap. Right, labeled blow-up: a curve that shoots up toward a dashed vertical line without ever crossing it.">
<figcaption>The three discontinuities, each failing continuity in its own way. A removable hole (left) is a single missing or misplaced point. A jump (middle) is two sides that disagree. A blow-up (right) is the function escaping to infinity at a vertical line.</figcaption>
</figure>

**The removable hole.** This is the gentlest break, and it connects straight back to Chapter 3. The function is heading toward a perfectly good height as you approach $a$ — the limit exists and is finite — but at $a$ itself the point is either *missing* (there's no dot, the function isn't defined there) or *misplaced* (there's a dot, but it sits at the wrong height, off the curve). Everything lines up except the arrival. We call it **removable** because you could fix it with a single dab of ink: drop one point into the hole, or slide the stray point down onto the curve, and the function becomes continuous. Nothing about the surrounding curve has to change. This is the discontinuity that the derivative will lean on constantly, because the secant-slope ratio $\frac{f(a+h)-f(a)}{h}$ from Chapter 5 is undefined at $h = 0$ yet has a perfectly good limit there — a removable hole, waiting to be filled.

!!! note "Note"
    A removable hole is the signature of a $\frac{0}{0}$ expression, like $\frac{x^2 - 1}{x - 1}$ at $x = 1$. Cancel the common factor and you get $x + 1$, which heads toward $2$ as $x \to 1$ — the limit is a clean $2$. But the *original* fraction never got to be defined at $x = 1$, because you can't divide by zero there. Same curve, one missing point. That is a removable hole, and it is exactly the kind of limit the "Common trap" in Chapter 5 warns you not to solve by setting the denominator's variable to zero.

**The jump.** Here the two sides genuinely disagree. As you approach $a$ from the left, the function heads toward one height; from the right, it heads toward a *different* height. The one-sided limits both exist, but they are not equal, so the full limit doesn't exist at all, and the graph shows a clean vertical step. A **jump discontinuity** is what a stair-step looks like: solid ground, then an instant leap to a new level, with your pen forced to hop the gap. No single dab of ink fixes this — the break is baked into the disagreement between the two sides.

!!! analogy "Analogy"
    Think of a parking garage where the price is \$5 for up to two hours and \$12 the moment you pass two hours. Graph the cost against time and you get a jump: right at the two-hour mark the price leaps from \$5 to \$12 with nothing in between. The analogy leaks in one honest way — real prices jump because someone *wrote a rule* with a hard cutoff, whereas a mathematical jump is just a property of the function's shape. But the felt experience is identical: approach the boundary from below and from above, and you arrive at two different answers.

**The blow-up.** The third break is the loudest. Near $a$ the function doesn't head toward any finite height at all — it shoots up toward $+\infty$ or plunges toward $-\infty$, hugging an invisible vertical wall it never crosses. That wall is a **vertical asymptote**: a vertical line $x = a$ that the graph races alongside, getting arbitrarily close without ever touching. The classic case is division by something shrinking to zero, like $\frac{1}{x}$ near $x = 0$: as the denominator vanishes, the quotient explodes. There is no value to plug in and no finite limit to approach, so continuity fails about as badly as it can. This break is sometimes called an *infinite discontinuity*, which is exactly what it is.

!!! warning "Common trap"
    A hole and a blow-up can look similar on a sloppy sketch — both involve a spot where the function "isn't defined" — but they are opposites where it counts. At a removable hole the limit *exists* and is a finite number; the function is well-behaved nearby and only one point is off. At a blow-up the limit does *not* exist because the function runs off to infinity; the whole neighborhood is misbehaving. Before you call a discontinuity "removable," check that the function is actually heading toward a finite height — if it's escaping to infinity, there is nothing to remove.

## Why continuity matters

So far continuity might feel like bookkeeping — a way to sort graphs into "smooth" and "broken." But it is far more than that. Continuity is the fine print under nearly every guarantee calculus makes. The big theorems in the chapters ahead almost all begin, silently, with "let $f$ be a continuous function," and they *need* that clause. Take it away and the guarantees simply stop being true.

Here is the cleanest example, and it is one your intuition already believes. Suppose a function is continuous on an interval, and suppose it starts below some height and ends above it. Then somewhere in between, it *must* pass through that height — it cannot skip over. This is the **Intermediate Value Theorem** (often shortened to IVT): a continuous function on an interval takes every value between its starting and ending heights, at least once. The reason is exactly the pen: to get from a low point to a high point without lifting, your pen has to cross every level in between. There is no way to teleport past a height when you're not allowed to leave the paper.

<figure>
<img src="assets/figures/intermediate-value.svg" alt="A continuous curve running from a low point on the left, labeled f of a, up to a high point on the right, labeled f of b. A dashed horizontal line marks a target height N between them. The curve crosses that line at a point, with a dashed vertical dropping to the input labeled c on the axis.">
<figcaption>The Intermediate Value Theorem, drawn. Because the unbroken curve starts below the target height N and ends above it, it has no choice but to cross N somewhere — at the input c. Continuity is the entire reason the crossing is guaranteed.</figcaption>
</figure>

!!! analogy "Analogy"
    If you were five feet tall at age eight and are six feet tall at age eighteen, then at some moment in between you were exactly five feet six — no skipping allowed, because height grows continuously. You don't need to know *when*; you just know it happened. That "it must have happened somewhere" is the entire content of the Intermediate Value Theorem, and the analogy barely leaks: human height really is a continuous function of time.

Why should you care that a crossing is guaranteed? Because "a continuous function crosses every height in between" is secretly a machine for *solving equations you can't solve by algebra*. Want to know that $x^3 = x + 1$ has a solution? Rewrite it as $f(x) = x^3 - x - 1$ and notice $f(1) = -1$ (negative) while $f(2) = 5$ (positive). Since $f$ is continuous, the IVT guarantees it hits $0$ somewhere between $1$ and $2$ — a solution exists, provably, before you've found a single digit of it. Existence first, value later; that split is one of calculus's quiet superpowers.

!!! probe "Wait, why?"
    *Does the Intermediate Value Theorem really need continuity, or is that just fine print?*
    It genuinely needs it — that is the whole point of stating the clause out loud. Picture the parking-garage jump from the last section: the cost is \$5 just before two hours and \$12 just after, and it never once equals \$8. A broken function can leap clean over a height and never take it, precisely because the jump lets the pen skip. Continuity is exactly the condition that forbids skipping, so it is exactly the condition the theorem cannot do without. Strip it away and the guarantee dies.

Continuity does more than power the IVT, though — it is the ground floor for the two ideas the rest of this book is built on. When you take a **derivative** (Chapter 5), you are taking a limit of slopes, and that limit only behaves if the function isn't tearing apart at the point; a function with a jump or a blow-up has no sensible slope there. In fact, wherever a function *has* a derivative it is automatically continuous, so smoothness sits one level above unbrokenness. And when you take an **integral** (Chapter 9) to add up the area under a curve, continuity is what promises the curve encloses a well-defined region with no gaps punched out of it. The theorems that make integration work — most of all the Fundamental Theorem of Calculus in Chapter 10 — lean on the function being continuous over the stretch you're measuring [@strang2010].

!!! note "Note"
    None of this means broken functions are forbidden or useless — you'll work with plenty of them, and a function can be perfectly continuous everywhere except at a handful of trouble spots. The skill is local: continuity is a property a function has *at each point*, and the real question is never "is this function continuous?" in the abstract but "is it continuous *here*, where I'm about to take a derivative or an integral?" Knowing where the breaks are is knowing exactly where calculus's guarantees do and don't apply.
