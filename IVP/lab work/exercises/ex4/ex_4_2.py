import cv2
import numpy as np

img = cv2.imread("ex4/test.jpeg")

def generate_motion_blur_kernel(kernel_size, direction = "horizontal"):
    kernel = np.zeros((kernel_size, kernel_size))
    if direction == "horizontal":
        kernel[kernel_size // 2, :] = 1
    elif direction == "vertical":
        kernel[: kernel_size // 2] = 1
    
    kernel /= kernel_size
    return kernel

def apply_motion_blur(img, kernel_size, direction):
    kernel = generate_motion_blur_kernel(kernel_size, direction)
    blurred_img = cv2.filter2D(img, -1, kernel)
    return kernel, blurred_img

# applying horizontal motion blur with a kernel of size 15

kernel, blurred_image = apply_motion_blur(img, 15, "horizontal")
cv2.imshow("Horizontal motion blur applied on image", blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()