class Teque:
    def __init__(self):
        self.arr = []

    def __setitem__(self, i, x):
        self.arr[i] = x

    def __getitem__(self, i):
        return self.arr[i]

    def __str__(self):
        return str(self.arr)

    def push_front(self, x):
        self.arr.insert(0, x)

    def push_back(self, x):
        self.arr.append(x)

    def push_middle(self, x):
        k = len(self.arr)
        i = (k + 1) // 2
        self.arr.insert(i, x)

    def get(self, i):
        if self.arr[i] not in self.arr:
            print("")
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

# notat: t_test.txt er en fil jeg lagde, som inneholder alle eksempel-inputtene
"""
python3 teque.py < t_test.txt
3
5
9
5
1

"""
