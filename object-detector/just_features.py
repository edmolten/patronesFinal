#!/usr/bin/python
import os
from config import *

os.system("{} {}object-detector/extract-features.py -p {} -n {}".format(ANACONDA_PATH, PROJECT_PATH, POSITIVE_DATA_PATH, NEGATIVE_DATA_PATH))
