import cv2
import numpy as np

text=input("Enter Text: ")

img=np.ones((500,700,3),dtype=np.uint8)*255

cv2.putText(img,text,(50,250),
cv2.FONT_HERSHEY_SIMPLEX,
2,(0,0,255),3)

cv2.imshow("Text",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
