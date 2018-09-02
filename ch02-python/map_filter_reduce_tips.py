# -*- coding: utf-8 -*-

# 保证脚本与Python3兼容
from __future__ import print_function

import sys

if sys.version_info[0] == 3:
    from functools import reduce
else:
    pass

"""
Created on Sun Sep  2 12:07:49 2018

@author: w2hw

内置map函数有两个参数，第一个是一个函数，第二个是一个可遍历对象 \
    (tuple, list, dict等) 
map函数将第二个参数里的每个元素依次传给作为第一个参数的函数，\
    并将函数的返回值依顺序组成一个列表(python3中不是列表而是可迭代对象)

filter函数也有两个参数，第一个是设定filter条件，第二个也是一个可遍历对象

reduce函数是用来做聚合运算的
"""

l = range(6)

print("l: ", list(l))

addOne = lambda x : x + 1

twoTimes = lambda x : x * 2

square = lambda x : x ** 2

print("add one: ", list(map(addOne, l)))

#其中的x表示不同的函数
print("[list(map(lambda x : x(i), [twoTimes, square])) for i in l]: \n", \
      [list(map(lambda x : x(i), [twoTimes, square])) for i in l])

print("filter: ", list(filter(lambda x : x % 2 == 0, l)))

print("reduce: ", reduce(lambda accumValue, addValue: accumValue + addValue, l, 0))