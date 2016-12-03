#!/usr/bin/python
import os
from config import *

# 1) Extract features
os.system("{} {}object-detector/extract-features.py -p {} -n {}".format(ANACONDA_PATH, PROJECT_PATH, POSITIVE_DATA_PATH, NEGATIVE_DATA_PATH))

# 2) Perform training
os.system("{} {}/object-detector/train-classifier.py -p {} -n {}".format(ANACONDA_PATH, PROJECT_PATH, POSITIVE_FEATURES_OUTPUT_PATH, NEGATIVE_FEATURES_OUTPUT_PATH))

# Perform testing
test_im_path = "C:/Users/eddox/Downloads/CarData/TestImages/test-16.pgm"
os.system("C:/Users/eddox/Anaconda/python.exe C:/Users/eddox/Documents/object-detector/object-detector/test-classifier.py -i {} --visualize".format(test_im_path))
