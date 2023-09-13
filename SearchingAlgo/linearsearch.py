"""
Linear Search
Author: Jiaxuan Li
It is just a brute force searching
The time Complexity is O(n)
This Algo can be used in both Sorted or Unsorted data
It will read every element one by one until it find the final result
"""

import sys

def linearsearch(data, key):
    for i, val in enumerate(data):
        if i == key:
            return int(val)
            
key = int(input())
while True:
    try:
        sequence = input().split(" ")
    except:
        break
ret = linearsearch(sequence, key)
print(ret)
