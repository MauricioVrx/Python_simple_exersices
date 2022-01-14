nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def run():
    square = list(map(lambda x: x**2 , nums))
    print(square)
    cube = list(map(lambda x: x**3, nums))
    print(cube)

if __name__ == '__main__':
    run()