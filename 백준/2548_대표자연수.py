import sys
def input():
    return sys.stdin.readline().rstrip()
n = int(input())
arr = sorted(list(map(int,input().split())))
mid = n//2
if n%2 == 0:
    print(arr[mid-1])
else:
    print(arr[mid])


