# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 20:20:43 2018

@author: w2hw
"""

import numpy as np

from numpy.linalg import inv

n = np.array(range(1, 5)).reshape(2, 2)

print(n)

print(np.transpose(n))

print(n + n)

print(n - n)

print(3 * n)

print(n * n)

print(n.dot(n))

print(inv(n))

print(np.dot(inv(n), n))