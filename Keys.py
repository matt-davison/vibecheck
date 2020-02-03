import json

def getKey(service, target): 
    with open("keys.json") as infile:
        data = json.load(infile)
        item = data.get(service).get(target)
        if item is None:
            print("Target(s) for %s are missing. Please add entries to keys.json"%service)
        return(item)

def missingKeys(services):
    with open("keys.json") as infile:
        data = json.load(infile)
        for service in services:
            if data.get(service) is None or None in data.get(service).values():
                return False
        return True