import sys
import matplotlib.pyplot as plt
from numpy import pi, exp, sqrt
from generate_vals import generate_vals as gv
from gm_em_alg import gaussian_mixture_em as gm_em

task = int(sys.argv[1])
if task == 1:
    n = 500
    p = 2 / 3
    params = [[10, 1], [5, 1]]

    vals = gv(n, p, params, flag=2)
    start_p, start_point = [0.51, 0.49], [[6, 1], [3, 1]]

elif task == 2:
    n = 1000
    p = [0.25, 0.25, 0.25, 0.25]
    params = [[-20, 2], [0, 5], [3, 4], [10, 3]]

    vals = gv(n, p, params, flag=4)
    start_p, start_point = [0.2, 0.6, 0.1, 0.1], [[5, 2], [4, 1], [6, 1], [4, 1]]

p, point = gm_em(start_p, start_point, vals, iters=64)

fig, ax = plt.subplots(1, 1)
count, bins, ignored = plt.hist(vals, 30, fc="yellow", ec='blue', alpha=0.4, density=True)
for i in range(len(p)):
    plt.plot(bins, 1/(point[i][1] * sqrt(2 * pi)) * exp( - (bins - point[i][0]) ** 2 / (2 * point[i][1] ** 2)) * p[i], 
        label='p = {:.3f}, mu = {:.3f}, st_dev = {}'.format(p[i], point[i][0], point[i][1]), linewidth=4, color='blue')
plt.legend(loc='upper left')
plt.show()