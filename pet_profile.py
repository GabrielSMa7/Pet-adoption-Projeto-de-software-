pets = {
    'Bethoven': { 
        'age': '7', 
        'color': 'Brown and white',
        'size' : 'Big',
        'type' : 'Dog'
        },
    'Garfiel': {
        'age': '4', 
        'color': 'Orange',
        'size' : 'medium',
        'type' : 'Cat'
    },
}
for pet, pet_info in pets.items():
    print(f"\nPet Name: {pet}")
    age = pet_info['age']
    color = pet_info['color']
    size = pet_info['size']
    tpe = pet_info['type']

    print(f"Age: {age}")
    print(f"Color: {color}")
    print(f"Size: {size}")
    print(f"Type: {tpe}")
