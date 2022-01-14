def run():
    list1 = [1,2,3]
    list2 = [4,5,6]

    funList = lambda l1,l2: list(map(lambda x, y: x+y, l1 ,l2))

    print(list1)
    print(list2)
    print(funList(list1, list2))

if __name__ == "__main__":
    run()