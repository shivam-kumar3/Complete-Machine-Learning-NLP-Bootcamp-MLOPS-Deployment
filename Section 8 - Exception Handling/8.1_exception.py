try:
    num = int(input("Enter a number :"))
    result = 10/num
    print(result)
except ZeroDivisionError:
    print("The number cannot be divided with 0")
except Exception as ex:
    print(ex)
finally:
    print("Execution complete")



try:
    with open('new.txt','r') as f:
        data = f.read()
        print(data)
except FileNotFoundError:
    print("the given file is not available try to create one by using w command")
finally:
    print("The exception has been handled ")

# exception try, except block


try:
    a = b
except:
    print("The variable has not been assigned")



try:
    b = c
except Exception as ex:
    print(ex)

# try, except, else block

try:
    num = int(input("Enter a number "))
    result = 10/num
except Exception as ex:
    print(ex)
else:
    print(f'The result is {result}')