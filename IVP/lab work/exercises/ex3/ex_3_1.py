import cv2
import numpy as np

# study on intensity resolution: convert an 8-bit grayscale img to 7, 6, 5, 4, 3 and 2 bit images

img = cv2.imread("ex3/test.jpeg")

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def convert_bits(img, bits):
    reduced_img = np.floor((img // (2 ** (8 - bits))) * (2 ** (8 - bits)))
    reduced_img = np.uint8(reduced_img)
    return reduced_img

cv2.imshow(f"Original Grayscale Image", grayscale)
cv2.waitKey(0)
cv2.destroyAllWindows()

for i in range(7, 0, -1):
    temp_img = convert_bits(grayscale, i)

    cv2.imshow(f"{i} bit", temp_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()