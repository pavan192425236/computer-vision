import cv2
import numpy as np

h=int(input("Height: "))
w=int(input("Width: "))

img=np.ones((h,w,3),dtype=np.uint8)*255

bh=h//10
bw=w//10

img[0:bh,0:bw]=(0,0,0)
img[0:bh,w-bw:w]=(255,0,0)
img[h-bh:h,0:bw]=(0,255,0)
img[h-bh:h,w-bw:w]=(0,0,255)

cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
