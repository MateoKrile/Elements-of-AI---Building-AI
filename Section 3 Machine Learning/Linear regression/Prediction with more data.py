'''
Write a program that reads cabin details and prices from a CSV file 
(a standard format for tabular data) and fits a linear regression model to it. 
The program should be able to handle any number of data points (cabins) 
described by any number of features (like size, size of sauna, number of bathrooms, ...).

You can read a CSV file with the function np.genfromtxt(datafile, skip_header=1). 
This will return a numpy array that contains the feature data in the columns preceding the last one, 
and the price data in the last column. The option skip_header=1 just means that the first line in the 
file is supposed to contain just the column names and shouldn't be included in the actual data.

The output of the program should be the estimated coefficients and the predicted or 
"fitted" prices for the same set of cabins used to estimate the parameters. So if you fit the model 
using data for six cabins with known prices, the program will print out the prices that the model predicts 
for those six cabins (even if the actual prices are already given in the data).

Note that here we will not actually only simulate the file input using Python's io.StringIO function 
that takes an input string and pretends that the contents is coming from a file. In practice, 
you would just name the input file that contains the data in the same format as the string input below.
'''

import numpy as np
from io import StringIO

input_string = '''
25 2 50 1 500 127900
39 3 10 1 1000 222100
13 2 13 1 1000 143750
82 5 20 2 120 268000
130 6 10 2 600 460700
115 6 10 1 550 407000
'''

np.set_printoptions(precision=1)    # this just changes the output settings for easier reading
 
def fit_model(input_file):
    # read the data in and fit it. the values below are placeholder values
    data = np.genfromtxt(input_file, skip_header=1)
    x = np.array([row[:-1] for row in data])
    y = np.array([row[-1] for row in data])
    print(y)
    c = np.linalg.lstsq(x, y)[0]
    print(c)
    print(x @ c)

# simulate reading a file
input_file = StringIO(input_string)
fit_model(input_file)