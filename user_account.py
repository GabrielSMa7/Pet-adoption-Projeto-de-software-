import os

user_name = "User"
user_age = "Unknown"
user_adress = "Unknown"
user_email = "Unknown"

class User:
    def __init__(self, name, age, address, email):
        self.name = name
        self.age = int(age)
        self.address = address
        self.email = email
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"address: {self.address}")
        print(f"email: {self.email}")

def user_profile():
    user_name = input("name:")
    user_adress = input("address")
    user_age = input("age")
    user_email = input("email")

    user = User(user_name, user_age, user_adress, user_email)

    user.show_info()