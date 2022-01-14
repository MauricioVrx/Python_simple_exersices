"""
11 - Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class. Create a function to 
display the entire attribute and their values in Student class.
"""


class Student:

    def __init__(self, s_id, s_name):
        self.s_name = s_name
        self.s_id   = s_id

    def displayInfo(self):
        return f"{self.s_id} - {self.s_name}, estas bienvenido(a) a esta party hard."

if __name__ == '__main__':
    person1 = Student(1, "Pepe")
    print(person1.displayInfo())

