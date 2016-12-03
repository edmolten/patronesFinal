import ConfigParser as cp
import json

#Routes
ANACONDA_PATH = "C:/Users/eddox/Anaconda/python.exe"
PROJECT_PATH = "C:/Users/eddox/Documents/object-detector/"
ORIGINAL_DATASET_PATH = "C:/Users/eddox/Downloads/101_ObjectCategories"
SQUARE_DATASET_PATH = "C:/Users/eddox/Desktop/SquareDataSet"
TRAINING_PATH = "C:/Users/eddox/Desktop/Training"
TESTING_PATH = "C:/Users/eddox/Desktop/Testing"
working = False

if working:
    DATA_PATH = "C:/Users/eddox/Downloads/CarData/"
    POSITIVE_DATA_PATH = DATA_PATH + "pos"
    NEGATIVE_DATA_PATH = DATA_PATH + "neg"
    TEST_IMAGE_PATH = "C:/Users/eddox/Downloads/CarData/TestImages/test-16.pgm"
    POSITIVE_FEATURES_OUTPUT_PATH = PROJECT_PATH + "data/features/pos"
    NEGATIVE_FEATURES_OUTPUT_PATH = PROJECT_PATH + "data/features/neg"
else:
    DATA_PATH = "C:/Users/eddox/Desktop"
    POSITIVE_DATA_PATH = DATA_PATH + "/accordion"
    NEGATIVE_DATA_PATH = DATA_PATH + "/brontosaurus"
    TEST_IMAGE_PATH = "C:\Users\eddox\Desktop\image_0013.pgm"
    POSITIVE_FEATURES_OUTPUT_PATH = PROJECT_PATH + "data/features/pos2"
    NEGATIVE_FEATURES_OUTPUT_PATH = PROJECT_PATH + "data/features/neg2"

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
