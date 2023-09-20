import pyautogui
from random import randrange

i = 10

while i > 0:
    x = randrange(-100, 100)
    y = randrange(-200, 200)
    pyautogui.move(x, y)
    pyautogui.alert("Simple message")
    pyautogui.sleep(1)
    i -=1

