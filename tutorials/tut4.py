import cv2
import numpy as np

img = cv2.imread('glasses.png',cv2.IMREAD_COLOR)

px = img[55,55]

img[55,55] = [255,255,255]

px = img[100:150,100:150]
print(px)


watch_face = img[37:111,107:194]
img[0:74,0:87] = watch_face

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()