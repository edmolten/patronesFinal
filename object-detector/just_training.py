#!/usr/bin/python
import os
from config import *

os.system("{} {}/object-detector/train.py".format(ANACONDA_PATH, PROJECT_PATH))
