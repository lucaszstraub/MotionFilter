import cv2 as cv
import numpy as np

video = cv.VideoCapture("cars.mp4")

while True:
    _, frame = video.read()
    
    # cv.imshow('frame', frame)
    
    laplacian = cv.Laplacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian) #Converts from float to integer 1 to 255
    # cv.imshow("laplacian", laplacian)
    
    edges = cv.Canny(frame, 200, 200)
    cv.imshow("edges", edges)

    
    
    if cv.waitKey(5) == ord("X"):
        break

video.release()
cv.destroyAllWindows()