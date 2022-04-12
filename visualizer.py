import numpy as np
import cv2 as cv
from PIL import ImageGrab
import random

def getFrame():
    pil_image = ImageGrab.grab().convert('RGB') 
    open_cv_image = np.array(pil_image) 
    open_cv_image = cv.fastNlMeansDenoisingColored(open_cv_image,None,10,10,7,21)
    # Convert RGB to BGR 
    open_cv_image = open_cv_image[:, :, ::-1].copy()
    img_gray = cv.cvtColor(open_cv_image, cv.COLOR_BGR2GRAY)

    template = cv.imread("C:/Users/Jack/Desktop/Stuff July 2021/Programming/HideoutManager_v2/resources/learning_images/green.png")
    #template = cv.imread("C:/Users/Jack/Desktop/Stuff July 2021/Programming/HideoutManager_v2/resources/learning_images/shell.png")
    template = cv.fastNlMeansDenoisingColored(template,None,10,10,7,21)
    template = cv.cvtColor(template, cv.COLOR_BGR2GRAY)
    #template = cv.imread("C:/Users/Jack/Desktop/Stuff July 2021/Programming/HideoutManager_v2/resources/learning_images/bullet.png", 0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.82
    loc = np.where( res >= threshold)
    color = (random.randrange(255), random.randrange(255), random.randrange(255))
    placed = False
    for pt in zip(*loc[::-1]):
        cv.rectangle(open_cv_image, pt, (pt[0] + w, pt[1] + h), color, 2)
        #cv.rectangle(open_cv_image, (960, pt[1] - h), (1850, pt[1] + h * 4), color, 2)
    
    return open_cv_image

running = True

while running:
    # Get a numpy array to display from the simulation
    npimage=getFrame()

    cv.imshow('image',npimage)
    if cv.waitKey(1) == 27:
        running = False

cv.destroyAllWindows()