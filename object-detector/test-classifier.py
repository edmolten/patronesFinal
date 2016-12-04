from skimage.transform import pyramid_gaussian
from skimage.io import imread
from skimage.feature import hog
from sklearn.externals import joblib
import cv2
from nms import nms
from config import *


def sliding_window(image, window_size, step_size):
    '''
    This function returns a patch of the input image `image` of size equal
    to `window_size`. The first image returned top-left co-ordinates (0, 0) 
    and are increment in both x and y directions by the `step_size` supplied.
    So, the input parameters are -
    * `image` - Input Image
    * `window_size` - Size of Sliding Window
    * `step_size` - Incremented Size of Window

    The function returns a tuple -
    (x, y, im_window)
    where
    * x is the top-left x co-ordinate
    * y is the top-left y co-ordinate
    * im_window is the sliding window image
    '''
    for y in xrange(0, image.shape[0], step_size[1]):
        for x in xrange(0, image.shape[1], step_size[0]):
            yield (x, y, image[y:y + window_size[1], x:x + window_size[0]])



# Read the image
im = imread(TEST_IMAGE_PATH, as_grey=True)

# Load the classifier
clf = joblib.load(MODEL_PATH)

# List to store the detections
detections = []
# The current scale of the image
scale = 0
# Downscale the image and iterate
for im_scaled in pyramid_gaussian(im, downscale=DOWNSCALE):
    # This list contains detections at the current scale
    cd = []
    # If the width or height of the scaled image is less than
    # the width or height of the window, then end the iterations.
    if im_scaled.shape[0] < MIN_WINDOW_SIZE[1] or im_scaled.shape[1] < MIN_WINDOW_SIZE[0]:
        break
    for (x, y, im_window) in sliding_window(im_scaled, MIN_WINDOW_SIZE, STEP_SIZE):
        if im_window.shape[0] != MIN_WINDOW_SIZE[1] or im_window.shape[1] != MIN_WINDOW_SIZE[0]:
            continue
        # Calculate the HOG features
        fd = hog(im_window, ORIENTATIONS, PIXELS_PER_CELL, CELLS_PER_BLOCK, False, NORMALIZE)
        pred = clf.predict(fd)
        if pred == 1:
            print  "Detection:: Location -> ({}, {})".format(x, y)
            print "Scale ->  {} | Confidence Score {} \n".format(scale,clf.decision_function(fd))
            detections.append((x, y, clf.decision_function(fd),
                int(MIN_WINDOW_SIZE[0]*(DOWNSCALE**scale)),
                int(MIN_WINDOW_SIZE[1]*(DOWNSCALE**scale))))
            cd.append(detections[-1])
        # If visualize is set to true, display the working
        # of the sliding window
        if VISUALIZE:
            clone = im_scaled.copy()
            for x1, y1, _, _, _  in cd:
                # Draw the detections at this scale
                cv2.rectangle(clone, (x1, y1), (x1 + im_window.shape[1], y1 +
                    im_window.shape[0]), (0, 255, 0), thickness=3)
            cv2.rectangle(clone, (x, y), (x + im_window.shape[1], y +
                im_window.shape[0]), (255, 0, 0), thickness=3)
            cv2.imshow("Sliding Window in Progress", clone)
            cv2.waitKey(30)
    # Move the the next scale
    scale+=1

# Display the results before performing NMS
clone = im.copy()
for (x_tl, y_tl, _, w, h) in detections:
    # Draw the detections
    cv2.rectangle(im, (x_tl, y_tl), (x_tl+w, y_tl+h), (1, 255, 1), thickness=3)
cv2.imshow("Raw Detections before NMS", im)
cv2.waitKey()

# Perform Non Maxima Suppression
detections = nms(detections, THRESHOLD)

# Display the results after performing NMS
for (x_tl, y_tl, _, w, h) in detections:
    # Draw the detections
    cv2.rectangle(clone, (x_tl, y_tl), (x_tl+w,y_tl+h), (0, 255, 0), thickness=3)
cv2.imshow("Final Detections after applying NMS", clone)
cv2.waitKey()
