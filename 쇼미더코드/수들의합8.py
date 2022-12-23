from itertools import combinations_with_replacement
import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()
def dfs(start, value):#0
    global answer
    if len(value) == 2:
        a, b = 0, 0
        if value[1] - value[0] == value[1]:
            a = arr[value[1]]
            b = brr[value[1]]
        else:
            a = arr[value[1]] - arr[value[0] - 1]
            b = brr[value[1]] - brr[value[0] - 1]
        if a == b:
            answer += 1
        return

    for i in range(start,n):
        dfs(i, value + [idx[i]])

n = int(input())
idx = [i for i in range(n)]
arr = list(map(int,input().split()))
brr = list(map(int,input().split()))
answer = 0
for i in range(1,n):
    arr[i] = arr[i] + arr[i-1]
for i in range(1,n):
    brr[i] = brr[i] + brr[i-1]

dfs(0,[])

print(answer)