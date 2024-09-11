'''
Python can be used to perform operations on a file (read & write data)

Types of all files

1- text file : .txt,.docx,.log etc
2- Binary files : .mp3, .mov,.png,.jpeg etc

f = open('file_name','mode')

data = f.read()
f.close()

r - open for reading ( default)
w - open for wrtting, truncating the file first ( overwritting)
x - create a new file and open it for writting 
a - open for writting , appending to the end of the file if it exists
b - binary mode
t - text mode (default)
+ - open a disk file for updating (reading  and writing)

w and a - create a file even if it doesnt exist
'''


f = open("demo.txt", 'r+')
# data = f.read()
# print(data)

f.write('abc')
print(f.read())
f.close()

with open('demo.txt', 'r') as f:
    data = f.read()
    print(data)


with open('demo.txt','a') as f:
    f.write("\nthis will be in the new line")


with open('practice.txt', 'w') as f:
    f.write('Hi Everyone\nwe are learning File I/O\nusing Java\nI like programming in java')


with open('practice.txt', 'r') as f:
    data = f.read()
    print(data)

new_data = data.replace('java', "Python")

with open("practice.txt",'w') as f:
    f.write(new_data)
    
with open('practice.txt', 'r') as f:
    data = f.read()
    print(data)

