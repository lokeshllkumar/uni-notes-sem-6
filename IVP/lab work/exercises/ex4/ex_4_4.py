import cv2
import numpy as np

img = cv2.imread("IVP/lab work/exercises/ex4/test.jpeg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# a study on separable filters

row_filter = np.array([1, 2, 3, 4, 5], dtype = np.float32) / (1 + 2 + 3 + 4 + 5)
col_filter = row_filter.reshape(-1, 1)

# performing 1D convolutions with the row and column filters, respectively

def row_convolution(img, row_filter):
    return cv2.filter2D(img, -1, row_filter)

def col_convolution(img, col_filter):
    return cv2.filter2D(img, -1, col_filter)

# 2 subsequent 1D convolutions
blurred_row = row_convolution(img, row_filter)
blurred_col = col_convolution(blurred_row, col_filter)

cv2.imshow("After 1D convolutions", blurred_col)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 1 2D convolution
kernel_2D = np.outer(row_filter, row_filter)
blurred_2D = cv2.filter2D(img, -1, kernel_2D)

cv2.imshow("After 2D convolution", blurred_2D)
cv2.waitKey(0)
cv2.destroyAllWindows()