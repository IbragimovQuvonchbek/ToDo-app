import json
from hashlib import blake2b


def get_user_data():
    try:
        with open('users.json') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        with open('users.json', 'w') as f:
            json.dump([], f)
            return []


class User:
    id = -1

    def __init__(self, name, surname, username, phone, password):
        self.name = name
        self.surname = surname
        self.username = username
        self.phone = phone
        self.__password = password

    def is_user_available(self):
        for user in get_user_data():
            if user['username'] == self.username or user['phone'] == self.phone:
                return True
        return False

    def add_new_user(self):
        if not self.is_user_available():
            data = get_user_data()
            self.id = data[-1]['id'] + 1 if data else 1
            new = {
                "id": self.id,
                "username": self.username,
                "name": self.name,
                "surname": self.surname,
                "phone": self.phone,
                "password": blake2b(self.__password.encode('utf-8')).hexdigest(),
            }
            data.append(new)
            with open('users.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("registered successfully")
        else:
            print("username or phone number already exist")
        return self.id
