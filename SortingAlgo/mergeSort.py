import sys

def merge(left, right):
    ll, rr = 0, 0
    result = []
    while ll < len(left) and rr < len(right):
        if left[ll] < right[rr]:
            result.append(left[ll])
            ll += 1
        else:
            result.append(right[rr])
            rr += 1
    result+=left[ll:]
    result+=right[rr:]
    return result

def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    num = len(alist) // 2   # 从中间划分两个子序列
    left = merge_sort(alist[:num]) # 对左侧子序列进行递归排序
    right = merge_sort(alist[num:]) # 对右侧子序列进行递归排序
    return merge(left, right) #归并

ret = merge_sort([1,3,4,5,2])
print(ret)