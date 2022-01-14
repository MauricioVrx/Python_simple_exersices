def run():
    list1 = [1, 2, 3, 5, 7, 8, 9, 10]

    print(f"""
    Original list:
    {list1}
    """)

    even = len(list(filter(lambda x : x%2 == 0, list1)))
    odd  = len(list(filter(lambda x : x%2 != 0, list1)))

    print(f"Number of even numbers in the above array: {even}")
    print(f"Number of odd  numbers in the above array: {odd}")



# CONTINUAR

if __name__ == '__main__':
    run()