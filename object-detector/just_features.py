#!/usr/bin/python
import os
from config import *

os.system("{} {}object-detector/extract-features.py".format(ANACONDA_PATH, PROJECT_PATH))