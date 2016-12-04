import glob
import os
from config import *
from random import shuffle
from shutil import copyfile

for folder_path in glob.glob(os.path.join(SQUARE_DATASET_PATH, "*")):
    category = os.path.split(folder_path)[1]
    trainig_output_path = "{}/{}".format(TRAINING_PATH, category)
    testing_output_path = "{}/{}".format(TESTING_PATH, category)
    if not os.path.isdir(trainig_output_path):
        os.mkdir(trainig_output_path)
    if not os.path.isdir(testing_output_path):
        os.mkdir(testing_output_path)
    paths = []
    for image_path in glob.glob(os.path.join(folder_path, "*.pgm")):
        paths.append(image_path)
    shuffle(paths)
    path_number = len(paths)
    training_number = int(path_number * 0.8)
    training_paths = paths[:training_number]
    testing_paths = paths[training_number:]
    for path in training_paths:
        name = os.path.split(path)[1]
        copyfile(path, "{}/{}".format(trainig_output_path, name))
    for path in testing_paths:
        name = os.path.split(path)[1]
        copyfile(path, "{}/{}".format(testing_output_path, name))
