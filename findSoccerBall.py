import cv2
import numpy as np
import time


cap = cv2.VideoCapture(0)

time.sleep(.1)

ret, img_rgb = cap.read()


#img_rgb = cv2.imread('sBallTest.png')

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

template = cv2.imread('soccerball5.png', 0)
w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.5
loc = np.where( res >= threshold)

i = 0
for pt in zip(*loc[::-1]):
	i = i + 1
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

print(i)

cv2.imshow('Detected',img_rgb)

cv2.waitKey(0)
cv2.destroyAllWindows()