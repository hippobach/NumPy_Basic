import numpy as np

# Integer datatype guessed by NumPy
x = np.array([1, 2])
print("Data Type: ", x.dtype)

# Float datatype guessed by NumPy
x = np.array([1.3, 4.86, 12.9])
print("Data Type: ", x.dtype)

# Forced datatype
x = np.array([1, 2], dtype=np.int64)
print("Forcing a datatype: ", x.dtype)

# Math operations on datatype array
# First Array
arr1 = np.array([[4, 7], [2, 6]],
                dtype=np.float64)

# Second Array
arr2 = np.array([[3, 6], [2, 8]],
                dtype=np.float64)

# Addition of two array
Sum = np.add(arr1, arr2)
print("Addtion of two arrays: ", Sum)

# Addtion of array elements
Sum1 = np.sum(arr1)
print("Addition of array element: ", Sum1)

# Square root of array
Sqrt = np.sqrt(arr1)
print("Square root of array1 elements", Sqrt)

# More on NumPy Data Type: https://www.geeksforgeeks.org/data-type-object-dtype-numpy-python/
