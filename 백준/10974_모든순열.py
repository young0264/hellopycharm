import sys
sys.setrecursionlimit(10**6)
n = int(input())
numbers = [i for i in range(1,n+1)]
def dfs(box):
    if len(box) == n:
        print(*box,sep=' ')
    for i in range(n):
        if numbers[i] not in box:
            dfs(box+[numbers[i]])

dfs([])
