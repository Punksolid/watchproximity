from bluepy.btle import Scanner, DefaultDelegate
from subprocess import call
import time

print ("Scanner")
scanner = Scanner()

tries = 0;
while True:
    devices = scanner.scan(2);
    found = False
    for device in devices:
        if device.addr == "c0:41:1a:9d:46:9a":
            found = True
    if found == True:
        print("encontrado "+ str(device.rssi))
    else:
        tries = tries+1
        if tries == 4:
            call(["loginctl", "lock-session"])
    time.sleep(5)
