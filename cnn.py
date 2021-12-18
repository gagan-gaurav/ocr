import numpy as np
import cv2 as cv
import os
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt


path = 'myData'
testRatio = 0.2
valRatio = 0.2

images = []
classNo = []
myList = os.listdir(path)
print(myList)
noOfClasses = len(myList)

for x in range(0, noOfClasses):
	myPicList = os.listdir(path + '/' + str(x))
	for y in myPicList:
		currentImg = cv.imread(path + '/' + str(x) + '/' + y)  
		# print(currentImg)
		currentImg = cv.resize(currentImg, (32, 32))
		classNo.append(x)
		images.append(currentImg)
	print(x, end=" ")
print(" ")

images = np.array(images)
classNo = np.array(classNo)

# print(images.shape)
# print(classNo.shape)


### splitting the data
X_train, X_test, Y_train, Y_test = train_test_split(images, classNo, test_size= testRatio)
X_train, X_validation, Y_train, Y_validation = train_test_split(X_train, Y_train, test_size = valRatio)

noOfSamples = []

print(len(Y_train))
# print(X_train.shape)
# print(X_test.shape)
for x in range(0, noOfClasses):
	noOfSamples.append(len(np.where(Y_train == x)[0]))
print(noOfSamples)

plt.figure(figsize=(10, 5))
plt.bar(range(0,noOfClasses), noOfSamples)
plt.title("no of images of each class")
plt.xlabel("class id")
plt.ylabel("number of images")
plt.show()


def preProcessing(img):
	img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	img = cv.equalizeHist(img)
	cv.imshow('img', img)
	img = img/225
	return img

img = preProcessing(X_train[30])
# img = cv.resize(img, (300, 300))
# cv.imshow('img', img)
cv.waitKey(0)
