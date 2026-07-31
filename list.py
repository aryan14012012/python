
classmates = ["Aryan","deven","yash","punit","Tushar" ]
print("Class list:", classmates)



print("Total students:" , len(classmates))
print("First student:" , (classmates[0]))
print("Last student:" , (classmates[-1]))
print("First three:" , (classmates[:3]))



classmates.append("Meera")
print("\nAfter adding Meera:", classmates)

classmates.remove("deven")
print("After removing devev", classmates)

classmates.sort()
print("Sorted alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)


teacher = { "name": "Mr. Sharma", "subject": "python", "experience": 5}
print("\nTeacher profile:",teacher)


print("Subject: ",teacher["subject"])
print("Experience:" , teacher.get("experience", "Not found"))
teacher["Experience"] = 6
teacher["email"] = "sharma@school.com"
teacher.pop("experience")
print("Update teacher profile:", teacher)


roll_number = [1,2,3,4,5]
names = ["Aarav","priya","Rahul","Sneha","Meera"]
student_directory = dict(zip(roll_number, names))
print("/nStudent Directory:", student_directory)
print("Student at roll 3:", student_directory[3])
