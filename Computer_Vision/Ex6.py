import cv2
import numpy as np

img = cv2.imread("lena.png")

print(img.shape)

height, width = img.shape[:2]
#Starting Point
x1, y1 = int(height* .20), int(width* .20)

#End Point
x2, y2 = int(height* .85), int(width* .85)


crop = img[x1:x2, y1:y2]

cv2.imshow("Image",img)
cv2.waitKey()

cv2.imshow("Crop",crop)
cv2.waitKey()

cv2.destroyAllWindows()