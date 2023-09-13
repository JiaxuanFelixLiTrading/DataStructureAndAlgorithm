"""
Interpolation Search
The data has been sorted
It is faster than binary search if the data under some uniform distribution.
Time complexity is O(log(log(n)))
"""

def interpolation_search(data, value):
    left, right = 0, len(data)-1
    while left < right:
        mid = left + int( ((value - data[left])/(data[right] - data[left]) )* (right - left))
        if data[mid] == value:
            return mid
        elif data[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return  -1

key = int(input())
while True:
    try:
        data = input().split(" ")
    except:
        break
data = [int(i) for i in data]
ret = interpolation_search(data, key)
if ret == -1:
    print(f"Value {key} is Not Found in data {data}")
else:
    print(f"The index of {key} is {ret}")