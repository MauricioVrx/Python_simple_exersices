# def mult(z):
#     return  lambda x, y: x+y+z


def run():
    z = 3
    mult = lambda x, y: x+y+z
    # n1 = mult(3)
    suma = mult(1,2)
    print(suma)


if __name__== '__main__':
    run()




    # CORRECT
# def mult(z):
#     return  lambda x, y: x+y+z


# def run():
#     n1 = mult(3)
#     suma = n1(1,2)
#     print(suma)
