"""
7 - Write a simple Python class named Student and display its type. Also, display the __dict__ attribute keys and the value of the __module__ attribute of the Student class.
"""

class student:
    def __init__(self, s_id, s_name, s_class):
        self.s_id    = s_id
        self.s_name  = s_name
        self.s_class = s_class

if __name__ == '__main__':
    person1 = student(1, "Mauro", 3)
    print(type(person1))

    print(person1.__dict__.values()) #Keys()
    print(person1.__module__)
   