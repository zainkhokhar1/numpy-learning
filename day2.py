import numpy as np


# indexing array in numpy

# 1D Array

# arr_num = np.array([1,2,3,4,5])


# print(arr_num[1])
# print(arr_num[4])

# 2D Array

# arr2D = np.array([[1, 2, 10], [3, 4, 11], [5, 6, 12]])

# print(arr2D.shape)

# print(arr2D.itemsize)

# print(arr2D.ndim)

# because index is starting from zero so 2X2 means the 3X3 of normal matrix in maths.

# print(arr2D[2, 2])


# Multidimention array 3D or more...

# arr3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# print(arr3D.ndim)

# print(arr3D[0, 0, 0])

# print(arr3D[0:1,0:1,0:2])

# arr = np.array([10, 20, 30, 40, 50])


# syntax is -> [start, stop, step]

# print(arr[5:0:-3])

# print(arr[:4])

# print(arr[:-1])


# arr_numbers = np.arange(1, 11)

# applying boolean indexing

# which means only odd numbers

# mask = arr_numbers % 2 == 0

# print(arr_numbers[mask])

# or directly use the condition

# print(arr_numbers[arr_numbers % 2 == 0])


# fancy indexing

# arr = np.array([100, 20, 430, 5502, 50])

# print(arr[[0, 2, 4]])

# So in fancy indexing we are going to pass an array of indexing rather then a condition.


# let's try on a 2D array
# arr2D = np.array([[10, 20, 30], [20, 30, 10]])

# print(arr2D[[0, 1]].shape)


# views and copy

num_arr = np.arange(1,11)

view = num_arr[:5]
print(view)

view[2] = 10

print(num_arr)


