"""
5 - Define a Python function student(). Using function attributes display the names of all arguments.
"""

class Ex5:

    def __init__(self, name, lastname, yearsOld, grade, gender):
        self.name = name
        self.lastname   = lastname
        self.yearsOld   = yearsOld
        self.grade      = grade
        self.gender     = gender

    def objToDict(self):
        pass


if __name__ == '__main__':
    person = Ex5("Mauricio", "Villanueva", 29, 6, 1)
    print(f"Bienvenido {person.name} {person.lastname}.")
    print(person.__dict__)