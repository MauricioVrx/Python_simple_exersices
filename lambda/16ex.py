from functools import reduce

def run():
    childrens = [['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 2.0], ['G GHOSH', 1.0]]

    ordenedList = sorted(childrens, key=lambda elem: int(elem[1]))

    lowGrade = ordenedList[0][1]

    for i in ordenedList:
        if  i[1] > lowGrade:
            lowGrade = i[1]
            secondLowerList = sorted([x[0] for x in ordenedList if x[1] == i[1]], key = lambda elem: elem[0])
            break
        else: 
            secondLowerList = childrens

    print("Second lower grade: " + str(lowGrade)) 
    for children in secondLowerList:
        print(children)


if __name__ == '__main__':
    run()