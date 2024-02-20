import pyautogui, time, keyboard

# Αριθμός δευτερολέπτων
click_interval = 5
is_running = False


def toggle_script():
    global is_running
    if is_running:
        is_running = False
        print("Mouse clicking stopped")
    else:
        is_running = True
        print("Mouse clicking started")

# Αλληλουχία πλήκτρων
keyboard.add_hotkey("ctrl+shift+f", toggle_script)

while True:
    if is_running:
        pyautogui.click()
        time.sleep(click_interval)