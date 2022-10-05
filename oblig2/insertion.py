def insertion(A):
    n = len(A)
    for i in range(1, n):
        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1


if __name__ == "__main__":
    A = [80, 91, 7, 33, 50, 70, 13, 321, 12]
    insertion(A)
    print(A)
