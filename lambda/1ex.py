import random as rm

def run():
    # for i in range(1,16):
    #     print(i)

    lc = [rm.randrange(1,16) for x in range(1,16)]
    print(lc)

    mult = lambda x,y:x*y

    print(mult(8,2))
    



if __name__ == "__main__":
    run()