def start_of_file():

    while True:
        try:
            stdin = input().split()
        except EOFError:
            return
        for inputs in stdin[1:]:
            init_tree[int(inputs)] = int(stdin[0])
        if (stdin[0]) == "-1":
            break


def get_cat(cat, tree):
    """
    input:
        cat: int
        tree: list

    function: tree search to find the cat

    return:
        path: list
    """
    path = [cat]
    while tree[cat] != None:
        cat = tree[cat]
        path.append(cat)

    return path


if __name__ == "__main__":
    init_tree = [None] * 101
    cats = int(input())
    start_of_file()
    print(get_cat(cats, init_tree))
