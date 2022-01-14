def run():
    original = [2, 4, 6, 9, 11]
    valu = 2

    convert = lambda li, n : list(map(lambda x: x*n, li))

    print(convert(original, valu))


if __name__ == '__main__':
    run()