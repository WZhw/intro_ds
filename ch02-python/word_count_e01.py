# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 08:15:17 2018

@author: w2hw
"""

# 保证脚本与Python3兼容
from __future__ import print_function

def wordCount(data):
    re = {}
    for word in data:
        #re[word] = re[word].get(word, 0) + 1 一开始错误的写法
        re[word] = re.get(word, 0) + 1
    return re

if __name__ == "__main__":
    data = ["ab", "bc", "cd", "bc", "a", "cd"]
    print("The result is %s" % wordCount(data))