# Program - a sequence of instructions written iin programming language
# Process - instance of a program that is being language
# Thread - a unit of execution within a process

## Multithreading
# I/O bound tasks           Concurrent Execution

import threading as thd
import time

def p_nums():
    for i in range(1,6):
        time.sleep(0.5)
        print(i)

def p_letter():
    for i in range(5):
        time.sleep(1)
        print(chr(97+i))

# create threads
t1 = thd.Thread(target=p_nums)
t2 = thd.Thread(target=p_letter)
t=time.time()
# start the thread
t1.start()
t2.start()
# wait for thread tp complete
t1.join()
t2.join()
print(f"Finished Time : {time.time()-t}")
