import os,subprocess
print(os.popen('adb devices').read().split()[-2])

