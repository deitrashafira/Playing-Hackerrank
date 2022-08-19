#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    minus = []
    positive = []
    zero = []
    for i in arr:
        if i>0:
            positive.append(i)
        elif i<0:
            minus.append(i)
        elif i==0:
            zero.append(i)
    print(len(positive)/len(arr))
    print(len(minus)/len(arr))
    print(len(zero)/len(arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
