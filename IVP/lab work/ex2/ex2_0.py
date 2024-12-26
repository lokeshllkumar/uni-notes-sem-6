import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("ex2/test.jpeg", 1)

# objective: to double the image i.e. increase the image size by 2 times

h, w = img.shape[:2]

img2 = np.zeros((h * 2, w * 2, 3), dtype = np.uint8)

for i in range(h * 2):
    for j in range(w * 2):
        x = i // 2
        y = j // 2

        x1 = x
        x2 = min(x + 1, h - 1)
        y1 = y
        y2 = min(y + 1, w - 1)

        dx = x - x1
        dy = y - y1

        top = (1 - dx) * img[x1, y1] + dx * img[x2, y1]
        bottom = (1 -dx) * img[x1, y2] + dx * img[x2, y2]

        new_pixel = (1 - dy) * top + dy * bottom

        img2[i, j] = np.clip(new_pixel, 0, 255)


cv2.imshow("Resized Image", img2)
cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

thermal_img = cv2.applyColorMap(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.COLORMAP_JET)

cv2.imshow("Thermal Image", thermal_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
