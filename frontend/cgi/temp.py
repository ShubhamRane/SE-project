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

mdataset = ['axe', 'fan', 'butterfly', 'hat', 'apple']
mdata_objects = []
### load the data
for index, value in enumerate(mdataset):	
    data_object = np.load('data/full_numpy_bitmap_' + value + '.npy')
    data_object = np.c_[data_object, np.full(len(data_object), index)]
    data_object = data_object[:5000]
    mdata_objects.append(data_object)

### data information

def plot_samples(input_array, rows=4, cols=5, title=''):
    '''
    Function to plot 28x28 pixel drawings that are stored in a numpy array.
    Specify how many rows and cols of pictures to display (default 4x5).  
    If the array contains less images than subplots selected, surplus subplots remain empty.
    '''
    
    fig, ax = plt.subplots(figsize=(cols,rows))
    ax.axis('off')
    plt.title(title)

    for i in list(range(0, min(len(input_array),(rows*cols)) )):      
        a = fig.add_subplot(rows,cols,i+1)
        imgplot = plt.imshow(input_array[i,:784].reshape((28,28)), cmap='gray_r', interpolation='nearest')
        plt.xticks([])
        plt.yticks([])
    plt.show()

import itertools

def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = np.round(cm.astype('float') / cm.sum(axis=1)[:, np.newaxis], 5)
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')

### see sample images via a plot
### plot_samples(apple, title='Sample apple drawings\n')
### plot_samples(hat, title='Sample apple drawings\n')
# merge the apple and hat arrays, and split the features (X) and labels (y). Convert to float32 to save some memory.
X_data = []
y_data = []
for data_object in mdata_objects:
    X_data.append(data_object[:5000,:-1])
    y_data.append(data_object[:5000,-1])
X_data = tuple(X_data)
y_data = tuple(y_data)

X = np.concatenate(X_data, axis=0).astype('float32') # all columns but the last
y = np.concatenate(y_data, axis=0).astype('float32') # the last column

# train/test split (divide by 255 to obtain normalized values between 0 and 1)
# I will use a 50:50 split, since I want to start by training the models on 5'000 samples and thus have plenty of samples to spare for testing.
X_train, X_test, y_train, y_test = train_test_split(X/255., y, test_size=0.5, random_state=0)


import sys
if len(sys.argv) == 2 and sys.argv[1] == "train":
    clf = RandomForestClassifier(n_jobs=-1)
    clf.fit(X_train, y_train)
else:
    import pickle
    clf = pickle.load(open('clf_rf.pickle','r'))

y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print ('Accuracy: ',acc)
#print clf.predict([X_test[4000]])
#print y_test[4000]

### store the classifier
import pickle
pickle.dump(clf, open('clf_rf_temp.pickle', 'wb'))
