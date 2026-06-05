import multiprocessing as mlp
import time

def square_nums():
    for i in range(1,6):
        time.sleep(1)
        print(f"Square of {i} : {i*i}")
        
def cube_nums():
    for i in range(1,6):
        time.sleep(1)
        print(f"Cube of {i} : {i*i*i}")
        
# create process
if __name__ == "__main__"  :
    p1 = mlp.Process(target=square_nums)
    p2 = mlp.Process(target=cube_nums)
    
    t = time.time()
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print(f"Finished Time : {time.time() - t}")
