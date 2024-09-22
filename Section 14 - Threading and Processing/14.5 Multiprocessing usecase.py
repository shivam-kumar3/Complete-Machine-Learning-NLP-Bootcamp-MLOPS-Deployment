'''
Real World example : Multiprocessing for cpu bound tasks 
scenario : Factorial Calculation
Factorial Calculation, Especially for large numbers, 
involve significant computational work, Multiprocessing can be used to distributes the workload across multiple CPU cores, improving performance
'''

import multiprocessing
import math
import sys
import time

# increase the maximum number of digits for integer conversion 

sys.set_int_max_str_digits(1000000)

# funtion to compute factorial of a given number

def computer_factorial(number):
    print(f'Computing factorial of {number}')
    result = math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result 


if __name__ == '__main__':
    number = [5000,6000,8000,9000]
    t = time.time()

    # create pool of worker process
    with multiprocessing.Pool() as pool:
        result = pool.map(computer_factorial,number)

    final_time = time.time() - t
    print(f'Total time taken: {final_time:.2f} seconds')
