import numpy as np
import cv2 as cv
import os
from time import time
from vision import Vision

cascade_cone = cv.CascadeClassifier('cascade/old cascades/c9/cascade.xml')
vision_cone = Vision(None)
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    rectangles = cascade_cone.detectMultiScale(frame)
    scanned = vision_cone.draw_rectangles(frame, rectangles)
    cv.imshow('frame',scanned)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()