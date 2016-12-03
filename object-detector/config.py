import ConfigParser as cp
import json

#Routes
ANACONDA_PATH = "C:/Users/eddox/Anaconda/python.exe"
PROJECT_PATH = "C:/Users/eddox/Documents/object-detector/"
DATA_PATH = "C:/Users/eddox/Downloads/CarData/data/"
POSITIVE_DATA_PATH = DATA_PATH + "dataset/CarData/pos"
NEGATIVE_DATA_PATH = DATA_PATH + "dataset/CarData/neg"
POSITIVE_FEATURES_OUTPUT_PATH = PROJECT_PATH + "data/features/pos"
NEGATIVE_FEATURES_OUTPUT_PATH = PROJECT_PATH + "data/features/neg"
MODEL_PATH = PROJECT_PATH + "data/models/svm.model"
CONFIG_PATH = PROJECT_PATH + "data/config/config.cfg"

#Get configuration values for hog
config = cp.RawConfigParser()
config.read(CONFIG_PATH)

min_wdw_sz = json.loads(config.get("hog","min_wdw_sz"))
step_size = json.loads(config.get("hog", "step_size"))
orientations = config.getint("hog", "orientations")
pixels_per_cell = json.loads(config.get("hog", "pixels_per_cell"))
cells_per_block = json.loads(config.get("hog", "cells_per_block"))
visualize = config.getboolean("hog", "visualize")
normalize = config.getboolean("hog", "normalize")
threshold = config.getfloat("nms", "threshold")
