# Code to check if left or right mouse buttons were pressed
import win32api

win_pressed = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128

while True:
    mouse_click = win32api.GetKeyState(0x01)

    if mouse_click != win_pressed:  # Button state changed
        win_pressed = mouse_click
        if mouse_click < 0:
            print('Left Button Pressed')