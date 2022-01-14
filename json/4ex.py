import json


def run():
    dict1 = {"name":"Mauro", "age":29}
    dict2 = {"name":"Katha", "age":30}

    dictD = {
        1 : dict1,
        2 : dict2
    }

    # cj = json.dumps(dictD)

    print(json.dumps(dictD, sort_keys=True, indent=4))

if __name__ == '__main__':
    run()