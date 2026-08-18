import cv2

cap = cv2.VideoCapture("video.mp4")
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

height, width = frames[0].shape[:2]
out = cv2.VideoWriter("reverse.mp4",
                      cv2.VideoWriter_fourcc(*'mp4v'),
                      30,
                      (width, height))

for frame in reversed(frames):
    out.write(frame)

out.release()

print("Reverse video created successfully.")
