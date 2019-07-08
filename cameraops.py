import cv2
#starting camera 
cap=cv2.VideoCapture(0)
#                  first camera
# to check camera is opened or not 
'''if cap.isOpened():
    print("camera is ready to take pics")
else:
    print("not ready")
status,img =cap.read()
status1,img=cap.read()
cv2.imshow('liveimage',img)
cv2.imshow('liveimage1',img)
cv2.waitKey(0)
cap.release()

while cap.isOpened():
    status,frame=cap.read()
    #print(frame.shape)
    grayimage=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('live1',grayimage)
    cv2.line(frame,(0,0),(200,300),(0,255,0),3)  #line
    cv2.rectangle(frame,(50,50),(150,200),(0,0,255),2) # rectangle
    cv2.circle(frame,(200,300),100,(255,0,0))   #circle
    font=cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(frame,'OpenCV',(10,300),font,2,(0,2,55),2,cv2.LINE_AA)   #Put Text
    cv2.imshow('live',frame)
    if cv2.waitKey(10) & 0xff ==ord('q'):        #press q to terminate
        break
cv2.destroyAllWindows()
cap.release() '''
# add plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
#saving video
output=cv2.VideoWriter('class.avi',plugin,60,(640,480))


while cap.isOpened():
    status,frame=cap.read()

    cv2.imshow('live',frame)
    output.write(frame)
    if cv2.waitKey(10) & 0xff ==ord('q'):        #press q to terminate
        break

cv2.destroyAllWindows()
cap.release()