from sklearn.svm import LinearSVC
from sklearn.externals import joblib
import argparse as ap
import glob
import os
from config import *

if __name__ == "__main__":
    # Parse the command line arguments
    parser = ap.ArgumentParser()
    parser.add_argument('-p', "--posfeat", help="Path to the positive features directory", required=True)
    parser.add_argument('-n', "--negfeat", help="Path to the negative features directory", required=True)
    args = vars(parser.parse_args())

    pos_feat_path =  args["posfeat"]
    neg_feat_path = args["negfeat"]

    fds = []
    labels = []
    # Load the positive features
    for feat_path in glob.glob(os.path.join(pos_feat_path,"*.feat")):
        fd = joblib.load(feat_path)
        fds.append(fd)
        labels.append(1)

    # Load the negative features
    for feat_path in glob.glob(os.path.join(neg_feat_path,"*.feat")):
        fd = joblib.load(feat_path)
        fds.append(fd)
        labels.append(0)
    for x in fds:
        print len(x)
    clf = LinearSVC()
    print "Training a Linear SVM Classifier"
    clf.fit(fds, labels)
    # If model directorie don't exist, create them
    if not os.path.isdir(os.path.split(MODEL_PATH)[0]):
        os.makedirs(os.path.split(MODEL_PATH)[0])
    joblib.dump(clf, MODEL_PATH)
    print "Classifier saved to {}".format(MODEL_PATH)
