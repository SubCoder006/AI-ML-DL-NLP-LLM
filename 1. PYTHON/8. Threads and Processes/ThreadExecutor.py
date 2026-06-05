from concurrent.futures import ThreadPoolExecutor as tpe
import time
from unittest import result

def p_nums(num):
    time.sleep(1)
    return f"Number : {num}"
nums=[1,2,3,4,5,6]
with tpe(max_workers=3) as executor:
    results = executor.map(p_nums,nums)
    
for result in results:
    print(result)
    
    