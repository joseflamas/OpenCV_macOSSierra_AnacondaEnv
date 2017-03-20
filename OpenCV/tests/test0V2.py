import numpy as np
import cv2

images_data_path = '/Users/memo/_sublime/OpenCV/tests/data/videos/'

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter( images_data_path + 'FlipVideoInput.avi', fourcc, 20.0, (320,240))

while(cap.isOpened()):
    ret, frame = cap.read()
    ret = cap.set(3,320) 
    ret = cap.set(4,240)

    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(24) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()