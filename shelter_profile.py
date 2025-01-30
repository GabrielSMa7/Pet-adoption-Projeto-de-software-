shelters = {
    'Adocão': { 
        'local':'Maceio',
        'email': 'adoteme@org.com',
        'phone': '4949939052',
        'pets': '1234.233.122',
        'us': 'Lorem ipsum etiam sociosqu tincidunt ut gravida, aliquam imperdiet dolor luctus integer purus vivamus, dictumst scelerisque ac elementum nisi. torquent quisque senectus aptent purus urna dictumst scelerisque quis curae, pulvinar eros pharetra dui blandit nam id proin quis commodo, habitant platea vel netus laoreet quam semper platea. velit consequat accumsan augue auctor iaculis aliquet, ac litora massa magna nec netus, mattis volutpat ut euismod adipiscing. nec posuere turpis facilisis primis maecenas himenaeos fermentum cras eleifend, duis tortor ut nulla per rhoncus tellus phasellus mi, senectus mauris ultrices curabitur adipiscing felis justo conubia. ',
        
        },
    'Amigos de pata': {
        'local':'Penedo',
        'email': 'adocao@yahoo.com',
        'phone': '63348842',
        'pets': '1.254',
        'us': 'Lorem ipsum etiam sociosqu tincidunt ut gravida, aliquam imperdiet dolor luctus integer purus vivamus, dictumst scelerisque ac elementum nisi. torquent quisque senectus aptent purus urna dictumst scelerisque quis curae, pulvinar eros pharetra dui blandit nam id proin quis commodo, habitant platea vel netus laoreet quam semper platea. velit consequat accumsan augue auctor iaculis aliquet, ac litora massa magna nec netus, mattis volutpat ut euismod adipiscing. nec posuere turpis facilisis primis maecenas himenaeos fermentum cras eleifend, duis tortor ut nulla per rhoncus tellus phasellus mi, senectus mauris ultrices curabitur adipiscing felis justo conubia. ',
    },
}

def showshelter():
    for shelter, shelter_info in shelters.items():
        print(f"\nShelter Name: {shelter}")
        local = shelter_info['local']
        email = shelter_info['email']
        phone = shelter_info['phone']
        pets = shelter_info['pets']
        us = shelter_info['us']

        print(f"local: {local}")
        print(f"Email: {email}")
        print(f"phone: {phone}")
        print(f"Pets available: {pets}")
        print(f"About us: {us}")
showshelter()