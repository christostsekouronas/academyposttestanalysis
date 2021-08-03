import json

def readConfig():
    f = open('config.json',)
    return json.load(f)

