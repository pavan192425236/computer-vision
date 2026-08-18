import cv2
import numpy as np

h=int(input("Height: "))
w=int(input("Width: "))

img=np.ones((h,w,3),dtype=np.uint8)*255

cv2.circle(img,(w//2,h//2),100,(255,0,0),3)

cv2.imshow("Circle",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
