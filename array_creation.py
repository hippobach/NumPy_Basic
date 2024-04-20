# Array creation using list
arr = [1, 2, 3, 4, 5, 6]

for i in arr:
  print(i)

# Array creation using array function
import array
arr1 = array.array('i',[1, 2, 3])

print('The new created array:', end="")
for i in range(0, 3):
  print(arr1[i], end=" ")
print('\r')

# Array creation using numpy methods
import numpy as np

# empty() function
a = np.empty(2, dtype = int)
print("Matrix a:",a)

b = np.empty([2, 2], dtype = int)
print("Matrix b:",b)

c = np.empty([3,3])
print("Matrix c:",c)

# zeros() function
d = np.zeros(2, dtype = int)
print("Matrix b : \n", d)
 
e = np.zeros([2, 2], dtype = int)
print("\nMatrix a : \n", e)
 
f = np.zeros([3, 3])
print("\nMatrix c : \n", f)

# reshape() function
g = np.arange(8)
print("Original array: ", g)

g = np.arange(8).reshape(2, 4)
print("New array: ", g)

g = np.arange(8).reshape(4, 2)
print("New array: ", g)