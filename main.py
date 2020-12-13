import pyautogui
import time

history = ('rlawngo','qkqh','sksms','fhqht','dz')
print(pyautogui.position())
pyautogui.moveTo(984,727)

for i in range(0,5):
    pyautogui.click()
    pyautogui.write(history[i] , interval = 0.25)
    pyautogui.press('enter')
    time.sleep(1)
