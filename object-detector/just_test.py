#!/usr/bin/python
import os
from config import *

os.system("{} {}object-detector/test-classifier.py -i {} --visualize".format(ANACONDA_PATH, PROJECT_PATH, TEST_IMAGE_PATH))
