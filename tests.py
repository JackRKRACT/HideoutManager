import numpy as np
import cv2 as cv

#im_item = cv.imread(r"C:\Users\Jack\Desktop\Stuff July 2021\Programming\HideoutManager_v2\resources\barter_items\Gunpowder_%22Eagle%22_sm.png")
#im_shape = im_item.shape
#print(im_item.shape) # y, x, channels
#im_item = im_item[14:im_shape[0], 0:im_shape[1]]
#dst2 = cv.fastNlMeansDenoisingColored(im_item,None,10,10,7,21)


im = cv.imread('ses.png')
dst = cv.fastNlMeansDenoisingColored(im,None,10,10,7,21)
imgray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
print(cv.THRESH_BINARY_INV)
#ret, thresh = cv.threshold(imgray, 127, 255, cv.THRESH_BINARY_INV)

blur = cv.GaussianBlur(imgray,(5,5),0)
ret3,thresh = cv.threshold(blur,0,255,cv.THRESH_BINARY+cv.THRESH_OTSU)

#thresh = cv.adaptiveThreshold(imgray,255,cv.ADAPTIVE_THRESH_MEAN_C,\ cv.THRESH_BINARY,11,2)
contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

cv.drawContours(imgray, contours, -1, (0,255,0), 3)

cv.imwrite('ses2.png',imgray)
#cv.imwrite('im2.png', dst2)