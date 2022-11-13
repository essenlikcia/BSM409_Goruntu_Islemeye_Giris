import cv2
import numpy as np

img = cv2.imread("noisy.jpg")
median = cv2.medianBlur(img, 5)
compare = np.concatenate((img, median), axis=1) # side by side comparison

cv2.imshow("image comparison", compare)
cv2.waitKey()
cv2.destroyAllWindows()