import pyautogui
import time
import clipboard
# Open browser and keybr multiplayer and give the co ordinates of your screen to copy the text so it can type , now run this script just before yout race starts ,it can type at speed of min 2000 wpm.
def write():
      pyautogui.click(77,418)#these co ordinates

      pyautogui.drag(804,548)#are to copy text

      pyautogui.hotkey('ctrl', 'c', interval = 0.15)
      
      text = clipboard.paste()
      
      text = text.replace('␣',' ')

      text = text.replace('↵',' ')
      
      pyautogui.write(text)
time.sleep(2)
write()

# Any doubts, comment
