import cv2
import matplotlib.pyplot as plt
import numpy as np

# to apply Gaussian noise to an image

img = cv2.imread("IVP/lab work/exercises/ex5/test.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

mean, std = 0, 25
noise = np.random.normal(mean, std, img.shape).astype(np.uint8)

noisy_img = cv2.add(img, noise)

cv2.imshow("Noisy Image", noisy_img)
cv2.waitKey(0)
cv2.destroyAllWindows()