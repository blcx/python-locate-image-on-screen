import pyautogui
import time
import keyboard
import random
import win32api, win32con
import mouse

# takes screen shot of certain region
im1 = pyautogui.screenshot(region=(534,430,828,231,))
im1.save("screenshot.png")


#mouse cursor
pyautogui.displayMousePosition()



#checks image on screen
while 1:
    if pyautogui.locateOnScreen('ball.png', confidence=0.9) != None:
        print("i see")
        image = pyautogui.locateOnScreen('ball.png', confidence=0.8)
        x, y = pyautogui.center(image)
        pyautogui.moveTo(x,y)
        time.sleep(0.1)
    else:
        print("i cant see")
        time.sleep(0.5)
