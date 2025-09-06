student_grades = {
    "Charles": [80, 65, 72,],
    "Bob": [99, 100, 95],
    "Richard": [87, 78, 82],
    "Ricardo": [65, 75, 85],
    "Jone": [99, 100, 95],
    "Kory": [79, 85, 90],
    "Hijab": [20, 30, 10],
    "Jim": [65, 89, 70],
    "Jabriel": [55, 80, 76],
    "Jessica": [76, 81, 59],
    }

student_averages = {}
for student, scores in student_grades.items():
    count = 0 # These variables are reset here so scores can be counted on a per student basis.
    grades_sum = 0
    for score in scores: # This loop searches the list found within the dictonary allowing me to find the average of a student's scores no matter how many students and scores there is.
        count += 1
        grades_sum += score
        grade_average = grades_sum / count
        student_averages[student] = grade_average

student_letter_grades = {}
for student, average in student_averages.items():
    if average < 60: # This conditional is F to A so it could end on an else conditional for more code stability.
        average = "F"
    elif average < 69:
        average = "D"
    elif average < 79:
        average = "C"
    elif average < 89:
        average = "B"
    else:
        average = "A"
    student_letter_grades[student] = average

top_students = {}
for student, average in student_averages.items(): # This loop searches the student_averages dictionary and pulls a student and their corresponding average grade.
    top_student_average = average # The top_student_average could be a number lower than the actual top score without this variable.
    for comparison_average in student_averages.values(): # For every student and average grade pulled, this loop retrieves every average grade (one by one).
        if comparison_average > top_student_average:
            top_student_average = comparison_average
    if average == top_student_average: # This allows multiple students to be placed inside the top_students dictonary incase there is two students with the same score.
        top_students[student] = top_student_average

count = 0 # count is placed outside the loop so it can be continuously added to.
overall_average_sum = 0
for average in student_averages.values():
    count += 1
    overall_average_sum += average
class_average = overall_average_sum / count # This statement is outside the loop so it averages all values.

passing_count = 0 # I used passing_count instead of count so they would not be confused.
for average in student_averages.values():
    if average >= 70:
        passing_count += 1

print("----------------------------------------------------------------------------------------")
print("Class Grades Report:")
print("The top student(s) of this class were...")
print("")
for student, average in top_students.items():
    print(f"{student} with {average}")
print("")
print(f"The class average is {round(class_average, 2)}%")
print(f"with {passing_count} students passing.")
print("----------------------------------------------------------------------------------------")

input("Press ENTER to close report") # This prevents the program from closing when run with python.