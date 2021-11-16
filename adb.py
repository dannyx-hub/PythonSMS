from ppadb.client import Client
from art import tprint

tprint("PythonSMS")
print("\n written by Dannyx ©2021")
adb = Client(host='localhost', port=5037)


devices = adb.devices()
if len(devices) ==0:
    print("nie znaleziono zadnych urzadzen")
else:
    device = devices[0]

