

class Node:
	def __init__(self, element):
		self.element = element
		self.right = None 
		self.left = None 
		self.height = 0


class Set:
    def __init__(self):
        self.size = 0
    """
    The code is written such that it only works correctly and intended when used 
    on a balanced BST.  
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
            self.size += 1

        elif (x < v.element):
            v.left = self.insert(v.left, x)

        elif (x > v.element):
            v.right = self.insert(v.right, x)

        v.height = 1 + max((v.left).height, (v.right).height)
        #return self. balance(v)
        

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

    def findMin(self, v):
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

    def remove(self, v, x):
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
            v.left = self.remove(v.left, x)
 
        elif x > v.element:
            v.right = self.remove(v.right, x)

        elif v.left == None:
            v = v.right 

        elif v.right == None: 
            v = v.left 
        else:
            u = self.findMin(v)
            v.element = u.element 
            v.right = self.remove(v.right, u.element)
        v.height = 1 + max((v.left).height, (v.right).height)
        self.size -= 1

    def size(self):
        return self.size








