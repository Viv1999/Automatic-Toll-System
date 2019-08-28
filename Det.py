import numpy as np
import cv2
import argparse

#save_folder = 'vivek\\ATTS'

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True, help="path to image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
while True:
    cv2.imshow('originalImage',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cv2.destroyAllWindows()