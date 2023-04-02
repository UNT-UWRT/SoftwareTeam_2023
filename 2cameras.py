import cv2

cam1 = cv2.VideoCapture(0)
cam2 = cv2.VideoCapture(2)

while True:
        ret1, image1 = cam1.read()
        ret2, image2 = cam2.read()
        cv2.imshow('Front View',image1)
        cv2.imshow('Back View',image2)
        k = cv2.waitKey(1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
cam1.release()
cam2.release()
cv2.destroyAllWindows()
