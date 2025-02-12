class Shelter:
    def __init__(self, name, local, email, phone, pets, us):
     self.name = name
     self.local = local
     self.email = email
     self.phone = phone
     self.pets = int(pets)
     self.us = us   

    def show_info(self):
        print(f"Name:{self.name}")
        print(f"Local:{self.local}")
        print(f"Email:{self.email}")
        print(f"Phone:{self.phone}")
        print(f"Pets:{self.pets}")
        print(f"Us:{self.us}\n")
shelter1 = Shelter(
        'Adocão',
        'Maceio',
        'adoteme@org.com',
        '4949939052',
        3,
        'O Lar dos Peludos é um abrigo dedicado ao resgate e acolhimento de animais em situação de abandono e maus-tratos. Nosso objetivo é proporcionar um ambiente seguro e acolhedor para cães e gatos que precisam de uma segunda chance.'
    )
shelter2 = Shelter(
        'Amigo de pata',
        'Penedo',
        'adocao@yahoo.com',
        '63348842',
        3,
        'O Abrigo Esperança Animal é um espaço dedicado ao resgate, cuidado e reabilitação de animais abandonados, maltratados ou em situação de risco. Nossa missão é oferecer um lar temporário seguro, repleto de amor e atenção, enquanto trabalhamos para encontrar famílias responsáveis e amorosas para cada um de nossos resgatados.'
    )
shelters = [
    shelter1,
    shelter2
]

for i in shelters:
    print(f"{i.show_info()}")