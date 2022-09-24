

class Node:
	def __init__(self, element):
		self.element = element
		self.right = None 
		self.left = None 
		self.height = 0


class AVL:
    """
    We assume a balanced tree as an input 
    """
	def insert(self, v, x):
		"""
		args:
			v: a Node 
			x: element 

        output:
            Returns as a new node with the new insert, albeit right or left
		"""
        if v == None:
            Node = Node(x)
            Node.height += 1 
        elif (x < v.element):
            v.left = self.insert(v.left, x)
        elif (x > v.element):
            v.right = self.insert(v.right, x)
    return v

    def contains(self, v, x):
    """
        args:
            v: a Node 
            x: element 

        output:
            Returns as a new node with the new insert, albeit right or left
        """     """
        args:
            v: a Node 
            x: element 

        output:
            Returns boolean whether the tree contains the node
    """
        if v == None:
            return None
        elif v.element == x:
            return True 
        elif v.element < x:
            return self.contains(v.left, x)
        elif v.element > x:
            return self.contains(v.right x)
        else:
            return False 

    def findMin(v):
        """
        Tries to find the smallest node-child of the input-node given
        args:
            v: node 

        output:
            Returns a node with the smallest element 
        """
        current = v 
        while current != None:
            current = current.left 
        return current 

    def remove(v, x):
        """
        args:
            v: a input node
            x: element x

        output:
            removes the input-element which occurs in node v
        """
        if v == None:
            return None

        elif x < v.element:
            v.left = remove(v.left, x)
            return v 
        elif x > v.element:
            v.right = remove(v.right, x)
            return v 

        elif v.left == None:
            return v.right 
        elif v.right == None: 
            return v.left 

        u = self.findMin(v)
        v.element = u.element 
        v.right = remove(v.right, u.element)
        return v 







