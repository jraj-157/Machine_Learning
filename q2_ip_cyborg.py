import cv2 as cv
import numpy as np
import math

r2t = 180/np.pi
t2r = np.pi/180
x = 0 
y = 0
font_style = cv.FONT_HERSHEY_PLAIN
# e = False
# t = False
# s = False

img = cv.imread('/Users/jagnyarajpatnaik/Desktop/opencv_projects/q2.jpg',1)
# def f(img):

edges = cv.Canny(img,50,150) # edge detection
lines = cv.HoughLines(edges,1,np.pi/180, 200) # detecting hough lines

for line in lines:
    rho,theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))
    # y1 stores the rounded off value of (r * sin(theta)+ 1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))
    # x2 stores the rounded off value of (r * cos(theta)+ 1000 * sin(theta))
    x2 = int(x0 - 1000 * (-b))
    # y2 stores the rounded off value of (r * sin(theta)- 1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))
    cv.line(img, (x1, y1), (x2, y2), (255, 255, 255), 2)
    if (x2-x1==0):
        th = np.pi/2;
    else:
        th = math.atan((y2-y1)/(x2-x1))*r2t
text1 = str(th)
org = (x2,y2)
font = cv.FONT_HERSHEY_COMPLEX_SMALL
fontScale = 1

# text2 = str(180-th)
# org = (150,50)
# font = cv.FONT_HERSHEY_COMPLEX_SMALL
# fontScale = 1

 
color = (0,0,255)  #(B, G, R)
thickness = 3
lineType = cv.LINE_AA
bottomLeftOrigin = True
img_text1 = cv.putText(img, text1, org, font, fontScale, color, thickness, lineType, bottomLeftOrigin=False)
# img_text2 = cv.putText(img, text2, org, font, fontScale, color, thickness, lineType, bottomLeftOrigin=False)
print("acute angle is = " +str(th))
print("obtuse angle is = "+str(180-th))
print(x1,y1)
print(x2,y2)
cv.imshow('image', img_text1)
# cv.imshow('image', img_text2)

k = cv.waitKey(0)
cv.destroyAllWindows()
