import json 

def run():
    x = {
        "name": "John",
        "age": 30,
        "city": "New York"
    }

    y = json.dumps(x)

    print(y)

if __name__ == '__main__':
    run()