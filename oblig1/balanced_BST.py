class BSS:
    def __init__(self, x=None):
        self.element = x
        self.right = None
        self.left = None

    def order(self):
        yield self.value
        if self.left:
            yield from self.left.order()
        if self.right:
            yield from self.right.order()


def balanced_binary_search(v, A):
    if not A:
        return None
    median = len(A) // 2
    v = BSS(A[median])
    v.left = balanced_binary_search(v, A[:median])
    v.right = balanced_binary_search(v, A[(median + 1) :])
    return v


def order(v):
    print(v.element)
    if v.right:
        order(v.right)
    if v.left:
        order(v.left)


def start_of_file():
    while True:
        try:
            stdin = input().split()
        except EOFError:
            return
        for inputs in stdin:
            ins_lst.append(int(inputs))


if __name__ == "__main__":
    ins_lst = []
    start_of_file()
    node = balanced_binary_search(BSS(), ins_lst)
    order(node)

# balance_test.txt er et tekst-fil jeg lagde for å teste metoden min
"""
python3 balanced_BST.py < balance_test.txt
5
8
10
9
7
6
2
4
3
1
0
"""
