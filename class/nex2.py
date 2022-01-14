"""
2 - Write a Python class to convert a roman numeral to an integer.
"""

class Num:
    def __init__(self, n):
        self.n = n

    def romanNumber(self):
        total = 0
        
        coso = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        for value, key in coso.items():
            strLen = len(key)
            while key == self.n[:strLen:]:
                total += value
                self.n =self.n[strLen::]

        return total
            

if __name__ == '__main__':
    naturalN =  Num(str(input("Ingrese número romano: ")))
    print(naturalN.romanNumber())







