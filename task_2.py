class UserData:
    def __init__(self, name, age):
        self.user_name = name
        self.Age = age

    def print_info(self):
        print(f"User:{self.user_name}, Age:{self.Age}")


def process_data(data_list):
    result = []
    for d in data_list:
        if d.Age > 18:
            result.append(d.user_name.upper())
    return result