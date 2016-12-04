from skimage.feature import hog
from skimage.io import imread
from sklearn.externals import joblib
import glob
import os
from config import *


def pos_and_neg_paths():
    pos_paths = []
    neg_paths = []
    current_negative_category = 0
    for folder_path in glob.glob(os.path.join(TRAINING_PATH, "*")):
        category = os.path.split(folder_path)[1]
        if category == CATEGORY_TO_TEST:
            for im_path in glob.glob(os.path.join(folder_path, "*")):
                pos_paths.append(im_path)
        else:
            if current_negative_category != NEGATIVE_CATEGORIES_LIMIT:
                for im_path in glob.glob(os.path.join(folder_path, "*")):
                    neg_paths.append(im_path)
                current_negative_category += 1
    return pos_paths,neg_paths
#MAL RESULTADO AL USAR UNAS POCAS CATEGORIAS COMO NEGATIVAS

def pos_and_neg_paths_using_all():
    pos_paths = []
    neg_paths = []
    for folder_path in glob.glob(os.path.join(TRAINING_PATH, "*")):
        category = os.path.split(folder_path)[1]
        if category == CATEGORY_TO_TEST:
            for im_path in glob.glob(os.path.join(folder_path, "*")):
                pos_paths.append(im_path)
        else:
            current_negative_paths = glob.glob(os.path.join(folder_path, "*"))
            if(len(current_negative_paths)>NEGATIVE_IMAGES_PER_CATERGORY):
                current_negative_paths = current_negative_paths[:NEGATIVE_IMAGES_PER_CATERGORY]
            for im_path in current_negative_paths:
                neg_paths.append(im_path)
    return pos_paths,neg_paths

import matplotlib.pyplot as plt
from skimage import data, color, exposure

def extract(input_paths, output_path):
    i = 0
    for im_path in input_paths:
        im = imread(im_path, as_grey=True)

        fd = hog(im, ORIENTATIONS, PIXELS_PER_CELL, CELLS_PER_BLOCK, False, NORMALIZE)
        fd_name = os.path.split(im_path)[1].split(".")[0] + ".feat"
        fd_path = os.path.join(output_path, str(i) + fd_name)
        joblib.dump(fd, fd_path)
        i += 1
'''
        fd, hog_image = hog(im, ORIENTATIONS, PIXELS_PER_CELL, CELLS_PER_BLOCK, True, NORMALIZE)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4), sharex=True, sharey=True)

        ax1.axis('off')
        ax1.imshow(im, cmap=plt.cm.gray)
        ax1.set_title('Input image')
        ax1.set_adjustable('box-forced')

        ax2.axis('off')
        ax2.imshow(hog_image, cmap=plt.cm.gray)
        ax2.set_title('Histogram of Oriented Gradients')
        ax1.set_adjustable('box-forced')
        plt.show()
'''

# Create directories if don't exist
if not os.path.isdir(POSITIVE_FEATURES_OUTPUT_PATH):
    os.makedirs(POSITIVE_FEATURES_OUTPUT_PATH)
if not os.path.isdir(NEGATIVE_FEATURES_OUTPUT_PATH):
    os.makedirs(NEGATIVE_FEATURES_OUTPUT_PATH)

positive_paths,negative_paths = pos_and_neg_paths_using_all()
print "Calculating and saving the positive descriptors"
extract(positive_paths,POSITIVE_FEATURES_OUTPUT_PATH)
print "Positive features saved in {}".format(POSITIVE_FEATURES_OUTPUT_PATH)
print "Calculating and saving the negative descriptors"
extract(negative_paths,NEGATIVE_FEATURES_OUTPUT_PATH)
print "Negative features saved in {}".format(NEGATIVE_FEATURES_OUTPUT_PATH)
print "Completed calculating features from training images"
