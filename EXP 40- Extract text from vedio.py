import cv2
import pytesseract

cap=cv2.VideoCapture("video.mp4")

while True:

    ret,frame=cap.read()

    if not ret:
        break

    text=pytesseract.image_to_string(frame)

    print(text)

    cv2.imshow("Video",frame)

    if cv2.waitKey(30)&0xFF==27:
        break

cap.release()
cv2.destroyAllWindows()
