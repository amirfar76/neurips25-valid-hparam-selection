
import numpy as np
from scipy.stats import binom

def one_sided_binomial_pval(k, n, p0):
    k = int(k); n = int(n)
    if k <= 0:
        return 1.0
    if k > n:
        return 0.0
    return float(binom.sf(k-1, n, p0))

def hoeffding_pval(mean_loss, n, alpha):
    gap = max(0.0, alpha - float(mean_loss))
    return float(np.exp(-2.0 * n * gap * gap))

def quantile_exceedances_pvalue(losses, target_q, tau):
    losses = np.asarray(losses)
    n = losses.shape[0]
    successes = int(np.sum(losses <= target_q))
    # Evidence that success rate >= tau: use upper tail
    return float(binom.sf(successes-1, n, tau))

def holm_bonferroni(pvals, alpha=0.05):
    pvals = np.asarray(pvals, dtype=float)
    m = pvals.size
    order = np.argsort(pvals)
    rej = np.zeros(m, dtype=bool)
    passed = True
    for j, idx in enumerate(order):
        thr = alpha / (m - j)
        if pvals[idx] <= thr and passed:
            rej[idx] = True
        else:
            passed = False
    return rej

def benjamini_hochberg(pvals, alpha=0.1):
    pvals = np.asarray(pvals, dtype=float)
    m = pvals.size
    order = np.argsort(pvals)
    ranked = pvals[order]
    crit = alpha * (np.arange(1, m+1) / m)
    k = np.where(ranked <= crit)[0]
    rej = np.zeros(m, dtype=bool)
    if k.size > 0:
        kmax = int(k.max())
        rej[order[:kmax+1]] = True
    return rej

def weighted_bh(pvals, weights, alpha=0.1):
    pvals = np.asarray(pvals, dtype=float)
    w = np.asarray(weights, dtype=float)
    if np.any(w <= 0):
        raise ValueError("weights must be positive")
    m = pvals.size
    w = w * (m / np.sum(w))
    adj = pvals / w
    order = np.argsort(adj)
    ranked = adj[order]
    crit = alpha * (np.arange(1, m+1) / m)
    k = np.where(ranked <= crit)[0]
    rej = np.zeros(m, dtype=bool)
    if k.size > 0:
        kmax = int(k.max())
        rej[order[:kmax+1]] = True
    return rej

def pareto_mask(values, minimize=True):
    V = np.asarray(values, dtype=float)
    m, d = V.shape
    mask = np.ones(m, dtype=bool)
    for i in range(m):
        if not mask[i]:
            continue
        vi = V[i]
        for j in range(m):
            if i == j:
                continue
            vj = V[j]
            if minimize:
                if np.all(vj <= vi) and np.any(vj < vi):
                    mask[i] = False
                    break
            else:
                if np.all(vj >= vi) and np.any(vj > vi):
                    mask[i] = False
                    break
    return mask
