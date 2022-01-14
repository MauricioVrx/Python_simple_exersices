phone = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

def run():
    print(phone)

    phone.sort(key = lambda i : i["color"])

    print(phone)

if __name__ == "__main__":
    run()