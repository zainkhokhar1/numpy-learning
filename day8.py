import numpy as np

arr_one = np.array([1, 2, 3])
arr_two = np.array([2, 3, 2])

# dot product / matrix multiplication
# print(np.dot(arr_one, arr_two))

# print(arr_one @ arr_two)

# determinant

arr_twod = np.array([[1, 2], [3, 2]])

# print(np.linalg.det(arr_twod))

# inverse of a matrix
# print(np.linalg.inv(arr_twod))

# eigen_values, eigen_vectors = np.linalg.eig(arr_twod)
# print(f"Eigen Values : {eigen_vectors}")

# print(np.transpose(arr_twod))
# in_arr2d = np.linalg.inv(arr_twod)

# to verify we know that A-1 * A = I

# print(arr_twod @ in_arr2d)

print(np.linalg.matrix_rank(arr_twod))

# np.linalg.solve() It takes in the form of AX = B and results is given for the unknown X vector
