import numpy as np
from typing import Union

rng = np.random.default_rng()

def generate_vals(n: int, p: Union[float, list[float]], params: list[list[float, float]], flag: int) -> list[float]:
    vals = []
    while len(vals) < n:
        choice = rng.random()
        if flag == 2:
            if choice <= p: vals.append(rng.normal(params[0][0], params[0][1]))
            elif choice > p: vals.append(rng.normal(params[1][0], params[1][1]))
        elif flag == 4:
            if choice <= p[0]: vals.append(rng.normal(params[0][0], params[0][1]))
            elif p[0] <= choice <= sum(p[:2]): vals.append(rng.normal(params[1][0], params[1][1]))
            elif sum(p[:2]) <= choice <= sum(p[:3]): vals.append(rng.normal(params[2][0], params[2][1]))
            elif sum(p[:3]) <= choice <= 1: vals.append(rng.normal(params[3][0], params[3][1]))
    return vals