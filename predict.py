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

import sys
if len(sys.argv) == 2:
    nparray = sys.argv[1]
    prediction = int ( clf.predict( [nparray] )[0] )
    print(mdataset[prediction])
else:
    print("Failure")
