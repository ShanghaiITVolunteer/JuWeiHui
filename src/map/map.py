import cv2
import numpy as np
import sys


im = cv2.imread('..\\..\\files\\neighbour.jpg')
imcopy = im.copy()

gray = cv2.cvtColor(imcopy, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.adaptiveThreshold(blur, 255, 1, 1, 11, 2)
cv2.imshow('norm',thresh)
cv2.waitKey(0)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

samples =  np.empty((0,100))
responses = []
keys = [i for i in range(48,58)]

for cnt in contours:
    if cv2.contourArea(cnt)>50:
        [x,y,w,h] = cv2.boundingRect(cnt)
        print(x, y, w, h)