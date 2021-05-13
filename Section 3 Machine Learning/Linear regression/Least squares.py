'''
Write a program that calculates the squared error for multiple sets of coefficient values 
and prints out the index of the set that yields the smallest squared error: 
this is a poor man's version of the least squares method where we only consider a fixed set of alternative coefficient vectors 
instead of finding the global optimum.
'''
import numpy as np

# data
X = np.array([[66, 5, 15, 2, 500], 
              [21, 3, 50, 1, 100], 
              [120, 15, 5, 2, 1200]])
y = np.array([250000, 60000, 525000])

# alternative sets of coefficient values
c = np.array([[3000, 200 , -50, 5000, 100], 
              [2000, -250, -100, 150, 250], 
              [3000, -100, -150, 0, 150]])   

def find_best(X, y, c):
    smallest_error = np.Inf
    best_index = -1
    lstsq = np.linalg.lstsq(X, y)[0]
    for i, coeff in enumerate(c):
        diff = abs(sum(lstsq - coeff))
        smallest_error, best_index = (diff, i) if diff<smallest_error else (smallest_error, best_index)
    print("the best set is set %d" % best_index)

find_best(X, y, c)