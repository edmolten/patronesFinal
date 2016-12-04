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
ROWS = 10
COLUMNS = 11

# --- This options are not used at once
NEGATIVE_CATEGORIES_LIMIT = 2
NEGATIVE_IMAGES_PER_CATERGORY = 5
# ------

MIN_WINDOW_SIZE = [150, 150]
STEP_SIZE = [150, 150]
ORIENTATIONS = 8
PIXELS_PER_CELL = [5, 5]
CELLS_PER_BLOCK = [5, 5]
VISUALIZE = True
NORMALIZE = True
THRESHOLD = 0.3
DOWNSCALE = 2

CATEGORY_TO_TEST = "barrel"
COLLAGE_NUMBER_TO_TEST = 8
TEST_IMAGE_PATH = COLLAGES_PATH + "/" + str(COLLAGE_NUMBER_TO_TEST) + ".pgm"
