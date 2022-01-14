"""
9 - Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of 
the said class and print the original and modified values of the said attributes.
"""

class Student:
    def __init__(self, s_name, s_mark):
        self.name = s_name
        self.mark = s_mark


if __name__ == '__main__':
    person1 = Student("Mauro", "Kia")
    print(person1.__dict__)
    person1.name = "Javier"
    print(person1.__dict__)
