import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
ouput = cv2.VideoWriter('Register.avi',fourcc,20.0,(640,480) )

while cap.isOpened():
    ret,frame = cap.read()
    ouput.write(frame)
    gray =cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    if ret == True:
        cv2.imshow("Camera ",gray)

        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
ouput.release()
cv2.destroyAllWindows()