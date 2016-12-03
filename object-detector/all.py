#!/usr/bin/python
import os
from config import *

# 1) Extract features
os.system("{} {}object-detector/extract-features.py -p {} -n {}".format(ANACONDA_PATH, PROJECT_PATH, POSITIVE_DATA_PATH, NEGATIVE_DATA_PATH))

# 2) Perform training
os.system("{} {}object-detector/train-classifier.py -p {} -n {}".format(ANACONDA_PATH, PROJECT_PATH, POSITIVE_FEATURES_OUTPUT_PATH, NEGATIVE_FEATURES_OUTPUT_PATH))

# 3) Perform testing
os.system("{} {}object-detector/test-classifier.py -i {} --visualize".format(ANACONDA_PATH, PROJECT_PATH, TEST_IMAGE_PATH))
