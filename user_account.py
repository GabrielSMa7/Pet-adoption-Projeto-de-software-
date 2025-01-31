import os

user_name = "Quest"
user_age = "Unknown"
user_adress = "Unknown"
user_email = "Unknown"

def user_profile():
    while True:
        global user_name
        global user_age
        global user_adress
        global user_email
        os.system("cls")

        print(f"Name: {user_name}\nAge: {user_age}\nAdress: {user_adress}\nEmail: {user_email}")

        escolha = input("--Creat account (1)\n--Change account (2)\n--Exit (3)\n")

        if escolha == "1":
            user_name = input("Type your name: ")
            user_age = input("Type your age: ")
            user_adress = input("Type your adress: ")
            user_email = input("Type your email: ")
        elif escolha == "2":
            print("Change your name? y/n: ")
            control = input()
            if control == "y":
                user_name = input("Type your name: ")
            print("Change your age? y/n: ")
            control = input()
            if control == "y":
                user_age = input("Digite sua idade: ")
            print("Change adress? y/n: ")
            control = input()
            if control == "y":
                user_adress = input("Type your adress:")
            print("Change email? y/n: ")
            control = input()
            if control == "y":
                user_email = input("Type your email: ")
        elif escolha == "3":
            break
        print("\n")
