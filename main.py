import json
import base64
import os.path
from itertools import cycle
from time import sleep

# checks if the code is vaild
def checkCode(currentCash, currentMultiplier, Code, redeemedCodes):
    codes = {
        # Hidden becasue op code is in here for $10000
    }

    Code1 = codes.get('Code1')
    Code2 = codes.get('Code2')
    Code3 = codes.get('Code3')
    DevCode = codes.get('DevCode')

    if Code == Code1 and Code not in redeemedCodes:
        print(f'\n/---------------------------\\\nThe code {Code} has been redeemed Successfully for $100')
        currentCash += 100
        return currentCash, currentMultiplier, Code, True, Code1
    elif Code == Code2 and Code not in redeemedCodes:
        print(f'\n/---------------------------\\\nThe code {Code} has been redeemed Successfully for $200')
        currentCash += 200
        return currentCash, currentMultiplier, Code, True, Code2
    elif Code == Code3 and Code not in redeemedCodes:
        print(f'\n/---------------------------\\\nThe code {Code} has been redeemed Successfully for $300')
        currentCash += 300
        return currentCash, currentMultiplier, Code, True, Code3
    elif Code == DevCode and Code not in redeemedCodes:
        print(f'\n/---------------------------\\\nThe code {Code} has been redeemed Successfully for $10000')
        currentCash += 10000
        return currentCash, currentMultiplier, Code, True, DevCode
    else:
        print('\n/---------------------------\\\nYour code is invalid/Already Redeemed!')
        return currentCash, currentMultiplier, Code, False, None
        

# adds a shop to our game
def shop(currentCash, currentMultiplier, currentCost, currentRebirth, currentRebCost):
    opt = input(f'\n/---------------------------\\\nYou Have ${currentCash}\n\n1. upm to upgrade multiplier\n2. maxupm to Max Upgrade your Multiplier\n3. reb to do a rebirth\n\\---------------------------/\n')
    opt = opt.lower()

    if opt == 'reb':
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

    elif opt == 'upm':
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

    elif opt == 'maxupm':
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

# adds cash
def addCash(currentCash, currentMultiplier, currentRebirth):
    nbs = 1 + currentRebirth
    sum = currentMultiplier * nbs
    currentCash += sum
    return currentCash

cash = 0
multiplier = 1
multiCost = 100
rebirths = 0
rebcost = 10
redeemedCodes = {
    "None": None
}

isFile = os.path.exists('data.json')

if isFile:
    print('\n/---------------------------\\\nSave file found! Loading data...')
    sleep(1)
    with open('data.json', 'r') as file:
        collectedData = file.read()

    encodedData = collectedData
    encodedDataBytes = encodedData.encode('ascii')
    encodedMessageBytes = base64.b64decode(encodedDataBytes)
    decdata = encodedMessageBytes.decode('ascii')

    obj = json.loads(decdata)

    cash = obj['cash']
    multiplier = obj['multiplier']
    multiCost = obj['multiCost']
    rebirths = obj['rebirths']
    rebcost = obj['rebcost']
    redeemedCodes = obj['redeemedCodes']

    print(f'Loaded Save Data:\ncash: {cash}\nmultiplier: {multiplier}\nmultiCost: {multiCost}\nrebirths: {rebirths}\nrebcost: {rebcost}\nRedeemed Codes: {redeemedCodes}\n\\---------------------------/')
    sleep(3)
else:
    pass

print('\n/---------------------------\\\nRelease 1.2.0')

# main game loop
run = True
while run:
    wtd = input('\\---------------------------/\n1. Enter to get cash\n2. shop to enter the shop\n3. code to enter a code\n4. exit to exit\n')
    wtd = wtd.lower()

    if wtd == '':
        cash = addCash(cash, multiplier, rebirths)
        print(f'\n/---------------------------\\\nYou now have ${cash}')

    if wtd == 'shop':
        cash, multiplier, multiCost, rebirths, rebcost = shop(cash, multiplier, multiCost, rebirths, rebcost)

    if wtd == 'code':
        code = input('Enter a code: ')
        cash, multiplier, code, isRedeemed, codeRedeemed = checkCode(cash, multiplier, code, redeemedCodes)

        if isRedeemed:
            redeemedCodes[codeRedeemed] = code


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
