# Numpy is an important library for data analysis in Python. It provides support for large, multi-dimensional 
# arrays and matrices, along with a collection of mathematical functions to operate on these arrays efficiently.    

import numpy as np

arr1 = np.array([1,2,3,4])
print(arr1)
print(type(arr1))  

# Attributes of numpy arrays:
print("Attributes of numpy array:")
print(arr1.shape) # gives the shape i.e. the number of elements in each dimension of the array
print(arr1.ndim) # gives the number of dimensions of the array
print(arr1.size) # gives the total number of elements in the array
print(arr1.dtype) # gives the data type of the elements in the array
print(arr1.itemsize) # gives the size in bytes of each element in the array
print(arr1.nbytes) # gives the total number of bytes consumed by the array

# some Functions in numpy:
print("Functions in numpy:")
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.shape) # Output: (2, 3)
arr3 = arr2.reshape(3,2)  # change the shape of the array to (3, 2) i.e. 3 rows and 2 columns
print(arr3)

# Vectorized operations in numpy:
print("Vectorized operations in numpy:")
arr1 = np.array([4,3,8,7])
arr2 = np.array([5,8,11,4])
print("Addition : ",arr1 + arr2)
print("Substraction : ",arr1 - arr2)
print("Multiplication : ",arr1*arr2)
print("Division : ",arr2/arr1)

# Universal functions (ufuncs) in numpy:
print("Universal functions (ufuncs) in numpy:")
arr = np.array([1,2,3,4])
print("Square root : ",np.sqrt(arr))
print("Exponential : ",np.exp(arr))
print("Sine : ",np.sin(arr))
print("Cosine : ",np.cos(arr))
print("logarithmic : ",np.log(arr))
print("power : ",np.power(arr,2))

# Indexing,slicing and modification in numpy:
print("Indexing and slicing in numpy:")
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[0])
print(arr[1,2])
print(arr[1:,1:3])
print(arr[1:3,1:2])
arr[1:,1:3] = 99
arr[0:1,0:1] = 100
print(arr)

## stastical functions in numpy:
print("Statistical functions in numpy:")
arr = np.array([1,2,3,4,5])
print("Mean : ",np.mean(arr))
print("Median : ",np.median(arr))
print("Standard Deviation : ",np.std(arr))
print("Variance : ",np.var(arr))
print("Normalized value : ",(arr - np.mean(arr))/np.std(arr)) # Normalization of the array using mean and standard deviation

# Logical operations in numpy:
print("Logical operations in numpy:")
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print("Greater than : ",arr1 > arr2)
print("Less than : ",arr1 < arr2)
print("Equal to : ",arr1 == arr2)
print("Logical AND : ",np.logical_and(arr1 > 2, arr2 > 6))
print("Logical OR : ",np.logical_or(arr1 > 2, arr2 > 6))
print(arr1[(arr1 > 2) & (arr2 > 6)]) # Logical AND using bitwise operator (&) instead of np.logical_and() function