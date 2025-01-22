import cv2
import numpy as np

img = cv2.imread("IVP/lab work/exercises/ex3/test_128.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# implementing nearest neighbour interpolation

def nn_interpolation(img, new_height, new_width):
    original_height, original_width = img.shape
    new_img = np.zeros((new_height, new_width, 3), dtype = np.uint8)

    scale_y, scale_x = original_height / new_height, original_width / new_width 

    for i in range(new_height):
        for j in range(new_width):
            new_img[i, j] = img[int(i * scale_y), int(j * scale_x)]

    return new_img

cv2.imshow(f"Original Grayscale Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

dims = [(256, 256), (512, 512)]

for i, j in dims:
    temp_img = nn_interpolation(img, i, j)

    cv2.imshow(f"{i}*{j}", temp_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()