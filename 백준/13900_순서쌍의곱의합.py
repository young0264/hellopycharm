import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
c = sum(arr)
answer = 0
for i in range(n):
    answer += (c - arr[i])*arr[i]
    c-=arr[i]
print(answer)