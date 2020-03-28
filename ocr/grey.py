import cv2
import numpy as np
  
image = cv2.imread('../img/002.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
cv2.imshow('Original image',image)
img = cv2.imshow('Gray image', gray)
arr = np.array(img)
print(arr.shape)
  
cv2.waitKey(0)
cv2.destroyAllWindows()