import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

upper_cascade = cv2.CascadeClassifier("./opencv-master\data\haarcascades_cuda\haarcascade_upperbody.xml")

while cv2.waitKey(33) != ord('q'):
    ret, frame = capture.read()
    upper = upper_cascade.detectMultiScale(frame, 1.01 , 10, 0, minsize=(100,100))

    for x,y,w,h in upper:
        print(x,y,w,h)
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5, cv2.LINE_8)
    
    
    cv2.imshow("VideoFrame", frame)


capture.release()
cv2.destroyAllWindows()