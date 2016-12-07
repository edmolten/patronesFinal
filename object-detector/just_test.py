#!/usr/bin/python
import os
from config import *

os.system("{} {}object-detector/test.py -i {} --visualize".format(ANACONDA_PATH, PROJECT_PATH, TEST_IMAGE_PATH))
