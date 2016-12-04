import glob
import os
from PIL import Image
from config import *
from random import shuffle


def get_random_images_routes(n_categories, n_images, include):
    paths = []
    categories_paths = glob.glob(os.path.join(TESTING_PATH, "*"))
    include_path = "?"
    for path in categories_paths:
        if include == os.path.split(path)[1]:
            include_path = path
            categories_paths.remove(include_path)
    shuffle(categories_paths)
    categories_paths = categories_paths[:n_categories - 1]
    categories_paths.append(include_path)
    shuffle(categories_paths)
    for folder_path in categories_paths:
        this_category_images_paths = []
        for im_path in glob.glob(os.path.join(folder_path, "*")):
            this_category_images_paths.append(im_path)
        shuffle(this_category_images_paths)
        this_category_images_paths = this_category_images_paths[:n_images]
        for route in this_category_images_paths:
            paths.append(route)
    shuffle(paths)
    return paths


def create_collage(paths, n_categories, n_images):
    created_collages_paths = glob.glob(os.path.join(COLLAGES_PATH, "*.jpg"))
    if len(created_collages_paths) == 0:
        name = "1"
    else:
        last_path = created_collages_paths[-1]
        name = str(int(os.path.split(last_path)[1].split(".")[0]) + 1)
    collage = Image.new('RGB', (IMAGES_WIDTH * n_categories, IMAGES_HEIGHT * n_images))
    i = 0
    x = 0
    y = 0
    stop = n_categories * n_images
    for col in range(n_categories):
        if i == stop:
            break
        for row in range(n_images):
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


n_categories = 4
n_images = 6
category = "ant"
paths = get_random_images_routes(n_categories, n_images, category)
create_collage(paths, n_categories, n_images)
