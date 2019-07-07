import cv2
# start camera
cap=cv2.VideoCapture(0)
tp1=cap.read()[1]       #take 1
tp2=cap.read()[1]       #take 2 
tp3=cap.read()[1]       #take 3
# to make more perfect
gray1=cv2.cvtColor(tp1,cv2.COLOR_BGR2GRAY)   # converting to gray
gray2=cv2.cvtColor(tp2,cv2.COLOR_BGR2GRAY)
gray3=cv2.cvtColor(tp3,cv2.COLOR_BGR2GRAY)

# Now creating image diff
def img_diff(x,y,z):
    #Diff between x & y  -- gray1 and gray2  ==>  d1
    d1=cv2.absdiff(x,y)
    #Diff between y & z  -- gray2 and gray3  ==>  d2
    d2=cv2.absdiff(y,z)
    #Absolute diff b/w d1 & d2
    finalimg=cv2.bitwise_and(d1,d2)
    return finalimg

while cap.isOpened():
    status,frame=cap.read()    # continue image taker
    motionimg=img_diff(gray1,gray2,gray3)
    #replacing image frame
    gray1=gray2
    gray2=gray3
    gray3=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)        # passing live image to gray3
    cv2.imshow('motion',frame)
    cv2.imshow('motion1',motionimg)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
