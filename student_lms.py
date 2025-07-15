# Student Details
student_id = 101
student_name = "Ravi"
student_age = 20

# Scores Details
quiz_score = 80
assignment_score = 95
exam_score = 90

# Attendance Details
student_attendance = 95

# using arithmetic operators to calculate
total_score = quiz_score + assignment_score + exam_score # addition operator
average_score = total_score / 3 # division operator

# Using relational operators to determine
# If the student is passing based on average score 75
is_passed = average_score >= 75 


# Attendance 
student_attendance += 1 


#Determine award eligibility
qualified_award = student_attendance >= 90 and is_passed

#Student info display
print("======================")
print(f"Student ID: {student_id}")
print(f"Student Name: {student_name}")
print(f"Student Age: {student_age}")
print(f"Total Score: {total_score}")
print(f"Average Score: {average_score}")

print("===== STUDENT ATTENDANCE REPORT=====")
print(f"Current Attendance: {student_attendance}")

print("======================")
print("===== STUDENT SCORE REPORT=====")
print(f"Student PASSED: {is_passed}")
print(f"Student QUALIFIED FOR AWARD: {qualified_award}")