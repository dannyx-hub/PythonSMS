from ppadb.client import Client
from art import tprint
import os
import getopt
import sys
import config
tprint("PythonSMS")
print("\nwritten by Dannyx ©2021")
print("[*] ADB server start..")
config= config.JSONimport()
os.system(config[0])
tel_number = None
msg = None

argv = sys.argv[1:]
try:
    opts,args = getopt.getopt(argv,"n:m:")
except:
    print("error")
for opt,arg in opts:
    if opt in ['-n']:
        tel_number = arg
    elif opt in ["-m"]:
        msg = arg

senddone = True
while senddone:
    if len(config[1]) == 0 or len(config[2]) == 0:
        adb = Client(host='localhost', port=5037)   #when config dosent have added host and port information run on default settings
        print("[!] no host and port information on config.json. Run on default settings")
    else:
            adb = Client(host=config[1], port=int(config[2]))
    devices = adb.devices()
    if len(devices) ==0:
        print("[!]  no devices/emulators found")
        senddone = False
    else:
        device = devices[0]
        senddone = False
        try:
            device.shell(f"service call isms 7 i32 0 s16 'com.android.mms.service' s16 '{tel_number}'  s16 'null' s16 '{msg}' s16 'null' ")
            print("[*] message send!")
        except Exception as e:
            print(f"[!] {e}")

if senddone == False:
    os.system("D:\\skrypty\\platform-tools\\adb.exe kill-server")
    print("[*] ADB server kill..\nbye")
