#!/usr/bin/python
import os
from config import *

os.system("{} {}/object-detector/train-classifier.py -p {} -n {}".format(ANACONDA_PATH, PROJECT_PATH, POSITIVE_FEATURES_OUTPUT_PATH, NEGATIVE_FEATURES_OUTPUT_PATH))

# -p C:/Users/eddox/Documents/object-detector/data/features/pos -n C:/Users/eddox/Documents/object-detector/data/features/neg