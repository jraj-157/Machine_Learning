import cv2 as cv
import numpy as np

img = cv.imread('/Users/jagnyarajpatnaik/Desktop/opencv_projects/Screenshot 2022-04-10 at 10.02.19 AM.png',1)

img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV) # converting to HSV color range
img_threshold = cv.inRange(img_HSV,(25,100,100),(35,255,255)) # making the mask based on hsv range
k1 = cv.bitwise_and(img, img, mask = img_threshold) # converting the white color to yellow by bitwise


cv.imshow('image',img)
cv.imshow("Timg",k1)
cv.waitKey(0)
cv.destroyAllWindows()