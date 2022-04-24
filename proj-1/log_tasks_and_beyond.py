import logging
import numpy as np
import pandas as pd  # to manipulate csv files

logging.basicConfig(filename='test1_log.log',
                    level=logging.DEBUG)  # setting up the logging file and other configurations

arr = np.array([1, 2, 3, 4])  # installed third party package and used it
print(arr.shape)
logging.debug(arr.shape)
logging.debug(arr)

f = open("test_file.txt", "r")  # reading a file in python
print(f.read())  # printing its content

# f = open("test_file.txt", "a") # this is to write in the file
# f.write("One more line")
# f.close()

f = open("test_file.txt", "r")
print(f.read())

data = pd.read_csv('iris.csv')

print(data.loc[0, :])  # first row
print(data['sepal.length'])  # first column
