import numpy as np


class Teque:
    def __init__(self):
        self.arr = [None]

        def __setitem__(self, i, x):
            self.arr[i] = x

    def __getitem__(self, i):
        return self.arr[i]

    def __str__(self):
        return str(self.arr)

    def push_front(self, x):
        self.arr[0] = x

    def push_back(self, x):
        self.arr.append(x)

    def push_middle(self, x):
        k = len(self.arr)
        i = (k + 1) // 2
        self.arr.insert(i, x)

    def get(self, i):
        print(self.arr[i])


if __name__ == "__main__":
    t = Teque()
    line = 0
    num = int(input())
    for i in range(num):
        ins = input()

        lst = ins.split()
        if len(lst) == 2:
            line += 1
            (eval(f"t.{lst[0]}({lst[1]})"))
        else:
            line += 1
            (eval(f"t.{lst[0]}()"))
