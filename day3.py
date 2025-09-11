import numpy
import time

# list_num = [1, 32, 30, 20, 40]

# start_time = time.time()

# for n in list_num:
#     print(n**2)

# print(f"Time taken by python is: {time.time()-start_time}")

# # now using numpy vectorization
# start_time_num = time.time()
# print(numpy.array(list_num) ** 2)
# print(f"Time taken by python is: {time.time()-start_time_num}")


####################  Scalar and array operations in numpy ######

# print(list_num)

# num_list = numpy.array(list_num)
# num_list_new = numpy.array([10, 40, 20, 12, 30])

# print(num_list-1)

# print(num_list*num_list_new)

# a = numpy.array([[1, 3], [4, 3]])

# print(a.shape)

# b = numpy.array([10, 40])

# print(b.shape)

# print(a+b)


#####  Test #####

# a = numpy.array([5, 10, 15, 20])

# print(a + 3)
# print(a * 2)
# print(a**2)


### GPA calculate
# scores = [50, 70, 90, 100]

# # GPA = score/ 20

# gpa = []

# for score in scores:
#     gpa.append(score / 20)

# print(gpa)

# # now using nump
# gpa_num = numpy.array(scores) / 20
# print(gpa_num)


one_million = 1_000_000

py_start_time = time.time()

py_arr = list(range(one_million))


cube_arr = []

# python code to convert them
for number in py_arr:
    cube_arr.append(number**3)

print(f"Python consumed time is: {time.time() - py_start_time}")

num_start_time = time.time()
num_arr = numpy.arange(one_million)

num_cube_arr = num_arr**3

print(f"Numpy consumed time is: {time.time() - num_start_time}")
