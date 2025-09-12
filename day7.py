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


# Test for beginners

# 1. Read & Print

# Load the file (skip header) using np.genfromtxt.

# Print all the data.

# print(np.genfromtxt("data.txt", skip_header=True, delimiter=",", dtype=str))


# 2. Separate Columns

# Load only the Math scores (use usecols).

# Print the Math column.

# math_scores = np.genfromtxt("data.txt", delimiter=",", skip_header=True, usecols=[1])
# print(math_scores)


# 3. Save & Reload

# Save the Math column into math_scores.txt.

# Reload it and print to check.
# np.savetxt("math_scores.txt", math_scores, fmt="% .2f")

# print(f"Maths scores are : {np.loadtxt("math_scores.txt")}")


# 4. Row Average

# Compute average score per student.

# Save into student_avg.txt.

# data = np.loadtxt("data.txt", skiprows=1, usecols=[1, 2, 3, 4], delimiter=",")

# np.savetxt("student_avg.txt", np.mean(data, axis=1), fmt="% .2f")


# 5. Column Average

# Compute average score per subject.

# Save into subject_avg.txt.
