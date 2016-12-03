import os
import glob
from PIL import Image
PATH = "C:/Users/eddox/Downloads/101_ObjectCategories/accordion"
for im_path in glob.glob(os.path.join(PATH, "*.jpg")):
    name = im_path.split(".")[0]
    im = Image.open(im_path)
   # im = im.convert('RGB')
    im.save(name+".pgm")