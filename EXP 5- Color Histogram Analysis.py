import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image.jpg")
colors = ('b','g','r')

for i, c in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=c)

plt.title("Color Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()
