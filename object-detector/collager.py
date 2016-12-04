import glob
import os
from PIL import Image
from config import *
from random import shuffle

paths = []
for folder_path in glob.glob(os.path.join(TESTING_PATH, "*")):
    category = os.path.split(folder_path)[1]
    category_paths = []
    for im_path in glob.glob(os.path.join(folder_path,"*")):
        category_paths.append(im_path)
    shuffle(category_paths)
    for i in range(IMAGES_PER_CATEGORY):
        paths.append(category_paths[i])
shuffle(paths)
created_collages_paths = glob.glob(os.path.join(COLLAGES_PATH, "*.jpg"))
name = "?"
if len(created_collages_paths) == 0:
    name = "1"
else:
    last_path = created_collages_paths[-1]
    name = str(int(os.path.split(last_path)[1].split(".")[0]) + 1)

collage = Image.new('RGB', (IMAGES_WIDTH*COLUMNS, IMAGES_HEIGHT*ROWS))
i = 0
x = 0
y = 0
stop = IMAGES_PER_CATEGORY * CATEGORIES
for col in range(COLUMNS):
    if i == stop:
        break
    for row in range(ROWS):
        if i == stop:
            break
        image = Image.open(paths[i])
        collage.paste(image, (x, y))
        image.close()
        i += 1
        y += IMAGES_HEIGHT
    x += IMAGES_WIDTH
    y = 0

collage.save("{}/{}.jpg".format(COLLAGES_PATH, name))

