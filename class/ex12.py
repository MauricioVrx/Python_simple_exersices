"""
13 - Write a Python class named Student with two instances student1, student2 and assign given values to the said instances attributes. Print all the attributes 
of student1, student2 instances with their values in the given format.
"""

class Student:

    def __init__(self, s_id, s_name, s_lastname ):
        self.s_id   = s_id
        self.s_name = s_name
        self.s_lastname = s_lastname
        self.__crazyVar = "potato"


    def displayStudentInfo(self):
        instance = self.__dict__.copy()
        for com in self.__dict__:
            if com.startswith('_'):
                del instance[com]
        return instance
    
    def dispayAll(self):
        return self.__dict__
        

if __name__ == '__main__':
    print("\n")
    
    listStudents = []
    student1 = Student(1, "Mauricio", "Villanueva")
    student2 = Student(2, "Javier", "Rivera")

    listStudents.append(student1)
    listStudents.append(student2)

    print(student1.dispayAll())
    print(student1.displayStudentInfo())
    print(student1.dispayAll())

    print("\n")

    for std in listStudents:
        print(f"{std.s_id} - {std.s_name} {std.s_lastname}")