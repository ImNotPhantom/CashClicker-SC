
# Shop
class shop():
    def __init__(self):
        pass
    
    def getOpt(self, currentCash):
        self.opt = input(f'\n/---------------------------\\\nYou Have ${currentCash}\n\n1. upm to upgrade multiplier\n2. maxupm to Max Upgrade your Multiplier\n3. reb to do a rebirth\n\\---------------------------/\n')
        self.opt = self.opt.lower()
    
    def Handler(self, currentCash, currentMultiplier, currentCost, currentRebirth, currentRebCost):

        # Rebirth handler
        if self.opt == 'reb':
            robt = input(f'\n/---------------------------\\\nYou Have {currentMultiplier} Multipliers\n\nThis rebirth costs {currentRebCost} Multipliers. Y/n: ')
            robt = robt.lower()

            if robt == 'y':
                if currentMultiplier >= currentRebCost:
                    currentCash -= currentCash
                    currentMultiplier -= (currentMultiplier - 1)
                    currentCost -= (currentCost - 100)
                    currentRebCost += 10
                    currentRebirth += 1
                    print(f'\n/---------------------------\\\nYou now have {currentRebirth} rebirths!')
                    return currentCash, currentMultiplier, currentCost, currentRebirth, currentRebCost
                else:
                    print('\n/---------------------------\\\nYou don\'t have enough for this transaction')
                    return currentCash, currentMultiplier, currentCost, currentRebirth, currentRebCost
            else: return currentCash, currentMultiplier, currentCost, currentRebirth, currentRebCost
        
        # Upgrade handler
        elif self.opt == 'upm':
            opt2 = input(f'\n/---------------------------\\\nYou Have ${currentCash}\n\nThis upgrade costs ${currentCost}. Y/n: ')
            opt2 = opt2.lower()

            if opt2 == 'y':
                if currentCash >= currentCost:
                    currentCash -= currentCost
                    currentMultiplier += 1
                    currentCost += 100
                    print(f'\nYour multiplier is now {currentMultiplier}')
                    return currentCash, currentMultiplier, currentCost, currentRebirth, currentRebCost
                else:
                    print('\n/---------------------------\\\nYou don\'t have enough for this transaction!')
                    return currentCash, currentMultiplier, currentCost, currentRebirth, currentRebCost
            else: return currentCash, currentMultiplier, currentCost, currentRebirth, currentRebCost
        
        # Max Upgrade handeler
        elif self.opt == 'maxupm':
            opt3 = input(f'\n/---------------------------\\\nAre you sure this will buy max Multiplier Upgrades. Y/n: ')
            opt3 = opt3.lower()
            if opt3 == 'y':
                while currentCash >= currentCost:
                    currentCash -= currentCost
                    currentMultiplier += 1
                    currentCost += 100

                print(f'\nYour multiplier is now {currentMultiplier}')
                return currentCash, currentMultiplier, currentCost, currentRebirth, currentRebCost

            else:
                return currentCash, currentMultiplier, currentCost, currentRebirth, currentRebCost

        else: return currentCash, currentMultiplier, currentCost, currentRebirth, currentRebCost