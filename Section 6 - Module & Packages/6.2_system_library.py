'''
System Library Overview

Python standard library is a vast collection of modules and packages that come bundled with python, providing a wide range of functionalities out of the box. here an overview of some of the most commonly used modules and packages in the python standard library


'''

import array

arr = array.array("i",[1,2,3,4])

print(arr)

import math

print(math.sqrt(6))
print(math.pi)

# random

import random

print(random.randint(1,10))
print(random.choices(["shivam","shahi","vidu"]))


# file and directoary access

import os
print(os.getcwd())

def cwd(path):
    default = os.getcwd()
    if path == default:
        print("You are in the correct directory ")
    else:
        print(f"You need to switch your path to {default}")

# os.mkdir("test_dir") #this make a new folder

# high level operations on files and collection of files 

import shutil

# shutil.copyfile("source.txt", "destination.txt")


# data serialization

import json

data = {'name':'shivam','age':28}
# convert the data into json format
json_str = json.dumps(data)

print(json_str)
print(type(json_str))

# convert the data into normal dict

parshed = json.loads(json_str)
print(type(parshed))


