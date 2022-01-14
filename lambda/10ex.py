from functools import reduce

def run():
    fib_series = lambda n: reduce(lambda x, u: x+[x[-1]+x[-2]],range(n-2), [0, 1])
    # n = 3
    # fib_series = list(reduce(lambda x: x+[x[-1]+x[-2]],range(n-2), [0, 1]))
    print("Fibonacci series upto 2:")
    print(fib_series(3))
    # print(fib_series)

if __name__ == '__main__':
    run()