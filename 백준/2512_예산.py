from bisect import bisect_right
n = int(input())
arr = sorted(list(map(int, input().split())))
numbers = [i for i in range(arr[-1]+1)]
budget = int(input())
size = len(arr)
cnt = 0
ans = 0
mid = len(arr)
left,right =0,arr[-1]
while left <= right :
    sumvalue = 0
    mid = (left+right)//2
    arr_idx = bisect_right(arr,mid)
    sumvalue += sum(arr[:arr_idx])
    sumvalue += (size-arr_idx)*mid
    if sumvalue > budget:
        right = mid-1
    else : left = mid+1
print(right)

