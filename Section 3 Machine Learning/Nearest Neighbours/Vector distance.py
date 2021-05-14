"""
You are given an array x_train with multiple input vectors (the "training data") and 
another array x_test with one more input vector (the "test data"). 
Find the vector in x_train that is most similar to the vector in x_test. In other words, 
find the nearest neighbor of the test data point x_test.

The code template gives the function dist to calculate the distance between any two vectors. 
What you need to add is the implementation of the function nearest that takes the arrays x_train 
and x_test and prints the index (as an integer between 0, ..., len(x_train)-1) of the nearest neighbor.
"""
import numpy as np

x_train = np.random.rand(10, 3)   # generate 10 random vectors of dimension 3
x_test = np.random.rand(3)        # generate one more random vector of the same dimension

def dist(a, b):
    sum = 0
    for ai, bi in zip(a, b):
        sum += (ai - bi)**2
    return np.sqrt(sum)
    
def nearest(x_train, x_test):
    nearest = -1
    min_dist = np.Inf
    for i, vector in enumerate(x_train):
        d = dist(vector, x_test)
        min_dist, nearest = (d, i) if d<min_dist else (min_dist, nearest)

    print(nearest)
    
nearest(x_train, x_test)