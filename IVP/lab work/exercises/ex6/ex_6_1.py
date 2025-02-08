import cv2
import matplotlib.pyplot as plt
import numpy as np

# perform histogram equalization

img = cv2.imread('IVP/lab work/exercises/ex6/test.jpeg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

img_eq = cv2.equalizeHist(img)
histogram_eq = cv2.calcHist([img_eq], [0], None, [256], [0, 256])

cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Equalized Image", img_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure(figsize = (8, 5))
plt.plot(histogram, color = 'black')
plt.title("Grayscale Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 256])
plt.show()

plt.figure(figsize = (8, 5))
plt.plot(histogram_eq, color = 'black')
plt.title("Grayscale Equalized Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 256])
plt.show()
