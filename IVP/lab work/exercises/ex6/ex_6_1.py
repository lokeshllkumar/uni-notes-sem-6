import cv2
import numpy as np

# perform histogram equalization

img = cv2.imread('ex6/test.jpeg', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
hist = cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)

hist_img = np.ones((300, 256), dtype = np.uint8) * 255

for x in range(256):
    cv2.line(hist_img, (x, 300), (x, 300 - int(hist[x])), 0, 1)

cv2.imshow("Original Image", img)
cv2.imshow("Original Histogram", hist_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

equalized_img = cv2.equalizeHist(img)

hist_eq = cv2.calcHist([equalized_img], [0], None, [256], [0, 256])
hist_eq = cv2.normalize(hist_eq, hist_eq, 0, 255, cv2.NORM_MINMAX)

hist_img_eq = np.ones((300, 256), dtype = np.uint8) * 255

for x in range(256):
    cv2.line(hist_img_eq, (x, 300), (x, 300 - int(hist_eq[x])), 0, 1)

cv2.imshow("Equalized Image", equalized_img)
cv2.imshow("Equalized Histogram", hist_img_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()