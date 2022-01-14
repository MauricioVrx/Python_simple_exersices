"""
8 - Write a Python program to crate two empty classes, Student and Marks. Now create some instances and check 
whether they are instances of the said classes or not. Also, check whether the said classes are subclasses 
of the built-in object class or not.
"""

class Person:
    def __init__(self):
        pass

class Student(Person):
    def __init__(self):
        pass

class Mark:
    def __init__(self):
        pass

if __name__ == '__main__':
    person1 = Student()
    thing1  = Mark()
    print(isinstance(person1,Student))  #Object == instance_class
    print(isinstance(Student(),Person)) #Sub-class
    print(issubclass(Student,Person))   #Sub-class