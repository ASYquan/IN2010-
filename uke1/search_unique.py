import numpy as np


def unique_search(n):
    """
    n : amount

    x : the number that is not in the range
    A : random Array from range [0, n-1]
    """
    sample = list(range(0, n))
    cp = sample.copy()
    A = np.random.choice(np.arange(0, n), replace=False, size=n - 1)
    print(A)
    for i in range(0, len(A) + 1):
        if sample[i] in A:
            cp.remove(sample[i])
    return cp[-1]


print(unique_search(9))
