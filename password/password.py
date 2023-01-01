from cryptography.fernet import Fernet

master_pwd  = input("What is the master password? ")

def add():
    lid = input("Login ID: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(lid + "|" + pwd + "\n")

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, passw = data.split("|")
            print("Login ID: ", name, "\nPassword: ", passw, "\n")


while True:
    option = input("Would you like to add or view password(Or press Q to quit)? ").lower()
    
    if option == 'add':
        add()

    elif option == "view":
        view()
    
    elif option == "q":
        quit()

    else:
        print("Please enter a valid option")

