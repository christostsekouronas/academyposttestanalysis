import json

def loadConfig():
    f = open('config.json',)
    return json.load(f)

def loadConfigKey(whichKeyToReturn):
    f = open('config.json',)
    keys = json.load(f)
    if whichKeyToReturn in keys:
        return keys[whichKeyToReturn]
    else:
        return None

def isKeyInConfigurations(whichKeyToReturn):
    f = open('config.json',)
    keys = json.load(f)
    if whichKeyToReturn in keys:
        return True
    else:
        return False

