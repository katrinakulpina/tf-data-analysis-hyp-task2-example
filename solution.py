import pandas as pd
import numpy as np
from hyppo.ksample import MMD

chat_id = 324047628 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.1
    _, pval = MMD(compute_kernel="laplacian", gamma=10).test(x, y)
    return pval < alpha
