import os
from pet_adoption_plataform import pet_profile
from pet_adoption_plataform import user_account
from pet_adoption_plataform import search

shelters = {
    'Adocão': { 
        'local':'Maceio',
        'email': 'adoteme@org.com',
        'phone': '4949939052',
        'pets': '3',
        'us': 'Lorem ipsum etiam sociosqu tincidunt ut gravida, aliquam imperdiet dolor luctus integer purus vivamus, dictumst scelerisque ac elementum nisi. torquent quisque senectus aptent purus urna dictumst scelerisque quis curae, pulvinar eros pharetra dui blandit nam id proin quis commodo, habitant platea vel netus laoreet quam semper platea. velit consequat accumsan augue auctor iaculis aliquet, ac litora massa magna nec netus, mattis volutpat ut euismod adipiscing. nec posuere turpis facilisis primis maecenas himenaeos fermentum cras eleifend, duis tortor ut nulla per rhoncus tellus phasellus mi, senectus mauris ultrices curabitur adipiscing felis justo conubia. ',
        
        },
    'Amigos de pata': {
        'local':'Penedo',
        'email': 'adocao@yahoo.com',
        'phone': '63348842',
        'pets': '3',
        'us': 'Lorem ipsum etiam sociosqu tincidunt ut gravida, aliquam imperdiet dolor luctus integer purus vivamus, dictumst scelerisque ac elementum nisi. torquent quisque senectus aptent purus urna dictumst scelerisque quis curae, pulvinar eros pharetra dui blandit nam id proin quis commodo, habitant platea vel netus laoreet quam semper platea. velit consequat accumsan augue auctor iaculis aliquet, ac litora massa magna nec netus, mattis volutpat ut euismod adipiscing. nec posuere turpis facilisis primis maecenas himenaeos fermentum cras eleifend, duis tortor ut nulla per rhoncus tellus phasellus mi, senectus mauris ultrices curabitur adipiscing felis justo conubia. ',
    },
}

def showshelter():
    while True:
        
        os.system("cls")

        for shelter in shelters.keys():
            print(f"Name: {shelter}")

        print("See more about the shelters? y/n")
        choice = input()

        if choice == "y":
            print("Enter the name of the shelter you want to see: ")
            shelter_choiced = input()
            shelter_choiced = shelter_choiced.lower().capitalize()
            shelter_info = shelters.get(shelter_choiced)
            
            if not shelter_info:
                continue
            
            while True:
                print(f"\nShelter Name: {shelter_choiced}")
                local = shelter_info['local']
                email = shelter_info['email']
                phone = shelter_info['phone']
                pets = shelter_info['pets']
                us = shelter_info['us']

                print(f"Local: {local}")
                print(f"Email: {email}")
                print(f"Phone: {phone}")
                print(f"Pets: {pets}")
                print(f"About us: {us}")

                print("--See our availabels pets? (1)\n--Send a donation for this shelter? (2)\n--Return (3)")
                
                choice = input()

                os.system("cls")

                if choice == "2":
                    if user_account.user_age == "Unknown":
                        print("You need have a account to do a donation")   
                    elif user_account.user_age > 18:
                        print("Send your tip")
                        donation = float(input())
                        print(f"Thanks {user_account.user_name}Our pets from {shelter_choiced} are pleased for your contribution of {donation:.2f}$")
                    else:
                        print("You need be a adult to do a donation")
                    input("\nPress any key to return")
                    continue

                elif choice == "1":
                    pets_availables = search.filtr(pet_profile.pets, "shelter", shelter_choiced)

                    for pet in pets_availables.keys():
                        print(f"Name: {pet}")

                    input("\nPress any key to return")
                    continue
                elif choice == "3":
                    break
        elif choice == "n":
            break