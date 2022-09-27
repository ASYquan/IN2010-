class TreeNode:
    def __init__(self, x=None):
        self.element = x
        self.left = None
        self.right = None
        self.parent = None


def depth(v):
    """
    Input: En node v
    Output: Dybden av noden
    """
    if not v:
        return -1
    return 1 + depth(v.parent)


def height(v):
    h = -1
    if not v:
        return h
    leftAns = height(v.left)
    rightAns = height(v.right)
    return max(leftAns, rightAns) + 1


"""Traversal:
we have postorder and preorder
Preorder executes an operation on itself, then the children
Postorder executes an operation on the children, then itself

These methods of traversal can be useful when copying and deleting. 
Preorder is good for copying and postorder is good for deletion. 
"""


def preorder_traversal(v, operation=None):
    """
    v: A node that cannot be null

    """
    res = []
    if v:
        res.append(v.element)
        res = res + preorder_traversal(v.left)
        res = res + preorder_traversal(v.right)
    return res


def preorder_operation(v, operation):
    res = []
    # res.append(f"{operation}:")
    if v:
        res.append(eval(f"{operation}(v)"))
        res = res + preorder_operation(v.left, operation)
        res = res + preorder_operation(v.right, operation)
        # print("operation:", operation, ", result:", left_child, "    ", right_child)
    return res


def postorder_traversal(v):
    res = []
    if v:
        res = res + preorder_traversal(v.left)
        res = res + preorder_traversal(v.right)
        res.append(v.element)
    return res


def postorder_operation(v, operation):
    res = []
    # res.append(f"{operation}:")
    if v:
        res = res + preorder_operation(v.left, operation)
        res = res + preorder_operation(v.right, operation)
        # print("operation:", operation, ", result:", left_child, "    ", right_child)
        res.append(eval(f"{operation}(v)"))
    return res


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.parent = root
    root.right.right = TreeNode(4)
    root.right.right.parent = root.right
    # print(depth(root.right.right))
    # print(height(root))
    # print(preorder_traversal(root, "height"))
    print(preorder_traversal(root))
    # print(preorder_operation(root, "height"))
    print(postorder_traversal(root))
    print(postorder_operation(root, "height"))
