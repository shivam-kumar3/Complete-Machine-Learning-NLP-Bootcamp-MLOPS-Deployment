'''
We will learn how to do logging in real world scenario

'''


import logging 

# basic logging setting 
logging.basicConfig(
    level = logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('final.log'), #log file name
        logging.StreamHandler()
    ]
    
)

# Making module 
logger = logging.getLogger("Arthematicapp")

def add (a,b):
    result = a+b
    logger.debug(f'Adding {a} +{b} = {result}')
    return result

def subtract (a,b):
    result = a-b
    logger.debug(f'Subtracting {a} - {b} = {result}')
    return result

def multiply (a,b):
    result = a*b
    logger.debug(f'Multiplying {a} * {b} = {result}')
    return result


def divide(a,b):
    try:
        result = a/b
        logger.debug(f'Dividing {a} + {b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None
    
add(10,16)
multiply(22,3)
subtract(32,376)
divide(43,2)