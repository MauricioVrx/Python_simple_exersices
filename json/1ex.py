import json

def run():
    x =  '{ "name":"John", "age":30, "city":"New York"}'

    y = json.loads(x)

    print(f"Name : {y['name']}")
    print(f"Age  : {y['age']}")


if __name__ == '__main__':
    run()