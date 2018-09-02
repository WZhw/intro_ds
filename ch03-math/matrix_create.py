# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 17:10:20 2018

@author: w2hw
"""

import numpy as np

A = np.matrix([[1, 2], [3, 4], [5, 6]])

B = np.array(range(1, 7)).reshape(3, 2)

#A * A

B * B

#创建特殊矩阵

np.zeros((3,2))

np.identity(3)

np.diag([1, 2, 3])

m = np.array(range(1, 10)).reshape(3, 3)

m[[0, 2]]

m[:, [1, 2]]