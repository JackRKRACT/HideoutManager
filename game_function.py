from numpy.core.fromnumeric import prod
import interaction as ina
import cv2 as cv
import time
import win32api
import pyautogui
import numpy as np
from PIL import ImageGrab as imgr
import os

# Goal of this is to create a universal craft functionality for the Hideout Manager
# User will click the timer icon in the hideout to create a new craft
# After clicking, Hideout Manager will select a region that contains all potential adjacent items 
# It will isolate all items that exist within this region, and produce images and JSON for the related items
# Filling in additional craft details will come later?

# Will get the current screen of the user, returning a PIL image
def getScreen():
    return
# Takes in a PIL image and converts it into a cv2 image
def convertToCV(pil_image):
    return

# Repeatedly searches until it finds image, returns location(s) of image upon first instance
def searchImage(image):
    while(True):
        image_loc = ina.findImageScreenVarRes(image, 0.85)
        if (len(image_loc) != 0):
            return image_loc
        time.sleep(0.1)

# Returns location of next mouse click
def nextClick():
    win_pressed = win32api.GetKeyState(0x01)
    while True:
        mouse_click = win32api.GetKeyState(0x01)
        if mouse_click != win_pressed:  # Button state changed
            win_pressed = mouse_click
            if mouse_click < 0:
                loc = pyautogui.position()
                return loc

def noProduced():
    produced = cv.imread("resources/learning_images/produced_text.png", 0)
    while len(ina.findImageScreen(produced)) != 0:
        time.sleep(1)
    return True

def exportImage(image, start, end, name):
    cropped = image[start[1]:end[1], start[0]:end[0]]
    cv.imwrite(name,cropped)

# Pass this the 'clock' image location, returns region array.
def isolateRegion(clock_location):
    produced_starting = (clock_location[0] + 110, clock_location[1] - 17)
    produced_ending = (produced_starting[0] + 60, produced_starting[1] + 60)
    ina.moveMouse([produced_starting])
    curr_screen = np.asarray(imgr.grab())
    exportImage(curr_screen, produced_starting, produced_ending, "Produced.png")
    return


def clickedClock(clock_img, clock_res):
    while(True):
        clock_locations = searchImage(clock_img)
        click_location = nextClick()

        for loc in clock_locations:
            clock_bound = (loc[0] + clock_res[1], loc[1] + clock_res[0])
            #print("Clock location " + str(loc))
            #print("Click location " + str(click_location))
            if click_location[0] > loc[0] and click_location[1] > loc[1]:
                if click_location[0] < clock_bound[0] and click_location[1] < clock_bound[1]:
                    #print("User actually clicked the clock")
                    return loc


def createCraft(name):
    current_dir = os.listdir()
    if 'crafts' in current_dir:
        current_dir = 'crafts/' + name
        os.mkdir('crafts/' + name)
    else:
        os.mkdir('crafts')
        current_dir = 'crafts/' + name
        os.mkdir('crafts/' + name)

    
        

# Starts searching for clock images
def newCraft():
    clock = cv.imread("resources/watch_test.png", 0)
    clock_res = clock.shape # y, x, channels
    # Make sure user is in game
    ina.inGame()
    # Find craft via clock location click
    loc = clickedClock(clock, clock_res)
    print("User clicked clock at : " + str(loc))
    isolateRegion(loc)

#newCraft()

createCraft("GreenGP")

