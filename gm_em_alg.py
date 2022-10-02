from scipy.stats import norm

Pair = list[float]
Point = list[list[float]]

def f(y: float, p: list[float], point: Point) -> float:
    f = 0
    for i in range(len(p)):
        f += p[i] * norm.pdf(y, point[i][0], point[i][1])
    return f

def w(y: float, f: float, p: float, pair: Pair) -> float:
    return p * norm.pdf(y, pair[0], pair[1]) / f

def gaussian_mixture_em_iter(p: list[float], point: Point, Y: list[float]) -> tuple[list[float], Point]:
    n = len(Y)
    m = len(p)
    new_p = [0] * m
    new_point = [[0, 0]] * m
    for i in range(len(p)):
        new_p[i], new_point[i][0], new_point[i][1], W = 0, 0, 0, 0
        for y in Y:
            fy = f(y, p, point)
            wy = w(y, fy, p[i], point[i])
            new_p[i] += p[i] * norm.pdf(y, point[i][0], point[i][1]) / fy
            new_point[i][0] += y * wy
            new_point[i][1] += ((y - point[i][0]) ** 2) * wy
            W += wy
        new_p[i] = new_p[i] / n
        new_point[i] = [new_point[i][0] / W, (new_point[i][1] / W) ** 0.5]
    return new_p, new_point

def gaussian_mixture_em(p: list[float], point: Point, Y: list[float], iters: int) -> tuple[list[float], Point]:
    for i in range(iters):
        p, point = gaussian_mixture_em_iter(p, point, Y)
        if i in [3, 15, 63]:
            print("iter {}:".format(i), p, point)

    return p, point