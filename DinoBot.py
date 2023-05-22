import pyautogui
from PIL import Image, ImageGrab
import time
# from numpy import asarray 

def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(700,720):
            for j in range(330,400):
                if data[i, j] <90:
                    return True
    return False

if __name__=='__main__':
    time.sleep(2)
    while True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        # image.show()
        # print(asarray(image))
        
        if(isCollide(data)):
            hit("up")


        for i in range(700,740):
                for j in range(340,370):
                    data[i, j] = 0

        # image.show()           
