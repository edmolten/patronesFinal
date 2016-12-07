from sklearn.svm import LinearSVC
from sklearn.externals import joblib
import glob
import os
from config import *

fds = []
labels = []

print "Loading the positive features"
for feat_path in glob.glob(os.path.join(POSITIVE_FEATURES_OUTPUT_PATH, "*.feat")):
    fd = joblib.load(feat_path)
    fds.append(fd)
    labels.append(1)

print "Loading the negative features"
for feat_path in glob.glob(os.path.join(NEGATIVE_FEATURES_OUTPUT_PATH, "*.feat")):
    fd = joblib.load(feat_path)
    fds.append(fd)
    labels.append(0)

clf = LinearSVC()
print "Training a Linear SVM Classifier"
clf.fit(fds, labels)
# If model directorie don't exist, create them
if not os.path.isdir(os.path.split(MODEL_PATH)[0]):
    os.makedirs(os.path.split(MODEL_PATH)[0])
joblib.dump(clf, MODEL_PATH)
print "Classifier saved to {}".format(MODEL_PATH)
