#one hot encoded
import random
import numpy as np
data = np.array([
[1, 1, 0, 0],
[0, 0, 1, 1],
[0, 0, 0, 0],
[1, 0, 0, 0],
[0, 1, 0, 0],
[0, 0, 1, 0],
[0, 0, 0, 1],
[0, 1, 1, 0],
[1, 0, 0, 1],
[1, 1, 1, 0],
[1, 1, 0, 1],
[1, 0, 1, 1],
[0, 1, 1, 1],
[1, 1, 1, 1],
[0, 1, 0, 1],
[1, 0, 1, 0],
])

targets = np.array([
    [0, 1, 0],
    [0, 0, 1],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
    [1, 0, 0],
])

nb_data = len(data)
input_size = len(data[1])

