import numpy

# arr = numpy.array([[2, 4, 1], [4, 2, 10], [10, 3, 1], [2, 9, 12]])

# print(arr.shape)


# ravel is used to convert multi-Dimenshion array into
# 1D array.

# print(numpy.ravel(arr))

# print(numpy.transpose(arr))

# .T is also going to give you transpose of the array.

# Transpose means converting the rows to columns and vice versa.

# print(arr.T)

# print(numpy.split(arr,2))


# By reshaping we mean just rotating or changing the rows and columns but not the actual data in it.

# arr_two = numpy.array([[2, 4, 3, 5], [4, 2, 6, 8]])

# print(arr_two.shape)
# print(arr_two.reshape((4, 2), order='C'))

# arr_one_dim = numpy.arange(1,101)

# print(arr_one_dim.reshape(10,10))

# print(arr_one_dim)


# We can convert any multi-D array to a 1D array by using this ravel method.

# print(arr_two.ravel())

# print(arr_two.flatten())


# arr_two = numpy.array([[2, 4, 3, 5], [4, 2, 6, 8]])

# arr_three = numpy.array([[1, 4, 3, 2], [1, 2, 6,3 ]])

# transpose of this array in numpy

# print(arr_two.T)

# print(numpy.hstack((arr_two, arr_three)))


##### Practice test for the vstack, hstack and concatenate.

# Q1. hstack with 1D arrays
# Create two 1D arrays [1,2,3] and [4,5,6].
# Stack them horizontally and print the result.

# Sol =>
# arr_one = numpy.array([1, 2, 3])
# arr_two = numpy.array([4, 5])

# print(numpy.hstack((arr_one, arr_two)))


# Q2. vstack with 1D arrays
# Using the same arrays from Q1, stack them vertically and print the result.

# Sol =>
# print(numpy.vstack((arr_one, arr_two)))


# Q3. hstack with 2D column arrays
# Create:
# a = np.array([[1], [2], [3]])  # shape (3,1)
# b = np.array([[4], [5], [6]])  # shape (3,1)
# Stack them horizontally and print the result.

# Sol =>
# print(numpy.hstack((a, b)))


# Q4. vstack with 2D row arrays
# Create:
# c = np.array([[1, 2, 3]])  # shape (1,3)
# d = np.array([[4, 5, 6]])  # shape (1,3)
# Stack them vertically and print the result.

# Sol =>
# print(numpy.vstack((c, d)))


# Q5. concatenate along axis=0
# Create:
# x = np.array([[1, 2], [3, 4]])
# y = np.array([[5, 6], [7, 8]])
# Concatenate x and y along axis=0 and print the result.
# print(numpy.concatenate((x, y), axis=0))

# Q6. concatenate along axis=1
# Using the same x and y arrays from Q5, concatenate along axis=1 and print.
# print(numpy.concatenate((x, y), axis=1))


# Q7. Trick question – mixing shapes
# Try this:
# p = np.array([1, 2, 3])
# q = np.array([[4, 5, 6]])
# Attempt to concatenate them along axis=0 and axis=1.
# Observe and print what happens (error or result).

# print(numpy.concatenate((p, q), axis=1))


# split function in numpy

# arr = [1, 2, 3, 4]

# num_arr = numpy.array(arr)

# print(num_arr)


# print(numpy.split(num_arr, [1,2,3]))

# in numpy horizontal means columns wise.
# in numpy vertical means rows wise.

# print(numpy.hsplit(num_arr, 4))

# arr_2d = numpy.array([[20, 10], [190, 3], [2, 19]])
# print(arr_2d.shape)
# print(numpy.vsplit(arr_2d, 3))


# arr_num = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# print(numpy.hsplit(arr_num,2))


print(numpy.arange(6))