import cv2

img = cv2.imread('lena.png')

print(img)

cv2.imshow("Image",img)
cv2.waitKey()

cv2.destroyAllWindows()