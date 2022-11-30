import os
print(os.popen('adb shell content query --uri content://contacts/phones/  --projection name:number').read().split("name").split("number"))
