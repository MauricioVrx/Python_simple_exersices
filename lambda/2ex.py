def multNumber(n):
    return lambda x: x* n


def run():
    vari = multNumber(2)
    print(vari(8))

if __name__ == "__main__":
    run()