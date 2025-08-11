#!/usr/bin/env python3
# 07_gui_automation.py
# Automate simple keyboard/mouse actions with pyautogui.
# WARNING: Running GUI automation will control your mouse/keyboard. Use carefully.

import time
import pyautogui  # controls keyboard & mouse

def demo_typing(text="Hello from pyautogui!", pause_between=0.12):
    """
    Move mouse to current position, type text, and press enter.
    """
    pyautogui.FAILSAFE = True  # move mouse to a corner to abort
    pyautogui.PAUSE = pause_between  # small pause between actions

    # show a countdown to give user time to focus correct window
    for i in range(5, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)

    print("Typing text now...")
    pyautogui.typewrite(text)   # type the text
    pyautogui.press("enter")    # press Enter
    print("Done.")

if __name__ == "__main__":
    demo_typing()
