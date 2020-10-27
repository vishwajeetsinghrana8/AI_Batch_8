import cv2
import numpy as np

img = cv2.imread("lena.png")

cv2.imshow("Image",img)
cv2.waitKey()

print(img.shape)
print("Height",img.shape[0])
print("Width",img.shape[1])
print("Depth",img.shape[2])
print('\n')
cv2.destroyAllWindows()

h,w,d = np.shape(img)
print("Height",h)
print("Width",w)
print("Depth",d)
print("DataType:",img.dtype)

