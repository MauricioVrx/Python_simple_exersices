"""
2 - Write a Python program to create a class and display the namespace of the said class.
3 - Write a Python program to create an instance of a specified class and display the namespace of the said instance.
"""

class myClass:

    def __init__(self, n1=1, n2=2):
        self.__n1=n1
        self.__n2=n2

    def geN1(self):
        return self.__n1

    def geN2(self):
        return self.__n2

    def mul2n(self):
        return self.__n1+self.__n2


if __name__ == "__main__":
    for n in myClass.__dict__:
        print(n)

    ins1 = myClass(5, 3)
    print(ins1.mul2n())
    print(ins1.__dict__)