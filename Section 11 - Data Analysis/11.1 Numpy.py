'''
NUMPY 

NUMPY IS A FUNDAMENTAL LIBRARY FOR SCIENTIFIC COMPUTING IN PYTHON. IT PROVIDES SUPPORT FOR ARRAY AND MATRICS, ALONG WITH A COLLECTION OF MATHEMATICAL FUNCTIONS TO OPERATE ON THESE DATA STRUCTURES.
IN THIS LESSON, WE WILL COVER THE BASICS OF NUMPY , FOCUSING ON ARRAYS AND VECTORIZED OPERATIONS.

'''

import numpy as np

# create array using numpy

#creating a 1d array

arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.ndim)


# creating a 2d array
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2)
print(arr2.ndim)
print(arr2.shape)

#creating 3d array
arr3 = np.array([[[1,2,3,4,5]]])
print(arr3)
print(arr3.ndim)