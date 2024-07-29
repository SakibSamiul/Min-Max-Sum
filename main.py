#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    minimum = 0
    maximum = 0
    n = len(arr)
    arr.sort()
    l = n - 1

    for i in range(n-1):
        minimum += arr[i]
        maximum += arr[l]
        l -= 1 
    print(minimum, maximum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    
