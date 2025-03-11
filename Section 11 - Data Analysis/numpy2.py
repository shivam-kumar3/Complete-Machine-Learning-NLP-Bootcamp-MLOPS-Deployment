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
matrix = np.array([[
    [2,4,6],
    [8,10,12],
    [9,43,22]]
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

# creating sequences of numbers in numpy 
# arange(start,stop,step)

arr = np.arange(9,12)
print(arr)

# creating identity matrices
# eye(size)

identity_matrix = np.eye(4)
print(identity_matrix)

# ARRAY PROPERTIES AND OPERATIONS

# shape , size , type

print(identity_matrix.shape)

ar_2d = np.array([[1,2,3],
                  [4,5,6],
                  ])
print(ar_2d.shape)
print(ar_2d.size)
print(ar_2d.ndim)
print(ar_1d.ndim)
print(matrix.ndim)

# dtype - dataypes of elements (int, float, str)

arr_float = np.array([10,20,30.6,50])
print(arr_float.dtype)

# astype - convert the data type


arr = np.array([1.2,2.5,3.9])

int_arr = arr.astype(int)
print(arr)
print(int_arr)


age = "100"

age_array = np.array(age, dtype='int')

print(age_array)



# OPERATIONS
'*,%,+,-'

arr = np.array([10,20,30])

print(arr +5 )
print(arr * 5)
print(arr **2)
print(arr % 4)


# aggregation function
'''
np.sum () -  add all elements
np.mean() - avg value 
np.min(array) - smallest value
np.array(array) - max value 
np.std(array) - standard deviation
np.var(array) - variance
'''

arr = np.array([10,20,40,50])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))
print(np.std(arr))
print(np.var(arr))