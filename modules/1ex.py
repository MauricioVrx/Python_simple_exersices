import random

def run():
    #OPTION 1
    rangeExa1= ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    strg = '#'
    for i in range(0,6):
        strg += random.choice(rangeExa1)
    print(strg)


    #OPTION 2
    rangeExa2= "0123456789ABCDEF"
    strg2 = '#'+''.join(random.choice(rangeExa2) for _ in range(0,6))
    print(strg2)

    rndm = random.choice([ x for x in range(0,71) if x % 7 == 0 ])

    print(rndm)


if __name__ == '__main__':
    run()