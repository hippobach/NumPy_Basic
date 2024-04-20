import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)
print(a.shape)

# access the elements of the array

# print the row 1
print(a[0])

# print element at [0][0]
print(a[0][0])

# print the whole column 0
print(a[:, 0])

# print the whole row 0
print(a[0, :])

# transpose the array using T attribute
print(a.T)

# transpose the array using transpose() function
print(a.transpose())

# computes the inverse of a square matrix: linalg (linear algebra), tìm ma trận nghịch đảo của một ma trận vuông 
print(np.linalg.inv(a))
# compute the determinant of a square matrix (tính định thức của một ma trận vuông)
print(np.linalg.det(a))
# Đường chéo chính của ma trận
print(np.diag(a))