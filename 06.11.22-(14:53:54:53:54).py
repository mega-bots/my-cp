import os
from time import sleep
for i in range(10):
  os.system("adb shell input tap 900 1800")
  sleep(0.1)
