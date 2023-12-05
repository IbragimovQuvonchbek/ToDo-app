import json
from hashlib import blake2b

from todo import ToDo, get_todo_data
from user import User, get_user_data


def signup():
    print("============Sign up===============")
    username = input("username: ")
    name = input("name: ")
    surname = input("surname: ")
    phone = input("phone: ")
    password = input("password: ")
    new = User(name, surname, username, phone, password)
    return new.add_new_user()


def login():
    print("=============Log in=============")
    username = input("username: ")
    password = blake2b(input("password: ").encode('utf-8')).hexdigest()

    data = get_user_data()
    for user in data:
        if username == user['username'] and password == user['password']:
            print("log in successfully")
            return user['id']
    print("incorrect username or password")
    return -1


def add_todo(user_id):
    print("==============To Do===========")
    text = input("text: ")
    expires = input("expires at(yyyy-mm-dd): ")
    new = ToDo(text, expires)
    new.add_new_todo(user_id)


def show_todo(user_id):
    data = get_todo_data()
    for todo in data:
        if todo['owner'] == user_id:
            print("===============================================")
            print(f"Id: {todo['id']}")
            print(f"Text: {todo['text']}")
            print(f"Expires at: {todo['expires']}")
            print("===============================================")


def edit_todo(user_id):
    data = get_todo_data()
    show_todo(user_id)
    todo_id = int(input("todo id: "))
    todo_id_is_found = False
    for todo in data:
        if todo['owner'] == user_id and todo['id'] == todo_id:
            todo_id_is_found = True
            text = input("text(press enter to skip): ")
            expires = input("expires at(yyyy-mm-dd)(press enter to skip): ")
            todo['text'] = text if len(text.strip()) != 0 else todo['text']
            todo['expires'] = expires if len(expires.strip()) != 0 else todo['expires']
            break
    with open('todos.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("edited successfully" if todo_id_is_found else "incorrect id")


def delete_todo(user_id):
    data = get_todo_data()
    show_todo(user_id)
    todo_id = int(input("todo id: "))
    todo_id_is_found = False
    for todo in data:
        if todo['owner'] == user_id and todo['id'] == todo_id:
            todo_id_is_found = True
            data.remove(todo)
            break
    with open('todos.json', 'w') as f:
        json.dump(data, f, indent=4)
    print("deleted successfully" if todo_id_is_found else "incorrect id")
