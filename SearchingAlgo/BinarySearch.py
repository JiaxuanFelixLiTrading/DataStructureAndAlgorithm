"""
Binary search
Author:Jiaxuan Li
It must be used in sorted data
It will cut off the unrelavent half and searching in the relavent half (Iteration)
Time complexity is O(log(n))
"""

def binarysearch(data, value):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (right + left) // 2 # lower bound
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1 # left region
        else:
            right = mid - 1 # right region
    return -1

"""
Input:
12 
1 3 5 7 9 11 12 15
Return:
The index of 12 is 6
"""

key = int(input())
while True:
    try:
        data = input().split(" ")
    except:
        break
data = [int(i) for i in data]
ret = binarysearch(data, key)
if ret == -1:
    print(f"Value {key} is Not Found in data {data}")
else:
    print(f"The index of {key} is {ret}")

