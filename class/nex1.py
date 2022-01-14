"""
1 - Write a Python class to convert an integer to a roman numeral.
"""
class Num:
    def __init__(self, n):
        self.n = n

    def romanNumber(self):
        romanN = ""
        num = self.n
        coso = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        for value, rom in coso.items():
            count = num//value
            if count >= 1:
                num -= count*value
                romanN =romanN+(count*rom)
            if num == 0:
                break

        return romanN
            

if __name__ == '__main__':
    naturalN =  Num(int(input("Ingrese número: ")))
    print(naturalN.romanNumber())



    
    

    