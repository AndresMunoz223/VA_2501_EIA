import cv2

# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("clase3/videos/2024-10-17 21-45-38.mp4")

while capture.isOpened():
    ret, frame = capture.read()
    if ret == False:
        break
    cv2.imshow('Camera 1', frame)
    cv2.waitKey(1)
cv2.destroyAllWindows()