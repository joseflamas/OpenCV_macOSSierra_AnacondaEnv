import numpy as np
import cv2
from matplotlib import pyplot as plt

# WORKING WITH IMAGES - COLOR DIFFERENCES BETWEEN MATPLOT AND 
# OpenCV follows BGR order, while matplotlib likely follows RGB order.

images_data_path = '/Users/memo/_sublime/OpenCV/tests/data/images/'

#display using matplot
img = cv2.imread( images_data_path + 'flor.png')
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])
plt.subplot(121);plt.imshow(img) # expects distorted color
plt.subplot(122);plt.imshow(img2) # expect true color
plt.show()

cv2.imshow('bgr image',img) # expects true color
cv2.imshow('rgb image',img2) # expects distorted color
cv2.imwrite( images_data_path + 'florMatPlotDissorted.png', img2 ) 
cv2.waitKey(0)
cv2.destroyAllWindows()