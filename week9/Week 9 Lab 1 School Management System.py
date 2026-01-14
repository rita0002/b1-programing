# School Management System - Alternative Implementation

class Person:
    """Generic person class"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

class Student(Person):
    """Student inherits from Person"""
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"I'm {self.name}, student ID {self.student_id}, aged {self.age}."

class Teacher(Person):
    """Teacher inherits from Person"""
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"Hello, {self.name} here. I teach {self.subject} and am {self.age} years old."

# Test instances
student = Student("Alice", 16, "S001")
teacher = Teacher("Mr. Smith", 35, "Mathematics")

print("=== SCHOOL MANAGEMENT SYSTEM ===")
print(student.introduce())
print(teacher.introduce())
print(f"Student age: {student.age}")
print(f"Teacher subject: {teacher.subject}")
