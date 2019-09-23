import numpy as np
import cv2

img = cv2.imread('glasses.png',cv2.IMREAD_COLOR)

# cv2.rectangle(img,(15,25),(200,150),(0,0,255),15)
cv2.circle(img,(100,63), 55, (0,255,0), -1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()