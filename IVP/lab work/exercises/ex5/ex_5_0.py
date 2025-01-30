import cv2
import matplotlib.pyplot as plt
import numpy as np

# applying a Gaussian filter on an image

img = cv2.imread("IVP/lab work/exercises/ex5/test.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(img, (5, 5), 0)

cv2.imshow("Blurred Image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()