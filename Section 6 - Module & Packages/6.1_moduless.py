'''
importing modules in python: Modules and packages

# in python modules and packages help organize and reuse code. here a comprehensive guide on how to import them

'''

import math

print(math.sqrt(16))

from math import sqrt, pi

print(sqrt(16))
print(sqrt(34))
print(pi)


import numpy as np 

n = np.array([1,2,3,4])
print(n)


from package.maths import addition

from package import maths

print(maths.addition(4,3))
print(maths.minus(4,3))


from package.subpack.mult import multiply

print(multiply(43,43))




