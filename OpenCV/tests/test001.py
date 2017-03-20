import numpy as np
import cv2
from matplotlib import pyplot as plt

# WORKING WITH IMAGES     LOAD - DISPLAY - WRITE

images_data_path = '/Users/memo/_sublime/OpenCV/tests/data/images/'

#load color image in greyscale
img = cv2.imread( images_data_path + 'flor.png', 0 )

#display
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#write
cv2.imwrite( images_data_path + 'florGris.png', img ) 


