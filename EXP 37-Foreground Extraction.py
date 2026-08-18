import cv2
import numpy as np

img=cv2.imread("image.jpg")

lower=np.array([121,121,121])
upper=np.array([255,255,255])

mask=cv2.inRange(img,lower,upper)

foreground=cv2.bitwise_and(img,img,mask=mask)

cv2.imshow("Foreground",foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()
