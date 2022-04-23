import logging
import numpy as np

logging.basicConfig(filename='test1_log.log', level=logging.DEBUG)  # setting up the logging file and other configurations

arr = np.array([1, 2, 3, 4])  # installed third party package and used it
print(arr.shape)
logging.debug(arr.shape)
logging.debug(arr)


