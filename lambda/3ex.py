califications = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

def run():
    califications.sort( key=lambda item: item[1] )
    print(califications)


if __name__ == "__main__":
    run()