from ppadb.client import Client
from art import tprint
import os
senddone = True


tprint("PythonSMS")
print("\nwritten by Dannyx ©2021")
print("[*] ADB server start..")
os.system("D:\\skrypty\\platform-tools\\adb.exe start-server")
while senddone:
    adb = Client(host='localhost', port=5037)
    devices = adb.devices()
    if len(devices) ==0:
        print("[!]  no devices/emulators found")
        senddone = False
    else:
        device = devices[0]
        senddone = False
        print(device.shell("service call isms 7 i32 0 s16 'com.android.mms.service' s16 '+48694643565'  s16 'test_wiadomosci' s16 'null' s16 'null' "))
if senddone == False:
    os.system("D:\\skrypty\\platform-tools\\adb.exe kill-server")
    print("[*] ADB server kill..\nbye")
    