#!/usr/bin/python
import os
from config import *

# 1) Extract features
os.system("{} {}object-detector/extract.py".format(ANACONDA_PATH, PROJECT_PATH))

# 2) Perform training
os.system("{} {}object-detector/train.py".format(ANACONDA_PATH, PROJECT_PATH))

# 3) Perform testing
os.system("{} {}object-detector/test.py".format(ANACONDA_PATH, PROJECT_PATH))
