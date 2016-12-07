import glob
import os
from skimage.feature import hog
from skimage.io import imread
import matplotlib.pyplot as plt
from config import *
from random import shuffle
from sklearn.externals import joblib


def pos_and_neg_paths(n_negative_images, n_negative_categories, category_to_test):
    pos_paths = []
    neg_paths = []
    negative_categorie_number = 0
    categories_paths = glob.glob(os.path.join(TRAINING_PATH, "*"))
    for category_path in categories_paths:
        category_name = os.path.split(category_path)[1]
        if category_name == category_to_test:
            for im_path in glob.glob(os.path.join(category_path, "*")):
                pos_paths.append(im_path)
            break
    shuffle(categories_paths)
    for category_path in categories_paths:
        if negative_categorie_number == n_negative_categories:
            break
        category_name = os.path.split(category_path)[1]
        if category_name == category_to_test:
            continue
        ims_paths = glob.glob(os.path.join(category_path, "*"))
        shuffle(ims_paths)
        ims_paths = ims_paths[:n_negative_images]
        for im_path in ims_paths:
            neg_paths.append(im_path)
        negative_categorie_number += 1
    for i in pos_paths:
        print i
    print "---------------------------------------------------------------------------------------"
    for i in neg_paths:
        print i
    return pos_paths, neg_paths


# MAL RESULTADO AL USAR UNAS POCAS CATEGORIAS COMO NEGATIVAS

def pos_and_neg_paths_using_all(n_negative_images, category_to_test):
    pos_paths = []
    neg_paths = []
    categories_paths = glob.glob(os.path.join(TRAINING_PATH, "*"))
    for category_path in categories_paths:
        category_name = os.path.split(category_path)[1]
        if category_name == category_to_test:
            for im_path in glob.glob(os.path.join(category_path, "*")):
                pos_paths.append(im_path)
            break
    for category_path in categories_paths:
        category_name = os.path.split(category_path)[1]
        if category_name == category_to_test:
            continue
        ims_paths = glob.glob(os.path.join(category_path, "*"))
        shuffle(ims_paths)
        ims_paths = ims_paths[:n_negative_images]
        for im_path in ims_paths:
            neg_paths.append(im_path)
    for i in pos_paths:
        print i
    print "---------------------------------------------------------------------------------------"
    for i in neg_paths:
        print i
    return pos_paths, neg_paths

# MEJOR RESULTADO AL USAR TODAS LAS CATEGORIAS CON CIERTO NUMEOR DE IMAGENES


def pos_and_neg_paths_using_specific(negative_categories, n_negative_images, category_to_test):
    pos_paths = []
    neg_paths = []
    categories_paths = glob.glob(os.path.join(TRAINING_PATH, "*"))
    for category_path in categories_paths:
        category_name = os.path.split(category_path)[1]
        if category_name == category_to_test:
            for im_path in glob.glob(os.path.join(category_path, "*")):
                pos_paths.append(im_path)
            break
    for category_path in categories_paths:
        category_name = os.path.split(category_path)[1]
        if category_name == category_to_test:
            continue
        if category_name in negative_categories:
            ims_paths = glob.glob(os.path.join(category_path, "*"))
            shuffle(ims_paths)
            ims_paths = ims_paths[:n_negative_images]
            for im_path in ims_paths:
                neg_paths.append(im_path)
    for i in pos_paths:
        print i
    print "---------------------------------------------------------------------------------------"
    for i in neg_paths:
        print i
    return pos_paths, neg_paths


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
        fd, hog_image = hog(im, ORIENTATIONS, PIXELS_PER_CELL, CELLS_PER_BLOCK, True, False)
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

positive_paths, negative_paths = pos_and_neg_paths_using_specific(['butterfly','barrel','cannon'],20,'sunflower')
#'''
print "Calculating and saving the positive descriptors"
extract(positive_paths, POSITIVE_FEATURES_OUTPUT_PATH)
print "Positive features saved in {}".format(POSITIVE_FEATURES_OUTPUT_PATH)
print "Calculating and saving the negative descriptors"
extract(negative_paths, NEGATIVE_FEATURES_OUTPUT_PATH)
print "Negative features saved in {}".format(NEGATIVE_FEATURES_OUTPUT_PATH)
print "Completed calculating features from training images"
#'''