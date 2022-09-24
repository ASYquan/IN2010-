import numpy as np


def array_count(A):
    column = 0
    largest_amnt = [0, 0]
    count = [0, column]
    for i in range(0, n*m):
        if A[column, i] == 1:
            count[0] += 1
        elif A[column, i] == 0:
            column += 1
            if count[0] > largest_amnt[0]:
                largest_amnt = count
    return largest_amnt


A = np.matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])

print(A)
print(array_count(A))

