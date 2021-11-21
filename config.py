import json
import os, sys
def JSONimport():
    if os.path.isfile("config.json"): 
        with open("config.json","r") as jsonconfig:
            config=json.load(jsonconfig)
            path = config["path"]
            host = config["host"]
            port = config["port"]
            if len(path) == 0:
                print("[*] Please change your config file and rerun this shit")
                sys.exit(1)
            else:
                    return path,host,port
    else:
        print("[*] ERROR: config file isn't exist. We change that and create this shit for you gl")
        with open("config.json", "w") as jsonconfig:
            data = '{"path":"D:\\skrypty\\platform-tools\\adb.exe start-server" }'
            
            json.dump(data,jsonconfig)
    
    
dump = JSONimport()
print(dump[0])