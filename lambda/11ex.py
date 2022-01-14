def run():
    l1 = [1, 2, 3, 5, 7, 8, 9, 10]
    l2 = [1, 2, 4, 8, 9]

    # res = [x for x in l1 if (x in l1 and x in l2)]

    cosa = lambda li1, li2 : list(filter(lambda x: x in li1,li2))
    cosa2 = list(filter(lambda x: x in l1, l2))

    l3 = [10, 20, 30, 40, 50] 
    l4 = [50, 75, 30, 20, 40, 69] 

    print(cosa(l1,l2))
    print(cosa(l3,l4))
    print(cosa2)

if __name__== '__main__':
    run()
