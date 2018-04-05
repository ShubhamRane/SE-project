import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split, GridSearchCV

mdataset = ['apple', 'axe', 'hat', 'butterfly', 'fan']

### store the classifier
import pickle
clf = pickle.load(open('clf_rf.pickle', 'r'))

from convert import test
path = "/path/to/image";
x = test.imageprepare(path);

import sys
if len(sys.argv) == 2:
    #path of the uploaded image as given by php
    path = sys.argv[1]
    #convert to array of 784
    x = test.imageprepare(path)
    #predict the value and find the name of object
    prediction = int ( clf.predict( [x] )[0] )
    print(mdataset[prediction])
else:
    print("Failure")
