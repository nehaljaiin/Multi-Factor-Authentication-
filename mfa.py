import random

def generate_code():
    code = str(random.randint(100000, 999999))
    return code

def authenticate(username, password, code):
    if username == "admin" and password == "password" and code == generate_code():
        return True
    else:
        return False

username = input("Enter username: ")
password = input("Enter password: ")
code = input("Enter code: ")

if authenticate(username, password, code):
    print("Authentication successful!")
else:
    print("Authentication failed!")
