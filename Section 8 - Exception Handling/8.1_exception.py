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