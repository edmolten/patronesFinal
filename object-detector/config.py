
ANACONDA_PATH = "C:/Users/eddox/Anaconda/python.exe"
PROJECT_PATH = "C:/Users/eddox/Documents/object-detector/"
ORIGINAL_DATASET_PATH = "C:/Users/eddox/Downloads/101_ObjectCategories"
SQUARE_DATASET_PATH = "C:/Users/eddox/Desktop/SquareDataSet"
TRAINING_PATH = "C:/Users/eddox/Desktop/Training"
TESTING_PATH = "C:/Users/eddox/Desktop/Testing"
COLLAGES_PATH = "C:/Users/eddox/Desktop/Collages"
POSITIVE_FEATURES_OUTPUT_PATH = "C:\Users\eddox\Desktop/Features/pos"
NEGATIVE_FEATURES_OUTPUT_PATH = "C:\Users\eddox\Desktop/Features/neg"
MODEL_PATH = "C:\Users\eddox\Desktop/Model/model"

IMAGES_WIDTH = 150
IMAGES_HEIGHT = 150
IMAGES_PER_CATEGORY = 2
CATEGORIES = 101
ROWS = 10
COLUMNS = 21
NEGATIVE_CATEGORIES_LIMIT = 2

MIN_WINDOW_SIZE = [150, 150]
STEP_SIZE = [150, 150]
ORIENTATIONS = 9
PIXELS_PER_CELL = [8, 8]
CELLS_PER_BLOCK = [3, 3]
VISUALIZE = False
NORMALIZE = True
THRESHOLD = 0.3

CATEGORY_TO_TEST = "bonsai"

working = False
if working:
    TEST_IMAGE_PATH = "C:/Users/eddox/Downloads/CarData/TestImages/test-16.pgm"
else:
    TEST_IMAGE_PATH = "C:\Users\eddox\Desktop\image_0013.pgm"


