import cv2
from cv2 import *

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2('haarcascade_smile.xml')
faces = face_cascade.detectMulticale(gray, 1.3, 5)

video_capture = cv2.VideoCapture(0)
while True:
    # captures video frame by frame
    frame = video_capture.read()
    # Capture image in monochrome
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # calls the detect( function)
    canvas = detect(gray, frame)

    #displays the result on camera feed
    cv2.imshow('Video', canvas)
    # the control breaks once q key is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    # release the capture once all the presseing is done
    video_capture.release()
    cv2.destroyAllWindows()