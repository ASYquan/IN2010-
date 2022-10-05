class Node:
    def __init__(self, element=None):
        self.element = element
        self.right = None
        self.left = None
        self.height = 0


class Set:
    """
    The code is written such that it only works correctly and intended when used
    on a balanced BST.
    """

    def __init__(self):
        self.unit = 0
        self.root_node = None

    def insert(self, v, x):
        """
        args:
                v: a Node
                x: element

        output:
                Returns as a new node with the new insert, albeit right or left
        """

        if self.root_node is None:
            self.root_node = Node(element=x)
            # self.unit += 1

        if v is None:
            self.unit += 1
            return Node(element=x)

        elif x < v.element:
            v.left = self.insert(v.left, x)

        elif x > v.element:
            v.right = self.insert(v.right, x)

        return v

        # v.height = 1 + max((v.left).height, (v.right).height)
        # return self. balance(v)

    def contains(self, v, x):
        """
        args:
            v: a Node
            x: element

        output:
            Returns boolean whether the tree contains the node
        """
        # print(v.element)
        if v is None:
            print("false")  # for CMP to work
            return False
        if v.element == x:
            # return v
            print("true")  # for CMP to work
            return True
        if v.element < x:
            return self.contains(v.right, x)
            # return True
        if v.element > x:
            return self.contains(v.left, x)
            # return True
        # return True

    def findMin(self, v):
        """
        Tries to find the smallest node-child of the input-node given
        args:
            v: node

        output:
            Returns a node with the smallest element
        """
        while v.left is not None:
            v = v.left
        return v

    def remove(self, v, x):
        """
        args:
            v: a input node
            x: element x

        output:
            removes the input-element which occurs in node v
        """
        if v == None:
            # self.unit -= 1
            return None

        if x < v.element:
            v.left = self.remove(v.left, x)
            # self.unit -= 1
            return v

        elif x > v.element:
            v.right = self.remove(v.right, x)
            # self.unit -= 1
            return v
        elif v.left is None:
            if v.element == self.root_node.element:
                self.root_node = v.right
            # v = v.right
            self.unit -= 1
            return v.right

        elif v.right is None:
            if v.element == self.root_node.element:
                self.root_node = v.left
            # v = v.left
            self.unit -= 1
            return v.left

        # print("brukt!")
        u = self.findMin(v.right)
        v.element = u.element
        v.right = self.remove(v.right, u.element)
        return v

    def size(self):
        print(self.unit)
        return self.unit

    def inorder(self, v):
        if v:
            self.inorder(v.left)
            print(v.element)
            self.inorder(v.right)


if __name__ == "__main__":
    s = Set()
    line = 0
    num = int(input())
    for i in range(num):
        ins = input()

        lst = ins.split()
        if len(lst) == 2:
            line += 1
            (eval(f"s.{lst[0]}(s.root_node, {lst[1]})"))
        else:
            line += 1
            (eval(f"s.{lst[0]}()"))
        # print("line:", line)
        # print("inorder:")
        # s.inorder(s.root_node)

    # print("in order")
    # s.inorder(s.root_node)
    # print(s.root_node.right.left.right.right.right.element)

    # print("inorder:")
    # s.inorder(s.root_node)
# print(f" Print of the current BST: \n\n\n {s.inorder(s.root_node)}")

"""
s = Set()
root = None

s.insert(s.root_node, 1)
s.insert(s.root_node, 2)
# print(s.root_node.left)
# s.remove(s.root_node, 1)
# s.size()
# print("remove return:", s.remove(s.root_node, 1).element)

# print("order:")
s.remove(s.root_node, 2)
s.inorder(s.root_node)
"""

"""
 python3 BST.py < inputs/example | cmp - outputs/example


"""
