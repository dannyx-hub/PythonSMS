from ppadb.client import Client
from art import tprint
import os
import getopt
import sys
senddone = True


tprint("PythonSMS")
print("\nwritten by Dannyx ©2021")
print("[*] ADB server start..")
os.system("D:\\skrypty\\platform-tools\\adb.exe start-server")
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

while senddone:
    adb = Client(host='localhost', port=5037)
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
    