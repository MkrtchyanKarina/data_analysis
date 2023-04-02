import cv2
import numpy as np
from PIL import Image
import imutils

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture("video.mp4")
fourcc = cv2.VideoWriter_fourcc(*'XVID')


while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(image=gray, minNeighbors=5, minSize=(15, 15), scaleFactor=1.05, maxSize=(60, 60))
    i = 1
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (25, 0, 0), thickness=-1)
        i += 1

    cv2.imshow('video feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
