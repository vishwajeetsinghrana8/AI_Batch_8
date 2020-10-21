import cv2

rgb = cv2.imread('lena.png')

B,G,R = cv2.split(rgb)

cv2.imshow("RGB",rgb)
cv2.waitKey()

cv2.imshow("Red",R)
cv2.waitKey()

cv2.imshow("Green",G)
cv2.waitKey()

cv2.imshow("Blue",B)
cv2.waitKey()

combine = cv2.merge([B,G,R])
cv2.imshow("Output",combine)
cv2.waitKey()

red = cv2.merge([B-B,G-G,R])
cv2.imshow("R",red)
cv2.waitKey()

green = cv2.merge([B*0,G,R*0])
cv2.imshow("G",green)
cv2.waitKey()

blue = cv2.merge([B,G-G,R-R])
cv2.imshow("B",blue)
cv2.waitKey()

cv2.destroyAllWindows()