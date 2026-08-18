import cv2
import numpy as np

img=cv2.imread("image.jpg")

lower=np.array([0,0,0])
upper=np.array([120,120,120])

mask=cv2.inRange(img,lower,upper)

background=cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("Background",background)
cv2.waitKey(0)
cv2.destroyAllWindows()
