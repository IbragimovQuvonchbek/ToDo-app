from functions import signup, login, add_todo, show_todo, edit_todo, delete_todo

while True:
    print("Exit | Sign up | Log in(0|1|2)")
    option = int(input("option: "))
    current_user = -1
    if option == 0:
        break
    elif option == 1:
        current_user = signup()
    if option == 1 or option == 2:
        current_user = login()

    while current_user != -1:
        print("back | my todo | create todo | edit todo | delete todo(0|1|2|3|4): ")
        option = int(input("option: "))
        if option == 0:
            break
        elif option == 1:
            show_todo(current_user)
        elif option == 2:
            add_todo(current_user)
        elif option == 3:
            edit_todo(current_user)
        elif option == 4:
            delete_todo(current_user)
