import pyautogui
import time
from PIL import ImageGrab, Image

# Loop indefinitely
while True:
    location = pyautogui.locateCenterOnScreen("ice_armor.png", confidence=0.9)
    if location is not None:
        pyautogui.press('3')
        print("Casting Ice Armor!")

    location = pyautogui.locateCenterOnScreen("flame_shield.png", confidence=0.9)
    if location is not None:
        pyautogui.press('4')
        print("Casting Flame Shield!")

    # time.sleep(5)
