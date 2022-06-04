import numpy as np
import cv2

#loading haarcascade classifiers for face and eye
#You can find these cascade classifiers here
#https://github.com/opencv/opencv/tree/master/data/haarcascades
#or where you download opencv inside data/haarcascades

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#loading the image
img = cv2.imread('D:\Pruebas Python\img\JKfotoTIC.jpg')

#converting the image to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detecting face in the grayscale image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

#iterate through each detected face
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle to each detected face

    #take the roi of the face (region of interest) 
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    #detect the eyes
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:

        #draw rectangle for each eye
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

#show the image
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()