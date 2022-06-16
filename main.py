import json
import base64
from time import sleep
from objects.codes import checkCodes
from objects.shop import shop
from objects.checkData import checkData
from objects.pets import petShop

# adds cash
def addCash(currentCash, currentMultiplier, currentRebirth, equippedPets=None):
    petMulti = 0
    for k in equippedPets:
        petMulti += equippedPets[k]['Multiplier']
    nbs = 1 + currentRebirth
    sum = currentMultiplier * nbs * petMulti
    currentCash += sum
    return currentCash

cash = 9999
multiplier = 1
multiCost = 100
rebirths = 0
rebcost = 10
redeemedCodes = {
    "None": None
}
petInv = {

}
ePets = {

}

# Objects
c = checkCodes()
s = shop()
cd = checkData()
ps = petShop()


cash, multiplier, multiCost, rebirths, rebcost, redeemedCodes = cd.checkFile(cash, multiplier, multiCost, rebirths, rebcost, redeemedCodes)
print('\n/---------------------------\\\nRelease 1.3.0')

# main game loop
run = True
while run:
    wtd = input('\\---------------------------/\n1. Enter to get cash\n2. shop to enter the shop\n4. code to enter a code\n5. Pet To by a pet\n6. exit to exit\n')
    wtd = wtd.lower()

    if wtd == '':
        if ePets == {}:
            cash = addCash(cash, multiplier, rebirths, {})
        else:
            cash = addCash(cash, multiplier, rebirths, ePets)
        print(f'\n/---------------------------\\\nYou now have ${cash}')

    if wtd == 'shop':
        s.getOpt(cash)
        cash, multiplier, multiCost, rebirths, rebcost = s.Handler(cash, multiplier, multiCost, rebirths, rebcost)

    if wtd == 'code':
        code = input('Enter a code: ')
        cash, multiplier, code, isRedeemed, codeRedeemed = c.checkCodes(cash, multiplier, code, redeemedCodes)

        if isRedeemed:
            redeemedCodes[codeRedeemed] = code
    
    if wtd == "pet" or wtd == '5':
        cash, ePets, petInv = ps.buyEgg(cash, petInv, ePets)

    if wtd == 'exit':
        yon = input('\n/---------------------------\\\nWould you like to save before exiting? Y/n: ')
        yon = yon.lower()

        if yon == 'y':
            f = open("data.json","w")

            data = {
                "cash": cash,
                "multiplier": multiplier,
                "multiCost": multiCost,
                "rebirths": rebirths,
                "rebcost": rebcost,
                "redeemedCodes": redeemedCodes
            }

            jsonData = json.dumps(data, indent = 4)

            message = jsonData
            message_bytes = message.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            encdata = base64_bytes.decode('ascii')

            with open('data.json', 'w') as file:
                file.write(encdata)

            print('Saved!')
            sleep(1)
            run = False
        else:
            run = False

quit()