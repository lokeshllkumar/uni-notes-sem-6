import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("ex4/test.jpeg")

# applying box kernels of varying dimension
kernel_sizes = [3, 5, 7, 9]
filtered_images = []

for k in kernel_sizes:
    filtered = cv2.blur(img, (k, k))
    filtered_images.append((k, filtered))

for i, (k, filtered) in enumerate(filtered_images):
    cv2.imshow(f"{k} * {k} filter", filtered)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# applying a custom box filter to blur the image

def custom_blur(img, kernel_size):
    kernel = np.random.rand(kernel_size, kernel_size)
    kernel /= kernel.sum()

    filtered = cv2.filter2D(img, -1, kernel)
    return kernel, filtered

# using a 9 * 9 custom filter

custom_kernel, blurred = custom_blur(img, 9)
cv2.imshow(f"Custom 9 * 9 filter", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
print("Custom 9 * 9 kernel used = ", custom_kernel)  
