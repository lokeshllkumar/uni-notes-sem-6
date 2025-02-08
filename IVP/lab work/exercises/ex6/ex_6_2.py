import cv2
import matplotlib.pyplot as plt
import numpy as np

def match_histogram(source, ref):
    src_values, src_counts = np.unique(source.ravel(), return_counts=True)
    ref_values, ref_counts = np.unique(ref.ravel(), return_counts=True)

    src_cdf = np.cumsum(src_counts).astype(np.float32) / source.size
    ref_cdf = np.cumsum(ref_counts).astype(np.float32) / ref.size

    mapping = np.interp(src_cdf, ref_cdf, ref_values)

    matched = np.interp(source.ravel(), src_values, mapping).reshape(source.shape).astype(np.uint8)

    return matched

source_img = cv2.imread('IVP/lab work/exercises/ex6/test.jpeg')
source_img = cv2.cvtColor(source_img, cv2.COLOR_BGR2GRAY)
ref_img = cv2.imread('IVP/lab work/exercises/ex6/test_512.png')
ref_img = cv2.cvtColor(ref_img, cv2.COLOR_BGR2GRAY)

matched_img = match_histogram(source_img, ref_img)

plt.figure(figsize = (12, 4))

plt.subplot(1, 3, 1)
plt.imshow(source_img, cmap = 'gray')
plt.title('Source Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(ref_img, cmap = 'gray')
plt.title('Reference Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(matched_img, cmap = 'gray')
plt.title('Matched Image')
plt.axis('off')

plt.tight_layout()
plt.show()

hist_src = cv2.calcHist([source_img], [0], None, [256], [0, 256])
hist_ref = cv2.calcHist([ref_img], [0], None, [256], [0, 256])
hist_matched = cv2.calcHist([matched_img], [0], None, [256], [0, 256])

cv2.imshow("Source Image", source_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("ref Image", ref_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("Histogram Matched Image", matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

plt.figure(figsize = (12, 5))

plt.subplot(1, 2, 1)
plt.plot(hist_src, color = 'red', label = 'Source Histogram')
plt.plot(hist_ref, color = 'green', label = 'Reference Histogram')
plt.title('Original Histograms')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(hist_src, color = 'red', linestyle = 'dashed', label = 'Source Histogram (Before)')
plt.plot(hist_ref, color = 'green', label = 'Reference Histogram')
plt.plot(hist_matched, color = 'blue', label = 'Matched Histogram')
plt.title('After Histogram Modification')
plt.legend()

plt.show()
