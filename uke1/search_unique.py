import numpy as np


def binary(n):
    """
    n : amount

    x : the number that is not in the range 
    A : random Array from range [0, n-1]
    """
    sample = list(range(0, n))
    A = np.random.choice(np.arange(0, n), replace = False, size = n - 1)
    print(A)
    print(sample)
    for i in range(0, len(sample)-1):
        if sample[i] in A:
            arr = np.delete(A, i)
    print(arr)
    return A


print(binary(9))
