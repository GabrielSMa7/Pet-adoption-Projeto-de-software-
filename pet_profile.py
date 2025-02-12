class Pet:
    def __init__(self, name, age, color, tpe, race, shelter):
        self.name = name
        self.age = age
        self.color = color
        self.tpe = tpe
        self.race = race
        self.shelter = shelter

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"age: {self.age}")
        print(f"color: {self.color}")
        print(f"type: {self.tpe}")
        print(f"race: {self.race}")
        print(f"shelter: {self.shelter}\n")

pet1 = Pet('Kevin', 3, 'black', 'dog', 'NRD', 'oo')
pet2 = Pet('Fla', 9, 'gray', 'cat', 'NDR', 'flu')

pets = [pet1, pet2]

def show_pets():
    global pets
    print("Pets:")
    for i in pets:
        print(f"{i.show_info()}")
    