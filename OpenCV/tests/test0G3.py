import cv2
import numpy as np
from matplotlib import pyplot as plt

images_data_path = '/Users/memo/_sublime/OpenCV/tests/data/images/'


img1 = cv2.imread( images_data_path + 'parte1.png' )
img2 = cv2.imread( images_data_path + 'parte2.png' )

dst = cv2.addWeighted(img1,0.5,img2,0.5,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()