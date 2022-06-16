from random import randint

class petShop():
    def __init__(self):

        self.basicEgg = {
            "Cat": {
                "Name": "Cat",
                "Multiplier": 2,
                "Rarity": 100,
            },
            "Dog": {
                "Name": "Dog",
                "Multiplier": 3,
                "Rarity": 50,
            },
            "Bunny": {
                "Name": "Bunny",
                "Multiplier": 4,
                "Rarity": 25,
            },
            "Noob": {
                "Name": "Noob",
                "Multiplier": 5,
                "Rarity": 12,
            },
        }

        self.eggs = {
            "basic egg": {
                "Name": "Basic Egg",
                "Cost": 500,
            },
        }
    
    def buyEgg(self, cash, petInv, ePets):
        run = True
        while run:
            wtd = input('1. to buy an egg💵\n2. to see all the eggs🥚\n3. to see your Inventory💼\n4. equip a pet🐕\n5. unequip a pet❌\n6. Any Key to Exit🚪\n')
            wtd = wtd.lower()

            # if the user selects '1'
            if wtd == '1':
                randomRarity = randint(1, 100)
                print('/---------------------------\\')
                opt = input('Which egg do you wanna buy? (TIP: Press 2 in the shop to see all the pets): ')
                opt = opt.lower()

                if opt in self.eggs:
                    eyon = input(f'The egg {self.eggs[opt]["Name"]} costs ${self.eggs[opt]["Cost"]}. Y/n: ')
                    eyon = eyon.lower()

                    if eyon == 'y':
                        if opt == "basic egg":
                            if cash >= self.eggs[opt]["Cost"]:
                                cash -= self.eggs[opt]["Cost"]
                                if randomRarity <= self.basicEgg["Dog"]["Rarity"]:
                                    if "Dog" in petInv:
                                        print('You got the Uncommon DOG, but you already had this in your inventory so here\'s a refund!')
                                        print('\\---------------------------/')
                                        
                                    else:
                                        print('You got the Uncommon DOG!')
                                        print('\\---------------------------/')
                                        petInv["Dog"] = self.basicEgg["Dog"]
                                        
                                
                                elif randomRarity <= self.basicEgg["Cat"]["Rarity"]:
                                    if "Cat" in petInv:
                                        print('You got the Common CAT, but you already had this in your inventory so here\'s a refund!')
                                        print('\\---------------------------/')
                                        
                                    else:
                                        print('You got the Common CAT!')
                                        print('\\---------------------------/')
                                        petInv["Cat"] = self.basicEgg["Cat"]
                    
            # if the user selects '2'
            elif wtd == '2':
                print('/---------------------------\\')
                i = 0
                for egg in self.eggs:
                    i += 1
                    print(f'{i}. {self.eggs[egg]["Name"]}: ${self.eggs[egg]["Cost"]}\n')
                print('\\---------------------------/')
                i = 0
                
            # if the user selects '3'
            elif wtd == '3':
                print('/---------------------------\\')
                for pet in petInv:
                    print(petInv[pet]['Name'])
                print('\\---------------------------/')
                
            # if the user selects '4'
            elif wtd == '4':
                print('/---------------------------\\')
                for pet in petInv:
                    print(petInv[pet]['Name'])
                print('-----------------------------')
                pel = True
                while pel:
                    wpte = input('Which pet do you want to equip? (TIP: type 1 to exit this loop): ')
                    if ePets.items() <= 3:
                        if wpte == '1':
                            pel = False
                        elif wpte in petInv:
                            ePets[wpte] = petInv[wpte]
                            petInv.pop(wpte)
                            print(f'The pet {wpte} Has been equiped!')
                            pel = False
                        else:
                            pel = True
                    else:
                        print('You can only equip 3 pets!')

                print('\\---------------------------/')
                

            # if the user selects '5'
            elif wtd == '5':
                print('/---------------------------\\')
                for pet in ePets:
                    print(pet)
                print('-----------------------------')
                puel = True
                while puel:
                    wptue = input('What pet do you want to unequip? (TIP: type 1 to exit this loop): ')
                    
                    if wptue == '1':
                        puel = False
                    elif wptue in ePets:
                        petInv[wptue] = ePets[wptue]
                        ePets.pop(wptue)
                        print(f'The pet {wptue} has been unequiped!')
                        puel = False
                    else:
                        puel = True
                print('\\---------------------------/')
            else:
                return cash, ePets, petInv
            