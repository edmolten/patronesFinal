#!/usr/bin/python
import os
from config import *

os.system("{} {}/object-detector/train-classifier.py".format(ANACONDA_PATH, PROJECT_PATH))