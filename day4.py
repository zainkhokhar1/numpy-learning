import numpy

# so unsigned bits cannot take negative values in it
# arr_unsigned = numpy.array([1,2,5,10] , dtype= numpy.uint8)

# print(arr_unsigned)

arr_nm = numpy.arange(1,11.1)
# print(arr_nm)
# print(arr_nm.dtype)

arr_nm_bool = numpy.array([True,False,True,True])

# print(arr_nm_bool.dtype)

arr_int = arr_nm.astype(numpy.int32)

# print(arr_int.dtype)

view = arr_nm.view()

# print(arr_nm)
# print(view)

# view[0] = 99

# print(arr_nm)
# print(view)



# from the above we can see that both the view and the actual data has changed because under the lay both of them were a single data (view points to the original array)

# print(view.base is arr_nm)

# now we are going to create a copy

copy = arr_nm.copy()

print(arr_nm)
print(copy)

copy[0] = 99



print(arr_nm)
print(copy)

# print(copy.base is None)


# print(arr_nm.base is None)

print(arr_int.dtype)

print(arr_int.strides)

