import cv2
import imutils

vs = cv2.VideoCapture("video.mp4")

while True:
    rat ,frame = vs.read()
    frame = imutils.resize(frame,width=600)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 150, 200)
    cv2.imshow("Edged",edged)

    if cv2.waitKey(1) & 0xFF == ord('q'):
           break

cv2.destroyAllWindows()
