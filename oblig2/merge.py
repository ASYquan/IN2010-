from countswaps import *


def merge(A1, A2, A):
    i = 0
    j = 0
    while i < (len(A1)) and j < (len(A2)):
        if A1[i] <= A2[j]:
            A[i + j] = A1[i]
            i += 1
        else:
            A[i + j] = A2[j]
            j += 1
    while i < (len(A1)):
        A[i + j] = A1[i]
        i += 1
    while j < (len(A2)):
        A[i + j] = A2[j]
        j += 1
    return A


def sort(A):
    # Implementation of MergeSort algorithm
    n = len(A)
    if n <= 1:
        return A
    i = n // 2
    A1 = sort(A[:i])
    A2 = sort(A[i:n])
    return merge(A1, A2, A)


if __name__ == "__main__":
    # O(n*log(n)) in worst case for mergesort (def sort)
    # O(n) in worstcase for merge (def merge)
    # from lectures
    lst = [80, 91, 7, 33, 50, 70, 13, 321, 12]
    A = CountSwaps(lst)
    print(sort(A))
