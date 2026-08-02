# My School Subject Planner

# Store fixed student details in a tuple
student_details = ("Asha", 15, "Class 9")

# Access tuple values
student_name = student_details[0]
student_age = student_details[1]
student_class = student_details[2]

# Create subject sets for different days
monday_subjects = {"Math", "Science", "English"}
tuesday_subjects = {"History", "Geography", "Art"}

# Modify sets
monday_subjects.add("Computer")
monday_subjects.remove("English")

# Compare subjects using common set operations
common_subjects = monday_subjects & tuesday_subjects
union_subjects = monday_subjects | tuesday_subjects
difference_subjects = monday_subjects - tuesday_subjects
symmetric_difference = monday_subjects ^ tuesday_subjects

# Display results
print("My School Subject Planner")
print("-" * 30)
print("Student Name:", student_name)
print("Student Age:", student_age)
print("Student Class:", student_class)
print("Monday Subjects:", monday_subjects)
print("Tuesday Subjects:", tuesday_subjects)
print("Common Subjects:", common_subjects)
print("All Subjects:", union_subjects)
print("Monday Only:", difference_subjects)
print("Unique Subjects:", symmetric_difference)
 