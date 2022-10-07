import sys
input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
if sum(arr) == len(arr):
    print(1)
else:
    print(sum(arr)-(len(arr)-1))