# arguments

def num(*args):
    for i in args:
        print(i)

num(1,2,3,4,5,6)


# keywords araguments

def print_details(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}:{values}")


print_details(name="shivam",age=39, country = "India")




def print_details2(*args,**kwargs):
    for val in args:
        print(f"Positional arguments : {val}")
    for key,values in kwargs.items():
        print(f"{key}:{values}")


print_details2(1,2,3,4,5,6,name='shivam',age=34,country = "India")


# return statement

def multiply(a,b):
    return a*b

