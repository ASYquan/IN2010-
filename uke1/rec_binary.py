import numpy as np

def binary(A, low, high, x):
    """
    Variables
    A: en array
    x: element vi ser etter
    """
    if high >= low:
        i = (low + high) // 2
        if A[i] == x:
            return True
        elif A[i] < x:
            return binary(A, i + 1, high, x)
        elif A[i] > x:
            return binary(A, low, i - 1, x)
    else:
        return False
    
arr = [0,1,2,3,4,5,6,7,8,9,10]
x = 11 
print(binary(arr, 0, len(arr) - 1, x))

