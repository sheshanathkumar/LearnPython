#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic, n, m):
    res = []
    for i in range (n) :
        
        for j in range (i+1, n):
            sum = 0
            for k in range (m):
                sum = sum + topic[i][k] or topic[j][k]
            res.append(sum)
    maxm = max(res)
    cnt = 0
    for i in range(len(res)) :
        if maxm == res[i]:
            cnt += 1
    del res
    res = []
    res.append(maxm)
    res.append(cnt)
    return res  
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic, n, m)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
