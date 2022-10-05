from countswaps import *


def sort(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j] > A[j + 1]:
                A.swap(j, j + 1)
    return A


if __name__ == "__main__":
    # O(nˆ2) i worst case
    # from lectures
    lst = [80, 91, 7, 33, 50, 70, 13, 321, 12]
    A = CountSwaps(lst)
    obj = sort(A)
    print(obj)
