# Short program that Stores data in variables & Compares the data
# Compare the data of two student from a collection of grade submissions.

# Create variables that store the id, average grade, and recent test score for the entries of two students.
id_student_1 = "#10"
average_grade_1 = "A"
test_score_1 = "90"

id_student_2 = "#20"
average_grade_2 = "A"
test_score_2 = "65"

# Compare the data saved from students entry.
# Check for duplicate IDs, compare their average grade, and compare their test scores.
no_duplicates = id_student_1 != id_student_2
print("No duplicate entries:")
print(no_duplicates)

same_average = average_grade_1 == average_grade_2
print("Same average grade:{")
print(same_average)

higher_score = test_score_1 > test_score_2
print(f"Higher score: {test_score_1}")
print(higher_score)