"""
3 - Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and ']. These brackets must be close in the correct 
order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid. 
"""
class Nex3:

    def __init__(self, strC):
        self.strC = strC

    def checkText(self):
        all     = ""
        closeBy = ""
        current = ""

        open  = ['(' , '[', '{']
        close = [')' , ']', '}']

        for i in self.strC:
            if i in open:
                var = str(open.index(i))
                all += var
                closeBy += var
                current = var
            if i in close:
                var = str(close.index(i))
                all += var 
                if var == current:
                    closeBy = closeBy[:-1]
                    if len(closeBy) > 0: 
                        current = closeBy[-1]
                else:
                    break

        if closeBy == "":
            return True
        else:
            return False
        

if __name__ == '__main__':
    newText = Nex3("((Ho))l[{an(d)a}]")
    print(newText.checkText())
