# very profesinal code btw
# ^^ can't spell btw

class checkCodes():

    # init the class
    def __init__(self):
        self.codes = {
            "Code1": "Release",
            "Code2": "Update1",
            "Code3": "Update2",
            "Code4": "Update3",
            "DevCode": "d3Vc0D3",
        }

    # check if the code is vaild
    def checkCodes(self, currentCash, currentMultiplier, code, redeemedCodes):
        # Geting the codes
        self.Code1 = self.codes.get('Code1')
        self.Code2 = self.codes.get('Code2')
        self.Code3 = self.codes.get('Code3')
        self.Code4 = self.codes.get('Code4')
        self.DevCode = self.codes.get('DevCode')

        # Code 1
        if code == self.Code1 and code not in redeemedCodes:
            print(f'\n/---------------------------\\\nThe code {code} has been redeemed Successfully for $100')
            currentCash += 100
            return currentCash, currentMultiplier, code, True, self.Code1
        
        # Code 2
        elif code == self.Code2 and code not in redeemedCodes:
            print(f'\n/---------------------------\\\nThe code {code} has been redeemed Successfully for $200')
            currentCash += 200
            return currentCash, currentMultiplier, code, True, self.Code2
        
        # Code 3
        elif code == self.Code3 and code not in redeemedCodes:
            print(f'\n/---------------------------\\\nThe code {code} has been redeemed Successfully for $300')
            currentCash += 300
            return currentCash, currentMultiplier, code, True, self.Code3

        # Code 4
        elif code == self.Code4 and code not in redeemedCodes:
            print(f'\n/---------------------------\\\nThe code {code} has been redeemed Successfully for 1 Multiplier')
            currentMultiplier += 1
            return currentCash, currentMultiplier, code, True, self.Code4
        
        # devcode
        elif code == self.DevCode and code not in redeemedCodes:
            print(f'\n/---------------------------\\\nThe code {code} has been redeemed Successfully for $10000')
            currentCash += 10000
            return currentCash, currentMultiplier, code, True, self.DevCode
        else:
            print('\n/---------------------------\\\nYour code is invalid/Already Redeemed!')
            return currentCash, currentMultiplier, code, False, None