import heapq as hp


class Heap:
    def __init__(self, lst):
        hp.heapify(lst)
        # print(type(lst))
        self.heap = lst

    def heap_push(self, x):
        hp.heappush(self.heap, x)

    def heap_pop(self):
        hp.heappop(self.heap)

    def __str__(self):
        return str(self.heap)

    def __setitem__(self, i, x):
        self.heap[i] = x

    def __getitem__(self, i):
        return self.heap[i]

    def __len__(self):
        return len(self.heap)


def start_of_file():
    while True:
        try:
            stdin = input().split()
        except EOFError:
            return
        for inputs in stdin:
            ins_lst.heap_push(int(inputs))


def balanced_binary_search(heap):
    if not heap:
        return None
    median = len(heap) // 2
    lst.append(heap[median])
    bst.heap_push(heap[median])

    h_right = balanced_binary_search(heap[(median + 1) :])
    h_left = balanced_binary_search(heap[:median])


if __name__ == "__main__":
    ins_lst = Heap([])
    start_of_file()
    lst = []
    bst = Heap([])

    balanced_binary_search(ins_lst)
    print(bst)
    print(lst)

# Litt usikker på hva output skal være. Printer ut begge for sikkerhetsskyld.
# lst : en liste som inneholder et balansert binærtre.
# bst : en heap som inneholder balansert binærtre.
# balance_test.txt er et tekst-fil jeg lagde for å teste metoden min

"""python3 balanced_heap.py < balance_test.txt
[0, 1, 5, 4, 2, 10, 6, 9, 7, 8, 3]
[5, 8, 10, 9, 7, 6, 2, 4, 3, 1, 0]

"""
