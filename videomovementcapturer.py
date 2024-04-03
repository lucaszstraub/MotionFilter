import cv2 as cv
video = cv.VideoCapture('cars.mp4')
subtractor = cv.createBackgroundSubtractorMOG2(200,50)    #Identifica o objeto que se move, muito ruido.

while True:
    ret, frame = video.read()
    if ret:
        #Visualize it
        mask = subtractor.apply(frame)
        cv.imshow("mask", mask)
        
        if cv.waitKey(5) == ord('X'):#BREAKS THE CODE
            break
    else:
        #Creates a loop
        video = cv.VideoCapture('cars.mp4')
        
cv.destroyAllWindows()
video.release()