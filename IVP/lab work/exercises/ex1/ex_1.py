import cv2
import numpy as np

cascade = cv2.CascadeClassifier("IVP/lab work/haarcascade/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("IVP/lab work/haarcascade/haarcascade_eye.xml")

img = cv2.imread("IVP/lab work/exercises/ex1/np_test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cascade.detectMultiScale(gray, 1.3, 5)

for x, y, w, h in faces:
    c_x, c_y = x + w // 2, y + h // 2
    radius = max(w, h) // 2

    cv2.circle(img, (c_x, c_y), radius, (255, 0, 0), 2)
    roi_gray = gray[y: y + h, x: x + w]
    roi_color = img[y: y + h, x: x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)

for x, y, w, h in eyes:
    eye_c_x, eye_c_y = x + w // 2, y + h // 2
    eye_radius = max(w, h) // 2
    cv2.circle(roi_color, (eye_c_x, eye_c_y), eye_radius, (0, 255, 0), 2)
cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()