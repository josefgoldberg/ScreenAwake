import time
from Quartz.CoreGraphics import CGEventCreateMouseEvent
from Quartz.CoreGraphics import CGEventPost
from Quartz.CoreGraphics import kCGEventMouseMoved
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseDown
from Quartz.CoreGraphics import kCGEventLeftMouseUp
from Quartz.CoreGraphics import kCGMouseButtonLeft
from Quartz.CoreGraphics import kCGHIDEventTap
print("Moving Mouse Begins...")

def mouseEvent(type, posx, posy):
    theEvent = CGEventCreateMouseEvent(
                                       None,
                                       type,
                                       (posx,posy),
                                       kCGMouseButtonLeft)
    CGEventPost(kCGHIDEventTap, theEvent)

def mousemove(posx,posy):
    mouseEvent(kCGEventMouseMoved, posx,posy)

i = 0
while True:
    try:
        mousemove(i, 20)
        print("Mouse moved to: ("+str(i)+",20)")
        time.sleep(30)
        i += 50
        if i==300:
            i = 0
    except:
        print("Goodbye...")
        exit()
