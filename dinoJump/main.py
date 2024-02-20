import keyboard
import pyautogui as pag

HITBOX = (686, 464, 737, 491)


def jump():
    screen = pag.screenshot()
    BG_COLOR = screen.getpixel((796, 495))
    for x in range(HITBOX[0], HITBOX[2]):
        for y in range(HITBOX[1], HITBOX[3]):
            pixel = screen.getpixel((x, y))
            if pixel != BG_COLOR:
                pag.press('space')
                print("Jumped!")
                return


while not keyboard.is_pressed('space'):
    pass

while True:
    jump()
