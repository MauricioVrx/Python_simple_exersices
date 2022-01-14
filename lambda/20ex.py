def fun(ea, leng):
    numInList = list(map(lambda x : int(x) if x.isdigit() else "", ea))
    return sorted([ele for ele in numInList if type(ele) == type(2) and  ele > leng], reverse=True)

def run():
    strn = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
    ea = list(strn.split(" "))
    leng = len(ea) 
    valuue = fun(ea, leng)

    print(valuue)


if __name__ == '__main__':
    run()