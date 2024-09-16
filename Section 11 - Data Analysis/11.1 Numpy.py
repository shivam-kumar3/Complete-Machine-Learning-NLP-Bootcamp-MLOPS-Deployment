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

new = np.arange(0,10).reshape(5,2)

print(new)
print(new.dtype)


# NUMPY VECTORIZED OPERATIONS   

arr4 = np.array([1,2,3,4,5])
arr5 = np.array([10,20,30,40,50])

# element wise addition

print("Addition: ", arr4 + arr5)

# element wise substraction

print("Addition: ", arr4 - arr5)

# element wise substraction

print("Addition: ", arr4 * arr5)


# universal function

# square root
arr6 = np.array([10,20,30,40,50])

print(np.sqrt(arr6))

# exponential
print(np.exp(arr6))

# sin
print(np.sin(arr6))

# natural log

print(np.log(arr6))


# array slicing and indexing 

arr7 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(arr7)

print(arr7[0,0])


print(arr7[1:,2:])

print(arr7[0:2,2:])

print(arr7[1:,1:3])