from time import *
import random as r 

def total_mistake(para_test,user_test):
    error = 0 
    for i in range (len(para_test)):
        try:
            if para_test[i] != user_test[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_start,time_end,user_input):
    time_delay = time_end - time_start
    time_r = round(time_delay,2)
    speed = len(user_input)/time_r
    return round(speed)



test = [
    "I love coding.",
    "Python is versatile.",
    "Data science is fun.",
    "AI is the future.",
    "Practice makes perfect."
]

test1 = r.choice(test)
print('****** TYPING TEST ******')
print(test1)
print()
print()
time_start = time()
test_input = input("Enter : ")
time_end = time()

print('Speed : ', speed_time(time_start,time_end,test_input),"w/sec")
print('Error : ', total_mistake(test1,test_input))
