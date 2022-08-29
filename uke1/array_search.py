import numpy as np


def array_count(A):
    n = np.shape(A)[0]
    m = np.shape(A)[1]
    column = 0
    largest_amnt = [0, 0]
    count = [0, column]
    i = 0
    while True:
        if A[column, i] == 1:
            count[0] += 1
            i += 1
        elif A[column, i] == 0:
            column += 1
            i = 0
            if count[0] > largest_amnt[0]:
                largest_amnt = count

        elif column == m:
            return largest_amnt
            break


A = np.matrix([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
print(A[0, 1])  # Her er problemet
print(A)
print(array_count(A))
