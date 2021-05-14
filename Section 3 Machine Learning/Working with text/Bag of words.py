"""
Your task is to write a program that calculates the distances (or differences) between every pair of lines in the 
This Little Piggy rhyme and finds the most similar pair. Use the Manhattan distance as your distance metric.

You can start by building a numpy array to store all the distances. Notice that the diagonal elements in the array 
(elements at positions [i, j] with i=j) will be equal to zero. This happens because the program will compare every 
row also with itself. To avoid selecting those elements, you can assign the value np.inf (the maximum possible floating point value). 
To do this, it's necessary to make sure the type of the array is float.

A quick way to get the index of the element with the lowest value in a 2D array (or in fact, any dimension) is by the function

    np.unravel_index(np.argmin(dist), dist.shape))

where dist is the 2D array. This will return the index as a list of length two.
"""
import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def manhattan_dist(a, b):
    dist = 0
    for ai, bi in zip(a, b):
        dist += abs(ai-bi)
    return dist

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=np.float)
    for x in range(len(data)):
        for y in range(len(data)):
            if x==y:
                dist[x][y] = np.Inf
            else:
                dist[x][y] = manhattan_dist()(data[x], data[y])
    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)

