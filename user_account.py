user_name = "Não cadastrado"
user_age = "Não cadastrado"
user_adress = "Não cadastrado"
user_email = "Não cadastrado"

while True:

    print("\n")

    print(f"Nome: {user_name}\nIdade: {user_age}\nEndereço: {user_adress}\nEmail: {user_email}")

    escolha = input("para criar uma conta digite 1 e para alterar digite 2 e para fechar digite 3: ")

    if escolha == "1":
        user_name = input("Digite seu nome: ")
        user_age = input("Digite sua idade: ")
        user_adress = input("Digite seu endereço: ")
        user_email = input("Digite seu email: ")
    elif escolha == "2":
        print("Deseja alterar nome? y/n: ")
        control = input()
        if control == "y":
            user_name = input("Digite seu nome: ")
        print("Deseja alterar idade? y/n: ")
        control = input()
        if control == "y":
            user_age = input("Digite sua idade: ")
        print("Deseja alterar endereço? y/n: ")
        control = input()
        if control == "y":
            user_adress = input("Digite seu endereço: ")
        print("Deseja alterar email? y/n: ")
        control = input()
        if control == "y":
            user_email = input("Digite seu email: ")
    elif escolha == "3":
        break
    print("\n")
