import numpy as np

# raw_csv = np.genfromtxt(
#     "./students_score.csv", delimiter=",", dtype=str, usecols=[1, 2, 3, 4]
# )

# subjects_csv = raw_csv[0]
# marks_csv = np.genfromtxt(
#     "./students_score.csv", delimiter=",", skip_header=True, usecols=[1, 2, 3, 4]
# )
# names_csv = np.genfromtxt(
#     "./students_score.csv", delimiter=",", skip_header=True, usecols=[0], dtype=str
# )
# print(names_csv)
# print(marks_csv)

# mask = (marks_csv > 0) & (marks_csv < 100)
# filteredMarks = marks_csv[mask].reshape(15, 4)
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

# rows = np.hstack((names_csv.reshape(15, 1), marks_csv))

# row_one = np.genfromtxt("./students_score.csv", delimiter=",", dtype=str)[0]

# data_set = np.vstack((row_one, rows))

# print(f"data set is : {data_set}")

# np.savetxt("clean_dataset.csv", data_set, delimiter=",", fmt="%s")

################# Now day 2 #########################


data_csv = np.genfromtxt(
    "./clean_dataset.csv",
    delimiter=",",
    skip_header=True,
    usecols=[1, 2, 3, 4],
)

header_csv = np.genfromtxt(
    "./clean_dataset.csv", delimiter=",", dtype=str, usecols=[1, 2, 3, 4]
)[0]

names_csv = np.genfromtxt(
    "./clean_dataset.csv", delimiter=",", dtype=str, usecols=[0], skip_header=True
)

mean = np.mean(data_csv, axis=0)
median = np.median(data_csv, axis=0)
std = np.std(data_csv, axis=0)

# print(mean)
# print(median)
# print(std)
# print(np.vstack((header_csv, mean.astype(int))))
# print(data_csv)
arrays = np.split(data_csv, 15, axis=0)

# max_of_all_students = np.sum(data_csv, axis=1)
# top_student_marks = np.max(max_of_all_students)

# index_of_max = max_of_all_students.argmax()

# print(index_of_max)
# print(
#     f"Name: {names_csv[index_of_max]}\nTotal marks: {np.sum(data_csv[index_of_max])} of highest score\n"
# )

# for i, n in enumerate(arrays):
#     print(f"Name: {names_csv[i]}\nTotal marks: {np.sum(n)}")

# indexes = np.argsort(np.sum(data_csv, axis=1))[::-1]
# for i in indexes:
#     print(f"Name: {names_csv[i]}\nmarks:{np.sum(data_csv[i])} \n")

# global_minimum = np.min(data_csv)
# global_maximum = np.max(data_csv)

# normalized_scores = (data_csv - global_minimum) / (global_maximum - global_minimum)
# print(normalized_scores)

# I have to calculate the average of all the students subject vise, So Let's go->
avg_per_subj = np.astype(np.average(data_csv, axis=0), int)

# print(names_csv.reshape(15, 1))
# print((avg_per_subj - data_csv))
student_avg_in_subject = data_csv - avg_per_subj

# names_with_average_per_subject = np.hstack(
#     ((names_csv).reshape((15, 1)), student_avg_in_subject)
# )
# original_header_with_name = np.genfromtxt(
#     "./clean_dataset.csv", dtype=str, delimiter=","
# )[0]
# compatible_header = original_header_with_name.reshape(1, 5)
# print(np.vstack((compatible_header, names_with_average_per_subject)))

# mask = student_avg_in_subject > 0
# actual_mask = np.all(mask, axis=1)
# print(actual_mask)
# print(data_csv[actual_mask])
