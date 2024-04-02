import numpy as np

# List
l1 = [1, 2, 3]
l2 = [4, 5, 6]

# Array
a = np.array([1, 2, 3])

# dot product
# #1
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

# #2
a1 = np.array(l1)
a2 = np.array(l2)
dot = np.dot(a1, a2)
print(dot)

# #3
sum1 = a1 * a2
dot = np.sum(sum1)
print(dot)

# #4
dot = a1 @ a2
print(dot)
