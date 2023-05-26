import numpy as np

# 1) Create a 3x3 matrix with values ranging from 0 to 8

matrix = np.arange(9).reshape(3, 3)

print(matrix)

# 2) Create a 10x10 array with random values and find the minimum and maximum values

array = np.random.rand(10, 10)

minimum_value = np.min(array)
maximum_value = np.max(array)

print("Array:")
print(array)
print("Minimum value:", minimum_value)
print("Maximum value:", maximum_value)

# 3) Replace all odd numbers in the given array with -1

exercise_1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

exercise_1[exercise_1 % 2 != 0] = -1

print(exercise_1)

# 4) Convert a 1-D array into a 2-D array with 3 rows

exercise_2 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

exercise_2_2d = exercise_2.reshape(3, -1)

print(exercise_2_2d)

# 5) Add 202 to all the values in given array

exercise_3 = np.arange(4).reshape(2, -1)

exercise_3 += 202

print(exercise_3)

# 6) Extract the first four columns of this 2-D array

exercise_6 = np.arange(100).reshape(5, -1)

columns = exercise_6[:, :4]

print(columns)
