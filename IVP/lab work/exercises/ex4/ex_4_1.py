import cv2
import numpy as np
import matplotlib.pyplot as plt

# simulating a defocus blur usign a circular kernel

img = cv2.imread("IVP/lab work/exercises/ex4/test.jpeg")

def generate_circular_kernel(kernel_size):
    kernel = np.zeros((kernel_size, kernel_size), dtype = np.float32)
    radius = kernel_size // 2
    y, x = np.ogrid[:kernel_size, :kernel_size]
    mask = (x - radius) ** 2 + (y - radius) ** 2 <= radius ** 2
    kernel[mask] = 1

    kernel /= kernel.sum()
    return kernel

def defocus(img, kernel_size):
    kernel = generate_circular_kernel(kernel_size)
    defocused_img = cv2.filter2D(img, -1, kernel)
    return kernel, defocused_img

# using a kernel of size 15(radius)

kernel, defocused_img = defocus(img, 5)
cv2.imshow("Defocused image using a circular kernel of radius 5", defocused_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Custom kernel used of radius 5 = ", kernel)

# can also use a Gaussian filter