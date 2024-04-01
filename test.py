import numpy as np

# NumPy Array Creation
# Creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 8]], dtype='float')
print("Array created using passed list:\n", a)

# Creating array from tuple
b = np.array((1, 2, 3))
print("\nArray created using passed tuple:\n", b)

# Creating a 3X4 array with all zeros
c = np.zeros((3, 4))
print("An array  initialized with all zeros:\n", c)

# Create an array with random values
d = np.random.random((2, 2))
print("A random array:\n", d)

# Create a sequence of integers
e = np.arange(0, 30, 5)
print("A sequential array with steps of 5:\n", e)

# Create a sequence of 10 values in range 0 to 5
f = np.linspace(0, 5, 10)
print("A sequential array with 10 values between" "0 and 5:\n", f)

# Reshape 3X4 array to 4X3 array
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])
newArr = arr.reshape(4, 3)
print("Original array:\n", arr)
print("-----------")
print("Reshaped array:\n", newArr)

# Flatten array - (làm phẳng mảng)
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
flatArr = arr1.flatten()

print("Original array:\n", arr1)
print("Flattened array:\n", flatArr)
