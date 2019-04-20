# -*- encoding=utf8 -*-
__author__ = "ethan"

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android import Android
import threading
import time

def connect_one():
    dev = Android('042a60610104')
    dev.wake()

def connect_devices():
    devices = ['042a60610104','19ebdefe9804','3ee07cf','467261200404','c63568b40004','fc84c6b2']
    devs = [Android(d) for d in devices]
    
    return devs
    
def run(dev):
    dev.wake()
    dev.start_app(package='com.wuba',activity='activity.launch.LaunchActivity')
    # poco = AndroidUiautomationPoco(dev)
    time.sleep(10)
    dev.stop_app(package='com.wuba')
    


def main():
    devs = connect_devices()
    for dev in devs:
        t = threading.Thread(target=run,args=(dev,))
        t.start()
        
    

main()





