import glob
import os
from PIL import Image
paths = []
IMAGES_PATH = "C:/Users/eddox/Desktop/SquareDataSet/airplanes"

for im_path in glob.glob(os.path.join(IMAGES_PATH,"*")):
    paths.append(im_path)

def create_collage():
    cols = 80
    rows = 10
    collage = Image.new('RGB', (80*150, 10*150))
    i = 0
    x = 0
    y = 0
    for col in range(cols):
        for row in range(rows):
            print(i, x, y)
            image = Image.open(paths[i])
            collage.paste(image, (x, y))
            image.close()
            i += 1
            y += 150
        x += 150
        y = 0

    collage.save("C:/Users/eddox/Desktop/SquareDataSet/airplanes/Collage.jpg")

#create_collage()
