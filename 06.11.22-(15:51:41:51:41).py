import os
os.system("""time adb shell input swipe 269 1600 525 1700 &
          adb shell input swipe 525 1600 525 1956  &
          adb shell input swipe 525 1856 781 1856 """)
