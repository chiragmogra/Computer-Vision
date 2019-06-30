import cv2
import numpy as np    
#   It starts the camera | 0 for current pc web cam | 1 for external another webcam
cap=cv2.VideoCapture(0)          
# Add plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
# For saving video
output=cv2.VideoWriter('vid.avi',plugin,25,(640,480))
# It returns True if camera is opened
while cap.isOpened():
    status,frame=cap.read()
    cv2.imshow('frame',frame)
    output.write(frame)      # It saves the video from its all frames
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)        #It use for convert color BGR to Gray
    cv2.imshow('gray',gray)
    # enter q as exit key from webcam
    if cv2.waitKey(1)  & 0xFF==ord('q'):
        break

cap.release()
output.release()
# It destroys all windows of camera
cv2.destroyAllWindows()