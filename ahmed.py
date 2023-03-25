import pyautogui as spam
import time
limit = input("enter number of messegs :")
msg = input("enter messeg you want to send:")
i = 0
time.sleep(10)
while i<int(limit):
    
    spam.typewrite(msg)
    spam.press('Enter')
    i =i+1 

    



