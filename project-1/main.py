import numpy as np

raw_csv = np.genfromtxt(
    "./students_score.csv", delimiter=",", dtype=str, usecols=[1, 2, 3, 4]
)

subjects_csv = raw_csv[0]
marks_csv = np.genfromtxt(
    "./students_score.csv", delimiter=",", skip_header=True, usecols=[1, 2, 3, 4]
)
names_csv = np.genfromtxt(
    "./students_score.csv", delimiter=",", skip_header=True, usecols=[0], dtype=str
)
# print(names_csv)
# print(marks_csv)

mask = (marks_csv > 0) & (marks_csv < 100)
filteredMarks = marks_csv[mask].reshape(15, 4)
# print(filteredMarks)


# print(f"Total Marks of {names_csv[1]} is {np.sum(marks_csv[1])}")
# print(f"Total Marks of {names_csv[2]} is {np.sum(marks_csv[2])}")
# print(f"Total Marks of {names_csv[3]} is {np.sum(marks_csv[3])}")

# print(raw_csv)
# print(f"Scores in {subjects_csv[[0,1,2,3]]} are {filteredMarks[:,[1,2,3]]}")
# save the clean dataset again
# print(f"subjects {subjects_csv}")
# print(f"names are {names_csv}")
# print(f"numbers are {marks_csv}")

rows = np.hstack((names_csv.reshape(15, 1), marks_csv))

row_one = np.genfromtxt("./students_score.csv", delimiter=",", dtype=str)[0]

data_set = np.vstack((row_one, rows))

print(f"data set is : {data_set}")

np.savetxt("clean_dataset.csv", data_set, delimiter=",", fmt="%s")
