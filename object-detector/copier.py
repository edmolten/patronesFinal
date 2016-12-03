
import glob
import os
from PIL import Image
from config import *
from random import shuffle

for folder_path in glob.glob(os.path.join(SQUARE_DATASET_PATH, "*")):
    category = os.path.split(folder_path)[1]
    '''
    trainig_output_path = "{}/{}/".format(TRAINING_PATH, category)
    testing_output_path = "{}/{}/".format(TESTING_PATH, category)
    if not os.path.isdir(trainig_output_path):
        os.mkdir(trainig_output_path)
    if not os.path.isdir(testing_output_path):
        os.mkdir(testing_output_path)'''
    paths = []
    for image_path in glob.glob(os.path.join(folder_path, "*.pgm")):
        paths.append(image_path)
    shuffle(paths)
    path_number = len(paths)
    training_number = int(path_number * 0.8)
    print("ALL: " + str(paths))
    print("size : " + str(len(paths)))
    print("TRAINING: " + str(paths[:training_number]))
    print("size : " + str(len(paths[:training_number])))
    print("TESTING: " + str(paths[training_number:]))
    print("size : " + str(len(paths[training_number:])))
