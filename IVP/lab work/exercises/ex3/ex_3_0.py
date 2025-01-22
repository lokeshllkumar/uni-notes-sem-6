import cv2
import numpy as np

# converting RGB -> grayscale using GSi = 0.299Ri + 0.587Gi + 0.114Bi

img = cv2.imread("IVP/lab work/exercises/ex3/test.jpeg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

red = img_rgb[:, :, 0]
green = img_rgb[:, :, 1]
blue = img_rgb[:, :, 2]

grayscale = 0.299 * red + 0.587 * green + 0.114 * blue

grayscale = np.uint8(grayscale)

cv2.imshow("RGB Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Grayscale Image", grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()
