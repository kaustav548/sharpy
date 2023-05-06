import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type = str, required=True,
    help="path to input image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
image_sharp = cv2.filter2D(img , ddepth=-1, kernel=kernel)
cv2.imshow('original',img)
cv2.imshow('img', image_sharp)
cv2.waitKey(0)
cv2.destroyAllWindows()