import json
def JSONimport():
    with open("config.json","r") as jsonconfig:
        config=json.load(jsonconfig)
    return config["path"]