import cv2

img = cv2.imread('lena.png')

# print(img)

img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, img3 = cv2.threshold(img2, 126, 255, cv2.THRESH_BINARY_INV)

cv2.imshow("Image",img)
cv2.waitKey()

cv2.imshow("Gray",img2)
cv2.waitKey()

cv2.imshow("Binary",img3)
cv2.waitKey()

cv2.destroyAllWindows()