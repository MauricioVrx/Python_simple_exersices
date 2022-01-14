"""
10 - Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and their 
values of the said class. Now remove the student_name attribute and display the entire attribute with values.
"""

class Student:

    def __init__(self, s_id, s_name):
        self.s_id = s_id
        self.s_name = s_name
        

if __name__ == '__main__':
    person1 = Student(1, "Mauriciano")
    person1.s_class = 6

    print(person1.__dict__)

    person1.__delattr__("s_name")

    print(person1.__dict__)
