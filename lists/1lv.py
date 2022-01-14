from functools import reduce
import random
import itertools 


#https://www.w3resource.com/python-exercises/list/


#Write a Python program to sum all the items in a list.
def ex1(li1):
    print(reduce(lambda x,y :x+y, li1))

#Write a Python program to multiply all the items in a list.
def ex2(li1):
    print(reduce(lambda x,y: x*y, li1))

#Write a Python program to get the largest number from a list.
def ex3(li1):
    print(sorted(li1, reverse=True)[0])

#Write a Python program to get the smallest number from a list.
def ex4(li1):
    print(sorted(li1, reverse=False)[0])

#Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
def ex5(li1):
    print([x for x in li1 if len(x)>=2 and x[0] == x[-1]])

#Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
def ex6(li1):
    print(sorted(li1, key= lambda x: x[-1]))

# Write a Python program to remove duplicates from a list.
def ex7(li1):
    print(sorted(list(filter(lambda i : li1.count(i) < 2 , li1))))

#Write a Python program to check a list is empty or not.
def ex8(li1):
    print("Empty list" if len(li1) == 0 else "No Empty list")

#Write a Python program to clone or copy a list
def ex9(li1):
    print(li1.copy())

#Write a Python program to find the list of words that are longer than n from a given list of words.
def ex10(li1, n):
    print(list(filter(lambda x: x if len(x) > n else "", li1)))

# Write a Python function that takes two lists and returns True if they have at least one common member. 
def ex11(li1, li2):
    print(True if list(filter(lambda x : x in li2 ,li1)) else False)

#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
def ex12(li1):
    print([y for x, y in enumerate(li1) if not x in [0, 4, 5] ])

#Write a Python program to generate a 3*4*6 3D array whose each element is *
def ex13(n1,n2,n3):
    print([[[z+1 for z in range(n3*(y),n3*(y+1))] for y in range(n2*(x),n2*(x+1))] for x in range(0,n1)])

#Write a Python program to print the numbers of a specified list after removing even numbers from it. 
def ex14(li1):
    print ([x for x in li1 if x %2 != 0 ])

#Write a Python program to shuffle and print a specified list.
def ex15(li1):
    print(random.sample(li1, len(li1)))

#Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
def ex16(n1,n2):
    print([x**2 for x in range(n1,n2+1)][:-6:-1])

#Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
def ex17(n1,n2):
    print([x**2 for x in range(n1, n2+1)][0:5])

#Write a Python program to generate all permutations of a list in Python.
def ex18(n):
    print(list(itertools.permutations([1,2,3])))

#Write a Python program to get the difference between the two lists.
def ex19(li1, li2):
    print(list(set(li1)-set(li2))+list(set(li2)-set(li1)))

#Write a Python program access the index of a list.
def ex20(li1, n):
    print(li1[n])

#Write a Python program to convert a list of characters into a string
def ex21(li1):
    print("".join(li1))

#Write a Python program to find the index of an item in a specified list.
def ex22(li1, n):
    print(li1.index(n))

#Write a Python program to flatten a shallow list.
def ex23(li1):
    print([x for y in[y for z in li1 for y in z] for x in y])

#Write a Python program to append a list to the second list.
def ex24(li1, li2):
    print(li1 + li2)

#Write a Python program to select an item randomly from a list. 
def ex25(li1):
    print(random.choice(li1))

def run():
    # ex1([1,2,-8])
    # ex2([1,-9,4,-9])
    # ex3([1,-9,4,-9])
    # ex4([1,-9,4,-9])
    # ex5(['abc', 'xyz', 'aba', '1221'])
    # ex6([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
    # ex7([1,2,3,5,2,9,7,6,8,3,1,4,3,5,8])
    # ex8([2])
    # ex9([2])
    # ex10(["Pepino", "3DS", "pokemon", "hola"], 5)
    # ex11(["tomate", "3DS", "pokemon", "hola"], ["tomaco", "DS", "pokimon", "hola"])
    # ex12(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'])
    # ex13(3,4,6)
    # ex14([1,2,3,5,2,9,7,6,8,3,1,4,3,5,8])
    # ex15(["0","1","2","3","4","5","6","7","8","9"])
    # ex16(1,30)
    # ex17(1,30)
    # ex18([1,2,3])
    # ex19([1,2,3,4],[5,3,2,1,1])
    # ex20([9,8,7,6,5,4,3,2,1,0],4)
    # ex21(["M","a","u","r","o"])
    # ex22(["M","a","u","r","o"], "o")
    # ex23([[[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]])
    # ex24([1,2,3],[4,5,6])
    ex25(["Red", "Blue", "Black"])

if __name__ == '__main__':
    run()