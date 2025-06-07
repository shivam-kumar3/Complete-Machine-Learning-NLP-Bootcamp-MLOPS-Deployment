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

arr7[0,0] = 100

print(arr7)


#statistical concepts -  normlization

# to have a mean of 0 and standard deviation of 1 

mean = np.mean(arr7)
std = np.std(arr7)

nor = (arr7 - mean)/ std

print('Normalized Data :', nor)

'''
np.mean
np.median
np.std
np.variance
'''

# Logical operations

print(arr7[(arr7>5) & (arr7 < 10)])


number = np.array([1,2,3,4,5,6,7,8,9,10])
even_num = number[number % 2 == 0]

print(number)
print(even_num)

# Filter with mask 

mask = number > 5
print(number[mask])

# Fancy indexing vs np.where()

print("-----------------")
indices = [0,3,5]

print(number[indices])

print("-----------------")
where_result = np.where(number>5)
print(number[where_result])
print(where_result)


# Condition array

condition_array = np.where(number > 5 , number , number)
print(condition_array)

# ADDING AND REMOVING DATA

arr = np.array([1,2,3])
arr2 = np.array([4,5,6])

combined = np.concatenate(([[arr,arr2]]))
print(combined)

print(combined.ndim)


original = np.array([[1,2],[3,4]])
new_row = np.array([[5,6]])

new = np.concatenate((original,new_row))
stack = np.vstack((original,new_row))
print(stack)
print('-------------')
print(new)

print('----------------')
new_col = [[7],[8]]
hstack = np.hstack((original,new_col))
print(hstack)


# Delete command using the index

arr = np.array([1,2,3,4,5,6,7])
deleted = np.delete(arr,2)
print(deleted)


# PRACTICAL QUESTIONS

import matplotlib.pyplot as plt

# Data Structure : [resturant_id , 2021,2022,2023,2024]
sales_data = np.array([
    [1,150000,180000,220000,250000],  #Paradise Biryani
    [2,120000,140000,160000,190000],   #Beijing Bites
    [3,200000,230000,260000,300000], #Pizza Hub
    [4,180000,210000,240000,270000],  #Burger Point
    [5,160000,185000,205000,230000] #chai point
    ])


print('< ---------- Zomato Sales Analysis ---------- >')
print('\nSales Data Shape', sales_data.shape)

# 1st three restro sales data
print("Sample data for 1st 3 restro:- \n", sales_data[:3])



'''
Create a NumPy array of integers from 10 to 50 (inclusive), and then extract only the even numbers from it.

Bonus: Reshape the resulting even numbers into a 2D array with 2 rows.

'''

num = np.array(range(10,50))
even_arr = num[num % 2 == 0]

reshaped = even_arr.reshape(2,-1)
print(reshaped)




