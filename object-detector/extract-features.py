from skimage.feature import hog
from skimage.io import imread
from sklearn.externals import joblib
import argparse as ap
import glob
import os
from config import *

if __name__ == "__main__":

    # Parsing args
    parser = ap.ArgumentParser()
    parser.add_argument('-p', "--pospath", help="Path to positive images",
            required=True)
    parser.add_argument('-n', "--negpath", help="Path to negative images",
            required=True)
    args = vars(parser.parse_args())
    pos_im_path = args["pospath"]
    neg_im_path = args["negpath"]

    # Create directories if don't exist
    if not os.path.isdir(POSITIVE_FEATURES_OUTPUT_PATH):
        os.makedirs(POSITIVE_FEATURES_OUTPUT_PATH)
    if not os.path.isdir(NEGATIVE_FEATURES_OUTPUT_PATH):
        os.makedirs(NEGATIVE_FEATURES_OUTPUT_PATH)


    print "Calculating and saving the positive descriptors"
    for im_path in glob.glob(os.path.join(pos_im_path, "*.pgm")):
        im = imread(im_path, as_grey=True)
        fd = hog(im, orientations, pixels_per_cell, cells_per_block, visualize, normalize)
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(POSITIVE_FEATURES_OUTPUT_PATH, fd_name)
        joblib.dump(fd, fd_path)
    print "Positive features saved in {}".format(POSITIVE_FEATURES_OUTPUT_PATH)
    print "Calculating and saving the negative descriptors"
    for im_path in glob.glob(os.path.join(neg_im_path, "*.pgm")):
        im = imread(im_path, as_grey=True)
        fd = hog(im,  orientations, pixels_per_cell, cells_per_block, visualize, normalize)
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(NEGATIVE_FEATURES_OUTPUT_PATH, fd_name)
        joblib.dump(fd, fd_path)
    print "Negative features saved in {}".format(NEGATIVE_FEATURES_OUTPUT_PATH)
    print "Completed calculating features from training images"
