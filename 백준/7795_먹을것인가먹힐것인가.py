n = int(input())
def binary_search(arr,target,s,e):
    x=0
    while s <= e:
        mid = (s+e)//2
        if arr[mid] > target :
            e = mid-1
            x=s
        else:
            s = mid+1
            x = s
    return x
from bisect import bisect

for _ in range(n):
    cnt = 0
    a,b = map(int,input().split())
    arr = sorted(list(map(int,input().split())))
    brr = list(map(int,input().split()))
    for i in brr:
        cnt+=(a-binary_search(arr,i,0,a-1))
    print(cnt)
