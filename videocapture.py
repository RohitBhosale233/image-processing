import cv2,time

video=cv2.VideoCapture(0)
counter=1

while 1:
    counter=counter+1
    check,frame=video.read()
   
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #huesaturation=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    colorvideo=cv2.bitwise_and(frame,frame)
    cv2.imshow('Capturing video',colorvideo)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
print(counter)
video.release()
cv2.destroyAllWindows()
