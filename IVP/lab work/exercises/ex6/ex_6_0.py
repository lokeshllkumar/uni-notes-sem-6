import cv2
import numpy as np
import matplotlib.pyplot as plt

# plot histogram of an image

img = cv2.imread('IVP/lab work/exercises/ex6/test.jpeg', cv2.IMREAD_GRAYSCALE)

histogram = cv2.calcHist([img], [0], None, [256], [0, 256])

plt.figure(figsize = (8, 5))
plt.plot(histogram, color = 'black')
plt.title("Grayscale Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.xlim([0, 256])
plt.show()
