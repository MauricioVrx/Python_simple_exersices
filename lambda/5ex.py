nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def run():
    par = list(filter(lambda x : x % 2 == 0, nums))
    inpar = list(filter(lambda x : x % 2 != 0, nums))
    print(par)
    print(inpar)

if __name__ == '__main__':
    run()