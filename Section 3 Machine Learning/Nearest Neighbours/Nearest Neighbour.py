"""
In the basic nearest neighbor classifier, the only thing that matters is the class label of the nearest neighbor. 
But the nearest neighbor may sometimes be noisy or otherwise misleading. 
Therefore, it may be better to also consider the other nearby data points in addition to the nearest neighbor.

This idea leads us to the so called k-nearest neighbor method, where we consider all the k nearest neighbors. 
If k=3, for example, we'd take the three nearest points and choose the class label based on the majority class among them.

The program below uses the library sklearn to create random data. Our input variable X has two features 
(compare to, say, cabin size and cabin price) and our target variable y is binary: it is either 0 or 1 
(again think, for example, "is the cabin awesome or not.")

Complete the following program so that it finds the three nearest data points (k=3) for each of the test data 
points and classifies them based on the majority class among the neighbors. Currently it generates the random data, 
splits it into training and test sets, calculates the distances between each test set items and the training set items, 
but it fails to classify the test set items according to the correct class, setting them all to belong to class 0. 
Instead of looking at just the nearest neighbor's class, it should use three neighbors and pick the majority class 
(the most common) class among the three neighbours, and use that as the class for the test item.
"""
import numpy as np
from sklearn.datasets import make_blobs
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# create random data with two classes
X, Y = make_blobs(n_samples=16, n_features=2, centers=2, center_box=(-2, 2))

# scale the data so that all values are between 0.0 and 1.0
X = MinMaxScaler().fit_transform(X)

# split two data points from the data as test data and
# use the remaining n-2 points as the training data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=2)

# place-holder for the predicted classes
y_predict = np.empty(len(y_test), dtype=np.int64)

# produce line segments that connect the test data points
# to the nearest neighbors for drawing the chart
lines = []

# distance function
def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum = sum + (ai - bi)**2
    return np.sqrt(sum)


def main(X_train, X_test, y_train, y_test):

    global y_predict
    global lines

    k = 3

    for i, test_item in enumerate(X_test):
        # calculate the distances to all training points
        distances = [dist(train_item, test_item) for train_item in X_train]
        y_dict = {distances[x]:y_train[x] for x in range(len(y_train))}
        neighbours = sorted(distances)[:k]
        y_sorted = [y_dict[neigh] for neigh in neighbours]
        for j in range(k):
            lines.append(np.stack((test_item, neighbours[j])))
        
        y_predict[i] = (np.round(np.mean(y_sorted)))

    print(y_predict)

main(X_train, X_test, y_train, y_test)