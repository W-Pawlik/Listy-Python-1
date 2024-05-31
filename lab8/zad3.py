
login_data = {
    "admin": "admin",
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5"
}

def check_access(login, password):
    if login in login_data and login_data[login] == password:
        if login == "admin" and password == "admin":
            print("Dostep do panelu admina")
        else:
            print("Dostep do strony uzytkownika")
    else:
        print("Nieprawidlowy login lub haslo")

print("Test1:")
check_access("admin", "admin")  

print("Test2:")
check_access("user1", "password1")  

