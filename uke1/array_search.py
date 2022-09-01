import numpy as np


def array_count(A):
    A = A.T
    n = np.shape(A)[0]
    best_ones, best_column = (0, 0)
    count_ones, column_count = (0, 0)
    i = 0
    while True:
        print(A[column_count, i])
        if A[column_count, i] == 1:
            count_ones += 1
            i += 1
        elif A[column_count, i] == 0:
            if count_ones > best_ones:
                best_ones = count_ones
                best_column = column_count
            column_count += 1
            i = 0
            if column_count == n-1:
                return best_column + 1
                break

 

#A = np.matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
A = np.matrix([[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1,0], [0,0,0,0]])
#print(A)
print(A)
print("best_column:" ,array_count(A))
