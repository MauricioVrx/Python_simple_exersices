"""
6 - Write a Python function student_data () which will print the id of a student (student_id). If the user passes an argument student_name or student_class the 
function will print the student name and class
"""

class student:
    def __init__(self, s_id, s_name, s_class):
        self.s_id    = s_id
        self.s_name  = s_name
        self.s_class = s_class

    def student_data(self, text=""):
        if self.s_name == text or self.s_class == text:
            return {"name": self.s_name, "class" : self.s_class}
        else:
            return self.s_id

if __name__ == '__main__':
    person1= student(1,"Mauricio", 6)
    person2= student(2,"Javier", 5)

    print(person1.student_data("Mauricio"))
    print(person2.student_data())
