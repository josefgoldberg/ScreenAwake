print("Starting up... Hold on...")

import pyautogui
import webbrowser
import time
import os

def onlyMove():
    print('Keep the mouse in the top left corner to stop the Move function.')
    currentMouseX, currentMouseY = pyautogui.position()
    while(currentMouseX != 0 and currentMouseY != 0):
        currentMouseX, currentMouseY = pyautogui.position()
        pyautogui.moveTo(currentMouseX+3, currentMouseY)
        time.sleep(10)
        currentMouseX, currentMouseY = pyautogui.position()

def openLinks():
    urls = ["http://128.226.95.31/", "http://128.226.95.32/", "http://128.226.95.34/", "http://128.226.95.33/", "http://128.226.162.41/", "http://128.226.162.42/", "http://128.226.162.43/", "http://128.226.61.36/"]
    for url in urls:
        webbrowser.get().open(url)

def rotateTabs():
    i = 0
    print('Keep the mouse in the top left corner to stop the rotate function.')
    currentMouseX, currentMouseY = pyautogui.position()
    while(currentMouseX != 0 and currentMouseY != 0):
        if i==8:
            i = 0
            time.sleep(30)
        pyautogui.click(100 + 210*i,20, duration=1)
        #pyautogui.click(100, 60, duration=0)
        pyautogui.hotkey("ctrl", "r")
        i += 1
        time.sleep(10)
        currentMouseX, currentMouseY = pyautogui.position()

def printCommandList():
    print('Command List:')
    print("    'Move' - keeps the computer awake by moving the mouse")
    print("    'Open' - opens each printer status link")
    print("    'Rotate' - rotates between all printer status links")
    print("    'Quit' - closes the program")

linkOpen = False
while(True):
    os.system("cls")
    printCommandList()
    inp = input('Command: ')
    if inp == 'Move':
        onlyMove()
    elif inp == 'Open':
        linkOpen = True
        openLinks()
    elif inp == 'Rotate':
        if linkOpen == False:
            openLinks()
            rotateTabs()
        else:
            webbrowser.get()
            rotateTabs()
    elif inp == 'Quit':
        break
    else:
        print("Invalid Input")
        
        
