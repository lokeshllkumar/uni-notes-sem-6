import cv2
import numpy as np

img = cv2.imread("ex4/test.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# a demonstration of convolution vs correlation

def custom_kernel(kernel_size):
    kernel = np.random.rand(kernel_size, kernel_size)
    kernel /= kernel.sum()

    return kernel

# to demonstrate the difference between the 2 processes, we generate a high variety kernel of size 9

kernel = custom_kernel(9)

def correlation(img, kernel):
    blurred_img = cv2.filter2D(img, -1, kernel)
    return blurred_img
    
def convolution(img, kernel):
    flipped_kernel = np.flipud(np.fliplr(kernel))
    blurred_img = cv2.filter2D(img, -1, flipped_kernel)
    return blurred_img

img_1 = correlation(img, kernel)
cv2.imshow("Upon correlation", img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

img_2 = convolution(img, kernel)
cv2.imshow("Upon convolution", img_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("Kernel used = ", kernel)