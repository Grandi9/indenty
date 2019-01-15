import cv2
 
image = cv2.imread('path')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
cv2.imshow('Original image',image)
cv2.imshow('Gray image', gray)
