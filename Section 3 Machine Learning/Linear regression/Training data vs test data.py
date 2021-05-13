'''
Write a program that reads data about one set of cabins (training data), 
estimates linear regression coefficients based on it, then reads data about another set of cabins (test data), 
and predicts the prices in it. Note that both data sets contain the actual prices, 
but the program should ignore the prices in the second set. They are given only for comparison.

The contents of the sets are as follows.

training data
size	size of the sauna	distance to water	number of indoor bathrooms	proximity of neighbors	actual price
25	2	50	1	500	    127900
39	3	10	1	1000	222100
13	2	13	1	1000	143750
82	5	20	2	120	    268000
130	6	10	2	600	    460700
115	6	10	1	550	    407000
test data
size	size of the sauna	distance to water	number of indoor bathrooms	proximity of neighbors	actual price
36	3	15	1	850	    196000
75	5	18	2	540	    290000
You can read the data into the program the same way as in the previous exercise.

You should then separate the feature and price data that you have just read from the file into two separate arrays 
names x_train and y_train, so that you can use them as argument to np.linalg.lstsq.

The program should work even if the number of features used to describe the cabins differs from five 
(as long as the same number of features are given in each file).

The output should be the set of coefficients for the linear regression and the predicted prices for the second set of cabins.
'''
import numpy as np
from io import StringIO


train_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

test_string = '''
36 3 15 1 850 196000
75 5 18 2 540 290000
'''

def main():
    # this just changes the output settings for easier reading
    np.set_printoptions(precision=1)    

    # read in the training data and separate it to x_train and y_train
    train_file = StringIO(train_string)
    train_data = np.genfromtxt(train_file, skip_header=1)
    x_train = np.array([row[:-1] for row in train_data])
    y_train = np.array([row[-1] for row in train_data])
    
    # fit a linear regression model to the data and get the coefficients
    c = np.linalg.lstsq(x_train, y_train)[0]

    # read in the test data and separate x_test from it
    test_file = StringIO(test_string)
    test_data = np.genfromtxt(test_file, skip_header=1)
    x_test = np.array([row[:-1] for row in test_data])

    # print out the linear regression coefficients
    print(c)

    # this will print out the predicted prics for the two new cabins in the test data set
    print(x_test @ c)

    
main()