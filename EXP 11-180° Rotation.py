import cv2

img = cv2.imread("image.jpg")
rot = cv2.rotate(img, cv2.ROTATE_180)

cv2.imshow("Original", img)
cv2.imshow("180 Degree", rot)
cv2.waitKey(0)
cv2.destroyAllWindows()
