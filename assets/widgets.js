/* Interactive figures for the book — dependency-free, offline, no CDN.
 *
 * Each `<figure class="widget" data-widget="NAME">` in a chapter is wired up on
 * load by the matching entry in WIDGETS below. A widget builds a responsive
 * hi-DPI canvas plus its controls inside the figure (before the <figcaption>),
 * and redraws on input and on resize. To add a widget: write a WIDGETS[name]
 * function and reference it from a chapter with the data attribute.
 *
 * Colors mirror assets/style.css. Keep them in sync with the :root palette.
 */
(function () {
  "use strict";

  var C = {
    ink: "#17181b",
    inkSoft: "#3b3d42",
    muted: "#6a6d73",
    rule: "#e4e3dd",
    ruleStrong: "#cfcdc4",
    accent: "#274b6d",
    accentSoft: "#eaf0f6",
    amber: "#9c6b12",
    amberSoft: "#fdf9f0",
    grid: "#ededea",
  };

  // A responsive hi-DPI canvas inserted into `parent` before `before`.
  function makeCanvas(parent, before, heightRatio) {
    var canvas = document.createElement("canvas");
    canvas.className = "widget-canvas";
    parent.insertBefore(canvas, before);
    var ctx = canvas.getContext("2d");

    function size() {
      var cssW = canvas.clientWidth || parent.clientWidth || 600;
      var cssH = Math.round(cssW * heightRatio);
      var dpr = window.devicePixelRatio || 1;
      canvas.style.height = cssH + "px";
      canvas.width = Math.round(cssW * dpr);
      canvas.height = Math.round(cssH * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      return { w: cssW, h: cssH };
    }

    return { canvas: canvas, ctx: ctx, size: size };
  }

  // A control row (slider + live readout) appended into `parent` before `before`.
  function addSlider(parent, before, label, min, max, step, value) {
    var row = document.createElement("label");
    row.className = "widget-slider";
    var name = document.createElement("span");
    name.className = "widget-slider-label";
    name.innerHTML = label;
    var input = document.createElement("input");
    input.type = "range";
    input.min = min;
    input.max = max;
    input.step = step;
    input.value = value;
    row.appendChild(name);
    row.appendChild(input);
    parent.insertBefore(row, before);
    return input;
  }

  function readoutBox(parent, before) {
    var box = document.createElement("div");
    box.className = "widget-readout";
    parent.insertBefore(box, before);
    return box;
  }

  function controlsBox(parent, before) {
    var box = document.createElement("div");
    box.className = "widget-controls";
    parent.insertBefore(box, before);
    return box;
  }

  // Draw faint gridlines and the x/y axes for a world-to-pixel mapping.
  function drawAxes(ctx, dim, mx, my, xr, yr) {
    ctx.clearRect(0, 0, dim.w, dim.h);
    ctx.lineWidth = 1;
    ctx.strokeStyle = C.grid;
    var i;
    for (i = Math.ceil(xr[0]); i <= Math.floor(xr[1]); i++) {
      ctx.beginPath();
      ctx.moveTo(mx(i), 0);
      ctx.lineTo(mx(i), dim.h);
      ctx.stroke();
    }
    for (i = Math.ceil(yr[0]); i <= Math.floor(yr[1]); i++) {
      ctx.beginPath();
      ctx.moveTo(0, my(i));
      ctx.lineTo(dim.w, my(i));
      ctx.stroke();
    }
    ctx.strokeStyle = C.ruleStrong;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(0, my(0));
    ctx.lineTo(dim.w, my(0));
    ctx.moveTo(mx(0), 0);
    ctx.lineTo(mx(0), dim.h);
    ctx.stroke();
  }

  function plotCurve(ctx, mx, my, xr, f, color, width) {
    ctx.strokeStyle = color;
    ctx.lineWidth = width;
    ctx.lineJoin = "round";
    ctx.beginPath();
    var n = 240;
    for (var i = 0; i <= n; i++) {
      var x = xr[0] + ((xr[1] - xr[0]) * i) / n;
      var px = mx(x);
      var py = my(f(x));
      if (i === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.stroke();
  }

  function dot(ctx, x, y, r, color) {
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.arc(x, y, r, 0, Math.PI * 2);
    ctx.fill();
  }

  function fmt(v) {
    return (v >= 0 ? " " : "") + v.toFixed(2);
  }

  var WIDGETS = {};

  // Secant line sliding into the tangent as h shrinks. f(x) = x^2.
  WIDGETS["tangent-secant"] = function (figure, cap) {
    var f = function (x) {
      return x * x;
    };
    var xr = [-3, 3];
    var yr = [-1.2, 8];
    var cv = makeCanvas(figure, cap, 0.62);
    var controls = controlsBox(figure, cap);
    var readout = readoutBox(figure, cap);
    var aInput = addSlider(controls, null, "point&nbsp;<em>a</em>", -2.4, 2.4, 0.05, 1);
    var hInput = addSlider(controls, null, "gap&nbsp;<em>h</em>", 0.05, 2.5, 0.05, 1.6);

    function draw() {
      var dim = cv.size();
      var pad = 8;
      var mx = function (x) {
        return pad + ((x - xr[0]) * (dim.w - 2 * pad)) / (xr[1] - xr[0]);
      };
      var my = function (y) {
        return dim.h - pad - ((y - yr[0]) * (dim.h - 2 * pad)) / (yr[1] - yr[0]);
      };
      var ctx = cv.ctx;
      var a = parseFloat(aInput.value);
      var h = parseFloat(hInput.value);
      var secant = (f(a + h) - f(a)) / h;
      var tangent = 2 * a;

      drawAxes(ctx, dim, mx, my, xr, yr);
      plotCurve(ctx, mx, my, xr, f, C.ink, 2.5);

      // Tangent line at a (the limit), drawn faint and dashed underneath.
      ctx.save();
      ctx.setLineDash([5, 4]);
      ctx.strokeStyle = C.amber;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(mx(xr[0]), my(f(a) + tangent * (xr[0] - a)));
      ctx.lineTo(mx(xr[1]), my(f(a) + tangent * (xr[1] - a)));
      ctx.stroke();
      ctx.restore();

      // Secant line through the two points, extended across the view.
      ctx.strokeStyle = C.accent;
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(mx(xr[0]), my(f(a) + secant * (xr[0] - a)));
      ctx.lineTo(mx(xr[1]), my(f(a) + secant * (xr[1] - a)));
      ctx.stroke();

      dot(ctx, mx(a), my(f(a)), 5, C.accent);
      dot(ctx, mx(a + h), my(f(a + h)), 5, C.amber);

      readout.innerHTML =
        '<span class="widget-num secant">secant slope = ' +
        fmt(secant) +
        "</span>" +
        '<span class="widget-num tangent">tangent slope (h→0) = ' +
        fmt(tangent) +
        "</span>";
    }

    aInput.addEventListener("input", draw);
    hInput.addEventListener("input", draw);
    window.addEventListener("resize", draw);
    draw();
  };

  // Riemann rectangles filling the area under f(x) = x^2 on [0, 2] as n grows.
  WIDGETS["riemann"] = function (figure, cap) {
    var f = function (x) {
      return x * x;
    };
    var lo = 0;
    var hi = 2;
    var trueArea = (hi * hi * hi) / 3 - (lo * lo * lo) / 3;
    var xr = [-0.25, 2.25];
    var yr = [-0.4, 4.4];
    var cv = makeCanvas(figure, cap, 0.62);
    var controls = controlsBox(figure, cap);
    var readout = readoutBox(figure, cap);
    var nInput = addSlider(
      controls,
      null,
      "rectangles&nbsp;<em>n</em>",
      1,
      80,
      1,
      6
    );

    function draw() {
      var dim = cv.size();
      var pad = 8;
      var mx = function (x) {
        return pad + ((x - xr[0]) * (dim.w - 2 * pad)) / (xr[1] - xr[0]);
      };
      var my = function (y) {
        return dim.h - pad - ((y - yr[0]) * (dim.h - 2 * pad)) / (yr[1] - yr[0]);
      };
      var ctx = cv.ctx;
      var n = Math.round(parseFloat(nInput.value));
      var dx = (hi - lo) / n;
      var sum = 0;

      drawAxes(ctx, dim, mx, my, xr, yr);

      // Midpoint rectangles.
      ctx.fillStyle = C.accentSoft;
      ctx.strokeStyle = C.accent;
      ctx.lineWidth = 1;
      for (var i = 0; i < n; i++) {
        var left = lo + i * dx;
        var mid = left + dx / 2;
        var hgt = f(mid);
        sum += hgt * dx;
        var x0 = mx(left);
        var x1 = mx(left + dx);
        var y0 = my(0);
        var y1 = my(hgt);
        ctx.fillRect(x0, y1, x1 - x0, y0 - y1);
        ctx.strokeRect(x0, y1, x1 - x0, y0 - y1);
      }

      plotCurve(ctx, mx, my, xr, f, C.ink, 2.5);

      readout.innerHTML =
        '<span class="widget-num secant">' +
        n +
        " rectangles → area ≈ " +
        sum.toFixed(3) +
        "</span>" +
        '<span class="widget-num tangent">true area = ' +
        trueArea.toFixed(3) +
        "</span>";
    }

    nInput.addEventListener("input", draw);
    window.addEventListener("resize", draw);
    draw();
  };

  function boot() {
    var figures = document.querySelectorAll("figure.widget[data-widget]");
    Array.prototype.forEach.call(figures, function (figure) {
      var name = figure.getAttribute("data-widget");
      var builder = WIDGETS[name];
      if (!builder) return;
      var cap = figure.querySelector("figcaption");
      builder(figure, cap);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
