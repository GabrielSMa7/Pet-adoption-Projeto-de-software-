import os

user_name = "Quest"
user_age = "Unknown"
user_adress = "Unknown"
user_email = "Unknown"

def user_profile():
    while True:
        os.system("cls")

        print(f"Name: {user_name}\nAge: {user_age}\nAdress: {user_adress}\nEmail: {user_email}")

        escolha = input("--Criar conta digite (1)\n--Alterar dados da conta (2)\n--Voltar digite (3)\n")

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
            print("Deseja alterar idade? y/n: ")
            control = input()
            if control == "y":
                user_age = input("Digite sua idade: ")
            print("Deseja alterar endereço? y/n: ")
            control = input()
            if control == "y":
                user_adress = input("Type your adress:")
            print("Deseja alterar email? y/n: ")
            control = input()
            if control == "y":
                user_email = input("Type your email: ")
        elif escolha == "3":
            break
        print("\n")
