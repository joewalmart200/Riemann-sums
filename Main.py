import math


def riemann_sum(f, a, b, n, method="midpoint"):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    if a == b:
        return 0.0

    dx = (b - a) / n

    if method == "left":
        return dx * sum(f(a + i * dx) for i in range(n))
    if method == "right":
        return dx * sum(f(a + (i + 1) * dx) for i in range(n))
    if method == "midpoint":
        return dx * sum(f(a + (i + 0.5) * dx) for i in range(n))
    if method == "trapezoid":
        total = 0.5 * (f(a) + f(b)) + sum(f(a + i * dx) for i in range(1, n))
        return dx * total

    raise ValueError(f"Unknown method: {method!r}")


if __name__ == "__main__":
    f = math.sin
    a, b, n = 0, math.pi, 100
    exact = 2.0

    print(f"Integral of sin(x) on [{a}, {b:.4f}] with n = {n}")
    print(f"{'Method':<10} {'Approx':>12} {'Error':>12}")
    for method in ("left", "right", "midpoint", "trapezoid"):
        approx = riemann_sum(f, a, b, n, method)
        print(f"{method:<10} {approx:>12.6f} {abs(approx - exact):>12.2e}")
