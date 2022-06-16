# imports lol
import os.path
import base64
import json
from time import sleep

# finds if the file is in the path
class checkData():
    def __init__(self):
        pass

    def checkFile(self, currentCash, currentMultiplier, currentCost, currentRebith, currentRebCost, reedeemedCodes):
        isFile = os.path.exists('./data.json')

        if isFile:
            print('\n/---------------------------\\\nSave file found! Loading data...')
            sleep(1)
            with open('C:/Users/catsw/Documents/CC/data.json', 'r') as file:
                collectedData = file.read()

            encodedData = collectedData
            encodedDataBytes = encodedData.encode('ascii')
            encodedMessageBytes = base64.b64decode(encodedDataBytes)
            decdata = encodedMessageBytes.decode('ascii')

            obj = json.loads(decdata)

            currentCash = obj['cash']
            currentMultiplier = obj['multiplier']
            currentCost = obj['multiCost']
            currentRebith = obj['rebirths']
            currentRebCost = obj['rebcost']
            reedeemedCodes = obj['redeemedCodes']

            print(f'Loaded Save Data:\ncash: {currentCash}\nmultiplier: {currentMultiplier}\nmultiCost: {currentCost}\nrebirths: {currentRebith}\nrebcost: {currentRebCost}\nRedeemed Codes: {reedeemedCodes}\n\\---------------------------/')
            sleep(3)

            return currentCash, currentMultiplier, currentCost, currentRebith, currentRebCost, reedeemedCodes
        else:
            return currentCash, currentMultiplier, currentCost, currentRebith, currentRebCost, reedeemedCodes