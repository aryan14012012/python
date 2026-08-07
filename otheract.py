class Student:
    
    
    school = "ABC School"
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    
    def display(self):
        print("Name  :", self.name)
        print("Age   :", self.age)
        print("School:", Student.school)
        print()
        
student1 = Student("Aryan", 14)
student2 = Student("Riya", 15)

student1.display()
student2.display()