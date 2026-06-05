# Memory Management
# 1. automatic garbage collection
# 2. reference counting
# 3. internal optimization

# Reference Counting - method python use to manage memory

import sys
a=[]
print(sys.getrefcount(a))

## Garbage collection -> includes a circular garbage collector to handle reference cycle
import gc
gc.enable()
gc.collect
gc.disable()

print(gc.get_stats())
print(gc.garbage)

## Best Practices
# 1. Use Local Variables - Shorter lifespan than global
# 2. Avoid Circular Reference -  Lead to memory leaks
# 3. Use Generators - produce itams one at a time
# 4. Explicitly delete objects
# 5. Profile Memory Usage

import gc 
class MyObj:
    def __init__(self,name):
        self.name = name
        print(f"Object {self.name} created.")
    
    def __del__(self):
        print(f"Object {self.name} delete.")
        
obj1 = MyObj("obj1")
obj2 = MyObj("obj2")
# circular referencing
obj1.ref = obj2
obj2.ref = obj1
del obj1
del obj2

print(gc.garbage)
gc.collect()


## Generators for Memory management
import gc
def gen_nums(n):
    for i in range(n):
        yield i

for num in gen_nums(100000):
    print(num)
    if(num > 20):
        break

## profiling Memory usage with tracemalloc
import tracemalloc
def create_list():
    return [i for i in range(10000)]

def main():
    tracemalloc.start()
    data=create_list()
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')
    
    print("[Top 10]")
    for stat in top_stats[::]:
        print(stat)
    
main()