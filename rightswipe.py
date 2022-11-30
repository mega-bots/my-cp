import os
import sys


if len(sys.argv) > 1:
    times = int(sys.argv[1])
else:
    times = 10

print("Times to swipe:" + str(times))

for x in range(times):
  print(x+1)
  os.system("adb shell input swipe 100 500 500 500 50")
