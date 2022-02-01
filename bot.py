from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 position: X: 581 Y: 400 RGB: ( 77,  80, 115)
#Tile 2 position: X: 682 Y: 400 RGB: (  0,   0,   0)
#Tile 3 position: X: 770 Y: 400 RGB: ( 79,  82, 116)
#Tiel 4 position: X: 869 Y: 400 RGB: ( 80,  83, 116)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(506, 480)[2] == 0:
        click(506, 480)
    if pyautogui.pixel(611, 480)[2] == 0:
        click(611, 480)
    if pyautogui.pixel(693, 480)[2] == 0:
        click(693, 480)
    if pyautogui.pixel(780, 480)[2] == 0:
        click(780, 480)