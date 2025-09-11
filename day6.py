import numpy as np

# arr = np.array([[3, 2], [4, 2]])

# print(np.sum(arr, axis=0))

# print(np.max(arr))

# print(np.min(arr))

# print(np.prod(arr, axis=1))

# axis -> 0 means column by column

# axis -> 1 means row by row


# print(np.cumprod(arr,axis=1))


# print(np.mean(arr,axis=0))

# print(np.median(arr,axis=1))

# print(np.std(arr, axis=0))


arr = np.array([1,2,32,4,2])


arr_2d_one = np.array([[1,2],[3,4]])
arr_2d_two = np.array([[3,3],[4,4]])

# 1. numpy sum reduction function

# print(np.sum(arr))

# numpy mean

# print(np.mean(arr))

# numpy min
# print(np.min(arr_2d_one))

# print(np.max(arr_2d_one))


# print(np.var(arr))

# print(np.std(arr))

# we know that max will return the actual largest value in the array but what when we want to get the actal index?

# here comes the argmax function in numpy

# print(np.argmax(arr))

# similarly for the minium values you can say argmin so it will give you the minimum value.

# print(np.argmin(arr))


arr_nan = np.array([1,2, np.nan, 4])

print(arr_nan)


print(np.nanmean(arr_nan))