# today going to learn the csv input and output or txt input or output in numpy
import numpy as np

# print(np.loadtxt("students_score.txt", skiprows=1, delimiter=",", unpack=True))

# print(np.genfromtxt("students_score.txt", skip_header=True, dtype=str))

# array_of_cols = np.genfromtxt(
#     "students_score.txt",
#     skip_header=1,
#     delimiter=",",
#     unpack=True,
#     usecols=[1, 2, 3, 4],
# )

# print(array_of_cols)

# np.savetxt("student_average.txt", np.mean(array_of_cols, axis=0), fmt="%  .2f")
