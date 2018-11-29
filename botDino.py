'''
First Stage
'''
# import pyautogui
# import time

# class Coordinates():
#     replayBtn = (340,390)
#     dinosuar = (171,395)

# def restartGame():
#     pyautogui.click(Coordinates.replayBtn)

# def pressSpace():
#     pyautogui.keyDown('space')
#     time.sleep(0.05)
#     print("Jump")
#     pyautogui.keyUp('space')  

# restartGame()
# time.sleep(1)
# pressSpace()

'''
Stage Two
'''

# from PIL import ImageGrab,ImageOps
# import pyautogui
# import time
# from numpy import *

# class Coordinates():
#     replayBtn = (340,390)
#     dinosuar = (171,395)
#     #240 x-coordinate
#     #420 y-coordinate

# def restartGame():
#     pyautogui.click(Coordinates.replayBtn)

# def pressSpace():
#     pyautogui.keyDown('space')
#     time.sleep(0.05)
#     print("Jump")
#     pyautogui.keyUp('space')  

# def imageGrabber():
#     #function to contain coordinates
#     #containing coordinates w.r.t dino
#     box = (Coordinates.dinosuar[0]+60,Coordinates.dinosuar[1],Coordinates.dinosuar[0]+100,Coordinates.dinosuar[1]+30) # 420-390 the difference b/w y coordinates
#     #box = (dinoCord.x+distance+40,dinoCord.Y+30)
#     image = ImageGrab.grab(box)
#     #more efficient in grayscale
#     grayImage = ImageOps.grayscale(image)
#     #convert image to an array
#     a = array(grayImage.getcolors())
#     #print out grayscaled scum of all color values of each pixel in a box
#     return a.sum()

# #Continously Jump
# #while True:
#     imageGrabber()

# #1447 main method
# def main():
#     restartGame()
#     while True:
#         if(imageGrabber()!=1447):
#             pressSpace()
#             time.sleep(0.1)

# main()
# #time.sleep(1)
# #pressSpace()




from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class Coordinates():
    replayBtn = (340,390)
    dinosuar = (171,438) #437-395 = 42px (for crouch of dino)
    #240 x-coordinate
    #420 y-coordinate

def restartGame():
    pyautogui.click(Coordinates.replayBtn)
    pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    #time.sleep(0.05)
    print("Jump")
    time.sleep(0.18)
    pyautogui.keyUp('space')  
    pyautogui.keyDown('down')

    #we record the jumping of dinosaur, exact time for the jump



def imageGrabber():
    #function to contain coordinates
    #containing coordinates w.r.t dino
    box = (Coordinates.dinosuar[0]+65,Coordinates.dinosuar[1],
    Coordinates.dinosuar[0]+150,Coordinates.dinosuar[1]+5) # 420-390 the difference b/w y coordinates
    #box = (dinoCord.x+distance+40,dinoCord.Y+30)
    image = ImageGrab.grab(box)
    #more efficient in grayscale
    grayImage = ImageOps.grayscale(image)
    #convert image to an array
    a = array(grayImage.getcolors())
    #print out grayscaled scum of all color values of each pixel in a box
    print(a.sum())
    return a.sum()

#Continously Jump
#while True:
    #imageGrabber()
 
#1447 main method
def main():
    restartGame()
    while True:
        if(imageGrabber()!=672):
            pressSpace()
            time.sleep(0.1)

main()
#time.sleep(1)
#pressSpace()         