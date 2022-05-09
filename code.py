#asks for the user too create a username
username = input("please create a username: ")

#asks for the user to create a password that has too be over 5 characters, repeatedly asks if this
#requirment is not met
while True:
    try:
        pass_creation = input("please create a password: ")
        password = pass_creation
        if len(password) > 5:
            break
        else:
            print("weak password, use more than 5 characters")
    except ValueError:
        print("")

#UI for login page
print("_" * 15)
print("  LOGIN PAGE")
print("_" * 15)

# asks user for their username and password, if incorrect the program promts the user to re enter till correct, program then continues
while True:
    try:
        username_check = input("please input your username: ")
        if username_check == username:
            break
        else:
            print("incorrect username try again: ")
    except ValueError:
        print("")


while True:
    try:
        password_check = input("please input your password: ")
        if password_check == password:
            break
        elif password_check != password:
            print("incorrect password try again: ")
    except ValueError:
        print("")


#now logged into whatever program desired
print("you are now logged in, welcome too......")
