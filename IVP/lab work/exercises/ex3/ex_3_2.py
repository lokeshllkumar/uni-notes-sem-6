import cv2
import numpy as np

# study on spatial resolution: convert a 512 * 512 img into a 256 * 256, 128 * 128, 64 * 64, and 32 * 32 img

img = cv2.imread("IVP/lab work/exercises/ex3/test_512.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def resize(img, new_height, new_width):
    original_height, original_width = img.shape

    new_img = np.zeros((new_height, new_width, 3), dtype = np.uint8)

    scale_y, scale_x = original_height / new_height, original_width / new_width

    for i in range(new_height):
        for j in range(new_width):
            block = img[int(i * scale_y): int((i + 1) * scale_y), int(j * scale_x) : int((j + 1) * scale_x)]
            avg_color = np.mean(block, axis = (0, 1)).astype(np.uint8)
            new_img[i, j] = avg_color
    
    return new_img

cv2.imshow(f"Original Grayscale Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

dims = [(256, 256), (128, 128), (64, 64), (32, 32)]

for i, j in dims:
    temp_img = resize(img, i, j)

    cv2.imshow(f"{i}*{j}", temp_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()