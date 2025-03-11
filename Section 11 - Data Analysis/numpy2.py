print("letss gooooooooooo")
'''
List - slow , high memory 
Numpy - 60 - 100 times faster , uses less memory

'''
import numpy as np 

lst = [ 1,2,3,4,5]
print(lst)

numpy_array = np.array([1,2,3,4,5])
print(numpy_array)


# 1d array - 1 dimention array

ar_1d = np.array([10,20,30,40,50])


# 2d array - 2 dimention array
ar_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(ar_2d)
print(ar_2d.ndim)

# matrix - multi dimention array
matrix = np.array([
    [2,4,6],
    [8,10,12],
    [9,43,22]
])

print(matrix)
print(matrix.ndim)

# creating arrays from python lists

marks = [65,32,25,67,89]

marks_array = np.array(marks)

print(marks_array)
print(marks_array.ndim)

# array with default values 

zero_array = np.zeros((4,5))
print(zero_array)


# array with one

one_array = np.ones((5,6))
print(one_array)

# array with a specif number

full_array = np.full((5,6),7)
print(full_array)