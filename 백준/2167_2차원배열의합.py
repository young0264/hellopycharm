import sys
def input():
    return sys.stdin.readline().rstrip()
r,c = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(r)]

t = int(input())
for _ in range(t):
    a,b,x,y = list(map(int,input().split()))
    sum_value = 0
    for i in range(a-1,x):
        for j in range(b-1,y):
            sum_value += graph[i][j]
    print( sum_value)