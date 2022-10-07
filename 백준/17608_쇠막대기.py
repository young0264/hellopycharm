import sys
input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

now = 0
cnt = 0
for i in range(-1,-n-1,-1):
    if arr[i] > now:
        cnt += 1
        now = arr[i]
    else:
        continue
print(cnt)