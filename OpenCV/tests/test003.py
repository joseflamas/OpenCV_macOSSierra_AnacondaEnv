import numpy as np
import cv2
from matplotlib import pyplot as plt

# WORKING WITH IMAGES 

images_data_path = '/Users/memo/_sublime/OpenCV/tests/data/images/'

#display using matplot
img = cv2.imread( images_data_path + 'flor.png' ,0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()