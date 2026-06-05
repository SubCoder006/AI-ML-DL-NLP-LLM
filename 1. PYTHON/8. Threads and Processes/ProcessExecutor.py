from concurrent.futures import ProcessPoolExecutor as ppe
import time
from unittest import result

def square(num):
    time.sleep(1)
    return f"Number : {num*num}"
nums=[1,2,3,4,5,6]
if __name__ == "__main__":
    with ppe(max_workers=3) as executor:
        results = executor.map(square,nums)
    
    for result in results:
        print(result)
    
    