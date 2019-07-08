import cv2
cap=cv2.VideoCapture(0)
while cap.isOpened():
    status,frame=cap.read()
    redcol=cv2.inRange(frame,(0,0,0),(40,40,255))
    cv2.imshow('liveredcolor',redcol)
    if cv2.waitKey(10)  & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()