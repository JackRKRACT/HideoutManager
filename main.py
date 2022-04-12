from interaction import *
import cv2 as cv
from hm_gui import hm_gui
import os
import random

from PIL import Image, ImageTk

#os.system('cls||clear')
#inGame()

x = hm_gui()

'''
inGame()
img = cv.imread("crafts/craft2/produced.png", 0)
locs = findImageScreenVarRes(img, 0.875)
print(locs)
for loc in locs:
    temp = []
    temp.append(loc)
    moveMouse(temp)
    time.sleep(1)

'''

'''
dir = "crafts/craft1/"
items = os.listdir(dir)

for item in items:
    img = cv.imread(dir + item,0)
    loc = findImageScreen(img)
    print(loc)


x = loadModules()
y = loadHideoutModules()

for module in x:
    enterModule(module)


'''
  