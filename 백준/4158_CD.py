# print(2**30) 10억
# from collections import defaultdict
# import sys
#
# while True:
#    cnt = 0
#    arr = defaultdict(list)
#    a, b = map(int, input().split())
#    if a==0 and b==0 : break
#    for _ in range(a):
#        arr[int(input())] = 1
#    for _ in range(b):
#        if arr[int(input())] :
#            cnt+=1
#    print(cnt)
import sys

input = sys.stdin.readline
while True:
    cnt = 0
    a, b = map(int, input().split())
    if a == 0 and b == 0: break
    arr = []
    for _ in range(a):
        arr.append(int(input()))

    for i in range(b):
        goal = int(input())
        start = 0
        end = a - 1
        while start <= end:
            mid = (start + end) // 2
            if goal > arr[mid]:
                start = mid+1
            elif goal < arr[mid]:
                end = mid - 1
            else:
                cnt += 1
                break
    print(cnt)
