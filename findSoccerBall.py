import cv2
import numpy as np
import time


#in place of making a cascade file
#would love to replace with cascade when I have the time
def getBestTemplate(img_gray):

	matches = []
	for x in range(8):
		template = cv2.imread(('sb%d.png') % x, 0)
		res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
		threshold = 0.5
		loc = np.where( res >= threshold)
		numMatches = loc[0].size

		print(("Template %d has %d matches") % (x, numMatches))
		matches.append(numMatches)

	return matches.index(max(matches))


def main():
	cap = cv2.VideoCapture(0)

	#delay for camera to light up else too dark
	time.sleep(.1)

	ret, img_rgb = cap.read()

	img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

	whichTemplate = getBestTemplate(img_gray)

	template = cv2.imread(('sb%d.png') % whichTemplate, 0)
	w, h = template.shape[::-1]
	res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
	threshold = 0.5
	loc = np.where( res >= threshold)

	for pt in zip(*loc[::-1]):
		cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

	cv2.imshow(('Detected with %d') % whichTemplate, img_rgb)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

main()






