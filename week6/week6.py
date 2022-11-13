import cv2
import numpy as np

image = cv2.imread("cat.png")

# create kernel(2d convolution matrix)
kernel1 = np.ones((5,5), np.float32)/25

# apply filter2d() func
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernel1)

# show original and output image
cv2.imshow("original", image)
cv2.imshow("kernel blur", img)

im1 = cv2.blur(image,(5, 5))
im2 = cv2.boxFilter(img, -1, (2, 2), normalize=True) # cv2.boxFilter(src, dst, depth, ksize, anchor, normalize, bordertype)
cv2.imshow("image", np.hstack((im1, im2)))

cv2.waitKey()
cv2.destroyAllWindows()
