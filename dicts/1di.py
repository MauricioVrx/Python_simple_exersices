import operator 
from functools import reduce
from collections import Counter


# Write a Python script to sort (ascending and descending) a dictionary by value. 
def ex1(di1, bool):
    print(sorted(di1.items(), key=operator.itemgetter(0), reverse=bool))


# Write a Python script to add a key to a dictionary.
def ex2(di1):
    di1.update({2:30})
    print(di1)


# Write a Python script to concatenate following dictionaries to create a new one.
def ex3(di1,di2,di3):
    print(di1 | di2 | di3)


# Write a Python script to check whether a given key already exists in a dictionary. 
def ex4(di1, v):
    print(v in di1.values()) # without .values for keys


# Write a Python program to iterate over dictionaries using for loops.
def ex5(di1):
    for key, value in di1.items():
        print(f"Key : {key}  - Value : {value}")


# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
def ex6(n):
    print({ x : x*x for x in range(1, n+1)}) 


# Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
def ex7():
    print({x: x**2 for x in range(1,15+1)})


# Write a Python script to merge two Python dictionaries.
def ex8(di1, di2):
    cdi1 = di1.copy()
    cdi1.update(di2)
    print(cdi1)


# Write a Python program to iterate over dictionaries using for loops.
def ex9(di1):
    for key, value in di1.items():
        print(f"{key} - {di1[key]}") # print(f"{key} - {value}")


# Write a Python program to sum all the items in a dictionary.
def ex10(di1):
    coso = (sum(di1.values()))  # reduce(lambda x,y: x+y, di1.values())
    print(coso)


# Write a Python program to multiply all the items in a dictionary.
def ex11(di1):
    coso = reduce(lambda x,y : x*y, di1.values())
    print(coso)

# Write a Python program to remove a key from a dictionary.
def ex12(di1):
    cdi1 = di1.copy()
    del cdi1[2]
    print(cdi1)


# Write a Python program to map two lists into a dictionary.
def ex13(di1,di2):
    coso = dict(map(lambda x, y : di1[x] * di2[x], di1.items() , di2.items() ))
    print(coso)


# Write a Python program to sort a given dictionary by key. 
def ex14(li1, li2):
    print(dict(zip(li1,li2)))
    coso = map()


# Write a Python program to get the maximum and minimum value in a dictionary. 
def ex15(di1):
    key_min = min(di1.keys(), key=(lambda k: di1[k]))
    key_max = max(di1.keys(), key=(lambda k: di1[k]))
    print(f"Min : {di1[key_min]} || Max : {di1[key_max]}") # print(f"Min - {min(di1.values())} ||  Máx - {max(di1.values())}")


# Write a Python program to get a dictionary from an object's fields.
class Ex16():
    def __init__(self):
        self.n1 = 1
        self.n2 = 2
        self.n3 = 3
def ex16():
    x16=Ex16()
    print(x16.__dict__)

# Write a Python program to remove duplicates from Dictionary.
def ex17(di1):
    empdic = {}
    for idx, val in di1.items():
        if not val in empdic.values():
            empdic[idx] = val
    print(empdic)


# Write a Python program to remove duplicates from Dictionary.
def ex18(dic):
    print("Con datos" if len(dic)>0 else "Vacío") # print("Vacío" if not bool(dic) else "Con datos")


# Combine two dictionary adding values for common keys
def ex19(di1, di2): # print(Counter(di1) + Counter(di2))
    diCopy = di2.copy()
    di3 = {}
    for idx, val in di1.items():
        if bool(di2.get(idx)):
            di3[idx] = val + di2.get(idx)
            del diCopy[idx]
        else:
            di3[idx] = val
    di3 = di3 | diCopy 
    print(di3)
    


def make_division_by(n):
    def division(x):
        return x/n
    return division

def run():
    # ex1({"red": 0, "blue":1, "green":2}, False)
    # ex2({0: 10, 1: 20})
    # ex3({1:10, 2:20},{3:30, 4:40},{5:50,6:60})
    # ex4({1:10, 2:20},1)
    # ex5({1:10, 2:20,3:30, 4:40,5:50,6:60})
    # ex6(5)
    # ex7()
    # ex8({1:1,2:2,3:3},{1:4,5:5})
    # ex9({1: 4, 2: 2, 3: 3, 5: 5})
    # ex10({1: 100, 2: -54, 3: 247})
    # ex11({1: 2, 2: 8, 3: 5})
    # ex12({1: 2, 2: 8, 3: 5})
    # ex13({1: 2, 2: 8, 3: 5},{1: 3, 2: 2, 3: 5})
    # ex14(['red', 'green', 'blue'], ['#FF0000','#008000', '#0000FF'])
    # ex15({'x':500, 'y':5874, 'z': 560})
    # ex16()
    # ex17({'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20})
    # ex18({'A': 20, 'B': 15, 'C': 20, 'D': 10, 'E': 20})
    ex19({'a': 100, 'b': 200, 'c':300}, {'a': 300, 'b': 200, 'd':400} )
    
    coso3 = make_division_by(3)
    print(coso3(18))
    coso5 = make_division_by(5)
    print(coso5(100))
    coso18 = make_division_by(18)
    print(coso18(54))

if __name__ == '__main__':
    run()