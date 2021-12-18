import numpy as np
import cv2 as cv
import os
 
path = 'myData'

images = []
myList = os.listdir(path)
print(myList)
noOfClasses = len(myList)

for x in range(0, noOfClasses):
	myPicList = os.listdir(path + '/' + str(x))
	for y in myPicList:
		currentImg = cv.imread(path + '/' + str(x) + str(y))  
		currentImg = cv.resize(currentImg, (32, 32))
		images.append(currentImg)