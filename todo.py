import json


def get_todo_data():
    try:
        with open('todos.json') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        with open('todos.json', 'w') as f:
            json.dump([], f)
            return []


class ToDo:
    id = 1

    def __init__(self, text, expires):
        self.text = text
        self.expires = expires

    def add_new_todo(self, user_id):
        data = get_todo_data()
        self.id = data[-1]['id'] + 1 if data else self.id
        new = {
            "id": self.id,
            "text": self.text,
            "expires": self.expires,
            "owner": user_id,
        }
        data.append(new)
        with open('todos.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("added successfully")
