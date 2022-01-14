def func(char):
    return lambda x : x[0] == char

def run():

    fun = func("s")
    word = "Esta es una cadena string cualquiera"
    word = word.lower().split(sep=None)
    all = list(map(fun, word))

    print(all)

if __name__== '__main__':
    run()


    # OPTION 2
    # charG = "s"
    # word = "Esta es una cadena string cualquiera"

    # word = word.lower().split(sep=None)
    # all = list(map(lambda x : x[0] == charG, word))

    # print(all) 


    
    
    # func = lambda x : x[0] == char




# def func(char):
#     return lambda x : x[0] == char

# def run():

#     fun = func("s")
#     word = "Esta es una cadena string cualquiera"
#     word = word.lower().split(sep=None)
#     all = list(map(fun, word))
