import numpy as np

a = np.array([1, 2, 5, 3])

# Add 1 to every element
print("Adding 1 to every element:", a + 1)

# Subtract 3 from each element
print("Subtracting 3 from each element:", a - 3)

# multiply each element by 10
print("Multiplying each element by 10:", a * 10)

# square each element
print("Squaring each element:", a ** 2)

# Modify existing array
a *= 2
print("Doubled each element of original array:", a)

# Transpose (hoán vị) of array
a = np.array([[1, 2, 3], [3, 4, 5], [9, 6, 0]])
print("\nOriginal array:\n", a)
print("Transpose of array:\n", a.T)

# Unary operators
arr = np.array([[1, 5, 6],
                [4, 7, 2],
                [3, 1, 9]])
# Maximum element of array
print("Largest element is: ", arr.max())
print("Shortest element is: ", arr.min())
# các phần tử lớn nhất theo mỗi hàng
print("Row-wise maximum elements:", arr.max(axis=1))
# các phần tử nhỏ nhất theo mỗi cột
print("Column-wise minimum elements:", arr.min(axis=0))

# Sum of array elements
print("Sum of all array elements:", arr.sum())

# Cumulative sum along each row (tổng tích lũy dọc theo mỗi hàng)
print("Cumulative sum along each row:\n", arr.cumsum(axis=1))

# Binary operators
b1_arr = np.array([[1, 2],
                   [3, 4]])
b2_arr = np.array([[4, 3],
                   [2, 1]])

# Add arrays
print("Array sum:\n", b1_arr + b2_arr)

# Multiple arrays
print("Array multiplication:\n", b1_arr * b2_arr)

# Matrix multiplication
print("Matrix multiplication:\n", b1_arr.dot(b2_arr))

# Sorting arrays
s_arr = np.array([[1, 4, 2],
                  [3, 4, 6],
                  [0, -1, 5]])
# Sorted array
print("Array elements in sorted order:\n", np.sort(s_arr, axis=None))

# Sorted array row-wise
print("Row-wise sorted array:\n", np.sort(s_arr, axis=1))

# Specify sort algorithm
print("Column wise sort by applying merge-sort:\n", np.sort(a, axis=0, kind='mergesort'))

# Example to show sorting of structured array
# set alias names for dtypes
dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)]

# Values to be put in array
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),
          ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)]

# Creating array
dtype_arr = np.array(values, dtype=dtypes)
print("\nArray sorted by names:\n",
      np.sort(dtype_arr, order='name'))

print("Array sorted by graduation year and then cgpa:\n",
      np.sort(dtype_arr, order=['grad_year', 'cgpa']))
