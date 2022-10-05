import numpy as np
from countswaps import *


def ChoosePivot(A, low, high):
    lst = [low, high // 2, high]

    return high
    # return high


def partition(A, low, high):
    p = ChoosePivot(A, low, high)
    print(p)
    A.swap(p, high)
    pivot = A[high]
    left = low
    right = high - 1
    while left <= right:
        while left <= right and A[left] <= pivot:
            left += 1
        while right >= left and A[right] >= pivot:
            right -= 1
        if left < right:
            A.swap(left, right)
    A.swap(left, high)
    return left


def MergeSort(A, low, high):
    # Do quicksort here. Use the Sorter's comparison- and swap
    # methods for automatically counting the swaps and comparisons.

    # Use A.swap(i, j) to swap the values at two indices i and j. The swap is
    # counted, when using this method. Comparisons are counted automatically.
    if low >= high:
        return A
    p = partition(A, low, high)
    MergeSort(A, low, p - 1)
    MergeSort(A, p + 1, high)

    return A


def sort(A):
    # This function was created for the use in "innlevering2.py"
    ans = MergeSort(A, 0, len(A) - 1)
    return ans


if __name__ == "__main__":
    lst = [80, 91, 7, 33, 50, 70, 13, 321, 12]
    A = CountSwaps(lst)
    # Quicksort(A, 0, n-1)
    print(sort(A))
