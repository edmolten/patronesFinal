from skimage.io import imread
from skimage.feature import hog
from sklearn.externals import joblib
import cv2
from config import *


def sliding_window(image, window_size, step_size):
    for y in xrange(0, image.shape[0], step_size[1]):
        for x in xrange(0, image.shape[1], step_size[0]):
            yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])

try:
    im = imread(TEST_IMAGE_PATH, as_grey=True)
except IOError:
    print "ERROR: No .pgm file, Dont forget to generate it from the collage"
    exit()

classifier = joblib.load(MODEL_PATH)
detections = []
for (x, y, im_window) in sliding_window(im, WINDOW_SIZE, STEP_SIZE):
    # Calculate the HOG features
    fd = hog(im_window, ORIENTATIONS, PIXELS_PER_CELL, CELLS_PER_BLOCK, False, NORMALIZE)
    pred = classifier.predict(fd)
    if pred == 1:
        print "Detection:: Location -> ({}, {})".format(x, y)
        print "Confidence Score {} \n".format(classifier.decision_function(fd))
        detections.append((x, y))
    if VISUALIZE:
        clone = im.copy()
        for x1, y1 in detections:
            cv2.rectangle(clone,
                          (x1, y1),
                          (x1 + WINDOW_SIZE[0], y1 + WINDOW_SIZE[1]),
                          (0.5, 0.5, 0.5),
                          thickness=4)
        cv2.rectangle(clone, (x, y), (x + im_window.shape[1], y +
                                      im_window.shape[0]), (255, 0, 0), thickness=4)
        cv2.imshow("Sliding Window in Progress", clone)
        cv2.waitKey(10)
cv2.waitKey()
