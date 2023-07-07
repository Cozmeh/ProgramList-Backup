import pyautogui,os 
from time import sleep 
os.system('control.exe appwiz.cpl')
sleep(2)
im1 = pyautogui.screenshot()
im1.save('ProgramList.png')
pyautogui.hotkey('alt','f4')
