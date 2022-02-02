from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from enum import Enum

delay = 0.0001

COOKIE_POSITION = (286, 511)


class State(Enum):
    CLICKING = 1
    UPGRADEING = 2

class Clickerbot():
    def _init_(self, delay, button):
        self.delay = delay
        self.state = State['CLICKING']
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True
    
    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        time.sleep(0.01)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    def run(self):
        while self.program_running:
            if keyboard.is_pressed('s'): 
                if self.running:
                    self.stop_clicking()
                else:
                    self.start_clicking()
            while self.running:
                match self.state:
                    case State.CLICKING:
                        click(COOKIE_POSITION[0], COOKIE_POSITION[1])
                        time.sleep(self.delay)
                    
                    case State.UPGRADEING:
                        pass


