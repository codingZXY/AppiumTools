# -*- coding: utf-8 -*-

import oappium
import threading
import time
from appium import webdriver
from copy import deepcopy

def test(*args):
    time.sleep(10)

class AppiumTest(oappium.MultiAppium):
    def __init__(self):
        super().__init__()
        self.target = test
        self.desired_caps = {
            "platformName": "Android",
            "deviceName": '',
            "appPackage": "com.wuba",
            "appActivity": ".activity.launch.LaunchActivity",
            "noReset": True,
            'unicodeKeyboard': True,
            'newCommandTimeout': 86400,
            "udid": '',
        }

    def get_task_threads(self):
        get_driver_threads = []
        for device in self.devices:
            deviceName = device['deviceName']
            serial = device['serial']
            port = device['port']
            caps = deepcopy(self.desired_caps)

            caps['deviceName'] = deviceName
            caps['udid'] = serial

            t = threading.Thread(target=self.get_driver,args=(serial,deviceName,port,self.target,caps))
            t.start()
            get_driver_threads.append(t)

        for t in get_driver_threads:
            t.join()

    def get_driver(self,serial,deviceName,port,target,desired_caps,try_time=3):
        for i in range(try_time):
            try:
                driver = webdriver.Remote(f'http://localhost:{port}/wd/hub', desired_caps)
                t = threading.Thread(target=target, args=(deviceName, serial, port, driver, desired_caps))
                self.task_threads.append(t)

                return
            except Exception as e:
                print(f'Driver Start Failed:{e} Retring:{i+1}')

        print(f'Get Driver Failed:{deviceName} {serial}')

if __name__ == '__main__':
    auto_obj = AppiumTest()
    auto_obj.run()