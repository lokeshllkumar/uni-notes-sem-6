import cv2
import numpy as np

# plot histogram of an image

img = cv2.imread('ex6/test.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist = cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)

hist_img = np.ones((300, 256), dtype = np.uint8) * 255

for x in range(256):
    cv2.line(hist_img, (x, 300), (x, 300 - int(hist[x])), 0, 1)

cv2.imshow("Grayscale Histogram", hist_img)
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
