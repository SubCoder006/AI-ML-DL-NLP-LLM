### This is documentation for iterators in Python.

# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# In Python, an iterator is an object that implements the iterator protocol, which consists of the methods
# __iter__() and __next__().

# The __iter__() method returns the iterator object itself and is used in cases where the object needs to
# be iterated multiple times. The __next__() method returns the next value from the iterator and raises a
# StopIteration exception when there are no more items to return.   

# Example of an iterator in Python:
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Usage of the MyIterator class:
my_list = [1, 2, 3, 4, 5]
it = MyIterator(my_list)
for item in it:
    print(item ,end=' ,')

### Without creating a custom iterator, we can also use built-in iterators in Python, such as lists,
# tuples, and dictionaries.
# For example, we can iterate over a list directly:

my_list = [1, 2, 3, 4, 5]
it = iter(my_list)  # Get an iterator from the list
for item in it:
    print(item,end=' ,')
    
# In this example, we use the built-in iter() function to get an iterator from the list, and then we can iterate over it using a for loop.

my_dict = {'a': 1, 'b': 2, 'c': 3}
it = iter(my_dict)  # Get an iterator from the dictionary
print(type(it))  # Output: <class 'dict_keyiterator'
for key in it:
    print(key,my_dict[key],end=' ,',sep=':')  