import numpy as np
import cv2

images_data_path = '/Users/memo/_sublime/OpenCV/tests/data/videos/'

cap = cv2.VideoCapture( images_data_path + 'NamJunePaik.mkv')

while(cap.isOpened()):
    ret, frame = cap.read()

    if frame != None:
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	cv2.imshow('frame',gray)
    	if cv2.waitKey(24) & 0xFF == ord('q'):
    		break
    else:
    	break
	    
cap.release()
cv2.destroyAllWindows()