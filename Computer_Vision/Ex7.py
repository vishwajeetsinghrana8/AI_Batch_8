import cv2
import numpy as np

img = np.zeros((512,512,3), dtype=np.uint8)
windowName = "Drawing"
cv2.namedWindow(windowName)

# cv2.rectangle(img, (50,50), (150,150), (120,10,50), -1)
# cv2.circle(img, (180,180), 50, (0,255,0), -1)
def draw_circle(event, x,y, flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 50, (0,255,0), -1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 40, (0,0,255), -1)
    if event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img, (x,y), 20, (255,255,255), -1)

cv2.setMouseCallback(windowName, draw_circle)

while True:

    cv2.imshow(windowName,img)
    if cv2.waitKey(20) == 27:
        break

cv2.destroyAllWindows()