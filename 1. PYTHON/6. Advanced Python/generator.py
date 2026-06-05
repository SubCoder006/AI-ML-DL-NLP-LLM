### This is a simple implementation of an iterator in Python i.e. a generator.

# A generator is a special type of iterator that allows you to create an iterator 
# in a more concise way using a function.

# A generator function is defined using the def keyword and contains one or more 
# yield statements. When the generator function is called, it returns a generator
# object that can be iterated over.  

# case 1: A simple generator function that yields a sequence of numbers:
def simple_generator():
    yield 1
    yield 2
    yield 3

gen = simple_generator()
print(type(gen))  # Output: <class 'generator'>
for value in gen:
    print(value,end=' ')
    
print()  # Just to add a newline after the previous output

# case 2: A generator function that generates an infinite sequence of numbers:
def infinite_generator():
    num = 0
    while True:
        yield num
        num += 1
        if(num > 20):
            break
        
gen = infinite_generator()
for value in gen:
    print(value,end=' ')
    
print()  # Just to add a newline after the previous output

# case 3: A generator function that generates Fibonacci numbers:
def fibb_nums():
    num1 = 0
    num2 = 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2
        if(num1 > 100):
            break
        
gen = fibb_nums()
for value in gen:
    print(value,end=' ')
    
print()  # Just to add a newline after the previous output

### Generators real world use case: Reading large files line by line without loading the entire file into memory.
def read_large_file(file_path):
    with open(file_path,'r') as file:
        for line in file:
            yield line.strip() # Yield each line of the file, without loading the entire file memory at once i.e. memory efficient way to read large files.
            
rd = read_large_file('large_file.txt')
for line in rd:
    print(line)