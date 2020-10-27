import cv2
import numpy as np

ref_point = []

def shape_detection(event, x,y, flags,param):
    global ref_point
    
    if event == cv2.EVENT_LBUTTONDOWN:
        ref_point = [(x,y)]

    if event == cv2.EVENT_LBUTTONUP:
        ref_point.append((x,y))
        print(ref_point)
        cv2.rectangle(image, ref_point[0], ref_point[1],(150,50,115), 3)
        cv2.imshow("image",image)


image = cv2.imread("lena.png")
clone = image.copy()
cv2.namedWindow('image')
cv2.setMouseCallback('image', shape_detection)

while True:
    cv2.imshow("image",image)
    k = cv2.waitKey(20)

    if k == ord('r'):
        image = clone.copy()

    if k == ord('c'):
        break

if len(ref_point) == 2:
    crop_img = clone[ref_point[0][1]:ref_point[1][1], ref_point[0][0]:ref_point[1][0]]
    cv2.imshow("Crop_Img",crop_img)
    cv2.imwrite("output.png",crop_img)
    cv2.waitKey()

cv2.destroyAllWindows()