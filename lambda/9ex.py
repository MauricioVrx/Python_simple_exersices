

def run():
    isNumber= lambda x :True if type(x) is int else False
    is_num = lambda q: q.replace('.','',1).isdigit()

    # print(isNumber("algo"))
    # print(isNumber(5))

    print(is_num(input("ingrese valor: ")))

if __name__ == '__main__':
    run()