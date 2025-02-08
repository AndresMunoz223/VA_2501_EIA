import cv2
import numpy as np
import imutils
import requests

capturephone = "http:/192.168.137.203:4747/shot.jpg"

while True:
    img_request = requests.get(capturephone)
    img_array = np.array(bytearray(img_request.content), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)
    cv2.imshow("image phone", cv2.resize(img, (640, 480)))
    if cv2.waitKey(1) ==27:
        break
cv2.destroyAllWindows()