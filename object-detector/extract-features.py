from skimage.feature import hog
from skimage.io import imread
from sklearn.externals import joblib
import glob
import os
from config import *


def pos_and_neg_paths():
    pos_paths = []
    neg_paths = []
    for folder_path in glob.glob(os.path.join(TRAINING_PATH, "*")):
        category = os.path.split(folder_path)[1]
        if category == CATEGORY_TO_TEST:
            for im_path in glob.glob(os.path.join(folder_path, "*")):
                pos_paths.append(im_path)
        else:
            for im_path in glob.glob(os.path.join(folder_path, "*")):
                neg_paths.append(im_path)
    return pos_paths,neg_paths


def extract(input_paths, output_path):
    for im_path in input_paths:
        im = imread(im_path, as_grey=True)
        fd = hog(im, ORIENTATIONS, PIXELS_PER_CELL, CELLS_PER_BLOCK, VISUALIZE, NORMALIZE)
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(output_path, fd_name)
        joblib.dump(fd, fd_path)

# Create directories if don't exist
if not os.path.isdir(POSITIVE_FEATURES_OUTPUT_PATH):
    os.makedirs(POSITIVE_FEATURES_OUTPUT_PATH)
if not os.path.isdir(NEGATIVE_FEATURES_OUTPUT_PATH):
    os.makedirs(NEGATIVE_FEATURES_OUTPUT_PATH)

positive_paths,negative_paths = pos_and_neg_paths()
print "Calculating and saving the positive descriptors"
extract(positive_paths,POSITIVE_FEATURES_OUTPUT_PATH)
print "Positive features saved in {}".format(POSITIVE_FEATURES_OUTPUT_PATH)
print "Calculating and saving the negative descriptors"
extract(negative_paths,NEGATIVE_FEATURES_OUTPUT_PATH)
print "Negative features saved in {}".format(NEGATIVE_FEATURES_OUTPUT_PATH)
print "Completed calculating features from training images"


'''
print "Calculating and saving the positive descriptors"
for im_path in glob.glob(os.path.join(pos_im_path, "*.pgm")):
    im = imread(im_path, as_grey=True)
    fd = hog(im, ORIENTATIONS, PIXELS_PER_CELL, CELLS_PER_BLOCK, VISUALIZE, NORMALIZE)
    fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
    fd_path = os.path.join(POSITIVE_FEATURES_OUTPUT_PATH, fd_name)
    joblib.dump(fd, fd_path)
print "Positive features saved in {}".format(POSITIVE_FEATURES_OUTPUT_PATH)
print "Calculating and saving the negative descriptors"
for im_path in glob.glob(os.path.join(neg_im_path, "*.pgm")):
    im = imread(im_path, as_grey=True)
    fd = hog(im,  ORIENTATIONS, PIXELS_PER_CELL, CELLS_PER_BLOCK, VISUALIZE, NORMALIZE)
    fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
    fd_path = os.path.join(NEGATIVE_FEATURES_OUTPUT_PATH, fd_name)
    joblib.dump(fd, fd_path)
print "Negative features saved in {}".format(NEGATIVE_FEATURES_OUTPUT_PATH)
print "Completed calculating features from training images"
'''
