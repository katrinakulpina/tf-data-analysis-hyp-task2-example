import pandas as pd
import numpy as np
from scipy.stats import ks_2samp

chat_id = 324047628 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.1
    res = ks_2samp(x, y)
    pval = res.pvalue
    return pval < alpha
