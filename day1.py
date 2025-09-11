# import numpy as np
# import time

# first try the python list
# py_list = list(range(1_000_000))

# start_time = time.time()

# py_sum = [x*2 for x in py_list]

# print(f'List taken time {time.time() - start_time}')


# numpy array

# py_list_nd = np.arange(1_000_000)  # similar to python range function
# start_time_1 = time.time()
# np_sum = py_list_nd * 2 
# print(f"Numpy array taken time {time.time() - start_time_1}")


# print(np.linspace(0,100,11))

# print(np.arange(1,10))

#1D array of zeros
# print(np.zeros(3))

# 2D array of zeros
# print(np.zeros((3,3)))

#1D array of one's
# print(np.ones(10))

#2D array of ones
# print(np.ones((2,3)))



# dimentional_two = np.zeros((3,3))

# print(dimentional_two.ndim)

# dimentional_one = np.zeros(10)

# print(dimentional_one.ndim)

# print(dimentional_two.shape)

# It's one dimentional so it's only having rows no columns
# print(dimentional_one.shape)


# print(dimentional_one.dtype)

# print(dimentional_two.dtype)


# it gives rows multiplied by columns
# print(dimentional_two.size)

# print(dimentional_two.itemsize)


#################  DAY 1 PRACTICE TEST ########################

import numpy as np

# py_list = [10,20,30,40]

# converting the python list to numpy array
# num_py_list = np.array(py_list)

# print(num_py_list)
# print(num_py_list.dtype)


# print(np.arange(5,25,5))

# print(np.linspace(0,14,7))


# print(np.ones((3,3)))


arr = np.array([[2, 4, 6], [8, 10, 12]], dtype=np.float32)

print(arr.itemsize)

