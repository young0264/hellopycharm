from bisect import bisect_left,bisect_right
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
arr = sorted(list(map(int,input().split())))
#arr = [i for i in range(100000)]

#def min_Upper(left,right,arr,target):
#    min_idx = right
#    mid = -1
#    while left<=right:
#        mid = (left+right)//2
#        if arr[mid]>target:
#            right = mid-1
#            min_idx = min(min_idx,mid)
#        else: left = mid+1
#    return mid
#
#def min_Lower(left,right,arr,target):
#    min_idx = right
#    mid = -1
#    while left<=right:
#        mid = (left+right)//2
#        if arr[mid]>=target:
#            right = mid-1
#            min_idx = min(min_idx,mid)
#        else: left = mid+1
#    return mid
#
for _ in range(m):
    s,e = map(int,input().split())
    a = bisect_left(arr,s)
    b = bisect_right(arr,e)
    print(b-a)

