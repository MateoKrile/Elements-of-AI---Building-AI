'''
Edit the following program so that it can process multiple cabins that may be described by any number of details (like five below), 
at the same time. You can assume that each of the lists contained in the list x and the coefficients c contain the same number of elements.
'''
import numpy as np
# input values for three mökkis: size, size of sauna, distance to water, number of indoor bathrooms, 
# proximity of neighbors
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]
c = [3000, 200, -50, 5000, 100]    # coefficient values

def predict(X, c):
    X = np.array(X)
    c = np.array(c)            
    print(X @ c)

predict(X, c)
