import search
import os

pets = {
    'Bethoven': { 
        'age': 7, 
        'gender': 'male',
        'color': 'brown and white',
        'size' : 'big',
        'type' : 'dog'
        },
    'Garfiel': {
        'age': 4, 
        'gender': 'male',
        'color': 'orange',
        'size' : 'medium',
        'type' : 'cat'
    },
    'Snoop': { 
        'age': 2, 
        'gender': 'male',
        'color': 'black and white',
        'size' : 'small',
        'type' : 'dog'
        },
    'Lady': { 
        'age': 2, 
        'gender': 'female',
        'color': 'brown',
        'size' : 'small',
        'type' : 'dog'
        },
    'Scooby': { 
        'age': 10, 
        'gender': 'male',
        'color': 'brown',
        'size' : 'big',
        'type' : 'dog'
        },
    'Marrie': {
        'age': 1, 
        'gender': 'female',
        'color': 'white',
        'size' : 'small',
        'type' : 'cat'
    },
}

print("Aply filters? y/n\n")
choice = input()

while choice == "y":
    
    os.system("cls")

    while True:  
        
        print("What kind of filter?\n--Type\n--Size\n--Gender\n")
        fltrs = input() 

        if fltrs.lower() == "type":
            os.system("cls")
            print("What kind of type?\n--Cat\n--Dog\n")
            spc = input()
            break
        if fltrs.lower() == "size":
            os.system("cls")
            print("What kind of Size?\n--Small\n--Medium\n--Big\n")
            spc = input()
            break
        if fltrs.lower() == "gender":
            os.system("cls")
            print("What kind of gender?\n--Female\n--Male\n")
            spc = input()
            break
        else:
            os.system("cls")
            print("Filter don't found, try again!\n")

    spc = spc.lower()
    fltrs = fltrs.lower()

    pets = search.filtr(pets, fltrs, spc)
    print("Aply another filter? y/n\n")
    choice = input()
        

def showpets():
    for pet, pet_info in pets.items():
        print(f"\nPet Name: {pet}")
        age = pet_info['age']
        color = pet_info['color']
        gender = pet_info['gender']
        size = pet_info['size']
        tpe = pet_info['type']

        print(f"Age: {age}")
        print(f"Color: {color}")
        print(f"Gender: {gender}")
        print(f"Size: {size}")
        print(f"Type: {tpe}")
