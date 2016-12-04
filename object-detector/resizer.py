import glob
import os
from PIL import Image
from config import *

for folder_path in glob.glob(os.path.join(ORIGINAL_DATASET_PATH, "*")):
    category = os.path.split(folder_path)[1]
    output_path = "{}/{}/".format(SQUARE_DATASET_PATH, category)
    if not os.path.isdir(output_path):
        os.mkdir(output_path)
    for image_path in glob.glob(os.path.join(folder_path, "*.jpg")):
        name = os.path.split(image_path)[1]
        image = Image.open(image_path)
        image = image.resize((150, 150), Image.LANCZOS)
        image.save("{}/{}".format(output_path, name))
        image.close()
