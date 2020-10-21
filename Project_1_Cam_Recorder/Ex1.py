import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    print(ret)
    
    cv2.imshow("Camera",frame)
    if cv2.waitKey(20) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

