from ppadb.client import Client
from art import tprint
from config import JSONimport
import os
import getopt
import sys

def main(tel_number,msg):
    path = JSONimport()
    os.system(path)
    senddone = True
    while senddone:
        adb = Client(host='localhost', port=5037)
        devices = adb.devices()
        if len(devices) ==0:
            return "[!]  no devices/emulators found"
            senddone = False
        else:
            device = devices[0]
            senddone = False
            try:
                device.shell(f"service call isms 7 i32 0 s16 'com.android.mms.service' s16 '{tel_number}'  s16 'null' s16 '{msg}' s16 'null' ")
                return "[*] message send!"
            except Exception as e:
                return f"[!] {e}"

    if senddone == False:
        os.system("D:\\skrypty\\platform-tools\\adb.exe kill-server")
        return"[*] ADB server kill..\nbye"
