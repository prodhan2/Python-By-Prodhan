import time 
import pyautogui
count  = 5
print(' T minus')
for i in range(5):
    print(count)
    time.sleep(1)
    count = count - 1
    for i in range (100) :
        pyautogui.typewrite("sumyta i am very sorry ? plz forgave me ")
        pyautogui.press("enter")
        time.sleep(.1)
