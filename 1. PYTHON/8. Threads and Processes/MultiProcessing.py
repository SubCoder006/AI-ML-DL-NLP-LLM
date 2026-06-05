## a real world usecase example

import multiprocessing as mpc
import time
import sys
import math
from unittest import result

sys.set_int_max_str_digits(100000)

def Factorial(num):
    print(f'Computing factorial of {num}')
    result = math.factorial(num)
    print(f'Factorial of {num} is {result}')
    return result

if __name__=="__main__":
    numbs=[9,29,79,169]
    start = time.time()
    
    with mpc.Pool() as pool:
        results = pool.map(Factorial,numbs)
    
    end = time.time()
    print(f'Results : {result}')
    print(f'Time Taken : {end-start} seconds')