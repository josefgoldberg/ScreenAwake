import pyautogui
import webbrowser
import time
import os
import time
import requests
from lxml import html
import sys
from selenium import webdriver

def onlyMove():
    print('Keep the mouse in the top left corner to stop the Move function.')
    currentMouseX, currentMouseY = pyautogui.position()
    while(currentMouseX != 0 and currentMouseY != 0):
        currentMouseX, currentMouseY = pyautogui.position()
        if currentMouseX >= 1000:
            directionX = -20
        else:
            directionX = 20
        if currentMouseY >= 500:
            directionY = -20
        else:
            directionY = 20
        if currentMouseX + directionX == 1 and currentMouseY + directionY ==1:
            directionX = 100
            directionY = 100
        pyautogui.moveTo(currentMouseX+directionX, currentMouseY+directionY, duration=1)
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
        pyautogui.click(100, 60, duration=0)
        #pyautogui.hotkey("ctrl", "r")
        i += 1
        time.sleep(10)
        currentMouseX, currentMouseY = pyautogui.position()

def termStatus():
    currentMouseX, currentMouseY = pyautogui.position()
    while(currentMouseX != 0 and currentMouseY != 0):
        os.system('cls')
        urls = ["http://128.226.95.31/prnLcdStatus.dhtml", "http://128.226.95.32/prnLcdStatus.dhtml", "http://128.226.95.34/home/index.html#hashHome", "http://128.226.95.33/prnLcdStatus.dhtml", "http://128.226.162.41/prnLcdStatus.dhtml", "http://128.226.162.42/prnLcdStatus.dhtml", "http://128.226.162.43/home/index.html#hashHome", "http://128.226.61.36/prnLcdStatus.dhtml"]
        labels = ["AAG06-1", "AAG06-2", "AAG06-C", "AAG14", "SLIC-1", "SLIC-2", "SLIC-C", "S3G13"]	
        for i in range(0,8):
            try:
                if i==2 or i==6:
                    #TODO find solution for color printers
                    raise Exception('Color Printers not yet compatible.')
                    print(labels[i], "-", page.xpath('//label[@class="xux-labelableBox-label"]/text()'))
                else:
                    test = requests.get(urls[i])
                    page = html.fromstring(test.content)
                    print(labels[i], "-", page.xpath('//td[@class="myAttributeDescriptor"]/text()'))
            except:
                print(labels[i], "-", "Status Unavailable")
                #print(sys.exc_info())
        print('')
        print('Keep the mouse in the top left corner to stop the status function.')
        time.sleep(10)
        currentMouseX, currentMouseY = pyautogui.position()

def printCommandList():
    print('Command List:')
    print("    'Move' - keeps the computer awake by moving the mouse")
    print("    'Open' - opens each printer status link")
    print("    'Rotate' - rotates between all printer status links")
    print("    'Status' - shows the status of all BW printers in terminal")
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
    elif inp == 'Status':
        termStatus()
    elif inp == 'Quit':
        break
    else:
        print("Invalid Input")
