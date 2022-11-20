"""

Problem 8.2. Right triangle class

right_triangle.py

"""

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

class RightTriangle:

	def __init__(self, a , b):
		if (a<0 or b<0):
			raise ValueError("Side Lengths <= 0")
		self.a = a
		self.b = b
		c =  math.sqrt((a**2) + (b**2))
		self.c = c

	def plot_triangle(self):
		p = np.array([[0,0], [self.a,0], [0,self.b]])
		poly = Polygon(p, closed=False)
		axis = plt.gca()
		axis.add_patch(poly)
		plt.axis("equal")
		plt.show()	

a1 = 1
b1 = 1
a2 = 3
b2 = 4

t1 = math.sqrt((a1**2)+(b1**2))
t2 = math.sqrt((a2**2)+(b2**2))

triangle1 = RightTriangle(a1,b1)
triangle2 = RightTriangle(a2,b2)

print('The hypotenuse of triangle1 is ', triangle1.c)
print('The hypotenuse of triangle1 is', triangle2.c)

print('Test = calculated hypotenuse of triangle1 is', t1 == triangle1.c) 
print('Test = calculated hypotenuse of triangle2 is', t2 == triangle2.c) 


def test_RightTriangle():

	success = False
	try:
		triangle3 = RightTriangle(1, -1)
	except ValueError:
		success = True
	assert success

test_RightTriangle()

triangle1.plot_triangle()
triangle2.plot_triangle()


#Dette er kjøreeksempeler fra min terminal

"""

> python3 right_triangle.py

The hypotenuse of triangle1 is  1.4142135623730951
The hypotenuse of triangle1 is 5.0
Test = calculated hypotenuse of triangle1 is True
Test = calculated hypotenuse of triangle2 is True

Process finished with exit code 0
	
"""