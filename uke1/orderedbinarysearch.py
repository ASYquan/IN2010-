import numpy as np

def binary(x, A):
    """
    Variables
    A: en array
    x: element vi ser etter
    """
    print(f"We are looking for {x}")
    x = int(x); 
    low = 0
    high = len(A) - 1
    while low <=high:
        i = (low + high) // 2
        if A[i] == x:
            return True
        elif A[i] < x:
            low = i + 1
        elif A[i] > x:
            high = i - 1
    return False

A = [0,1,2,3,4,5,6,7,8,9,10]
x = 2

print(binary(x,A))
