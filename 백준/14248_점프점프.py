#영우는 이 숫자가 적혀있는 만큼 왼쪽이나 오른쪽으로 점프할 수 있다.

import sys
from collections import deque
sys.setrecursionlimit(10**6)

n = int(input())
arr = list(map(int,input().split()))
start = int(input())
start = start-1 #인덱스로 치환
cnt = 1
#arr[start] = 0  #0으로 방문처리할꺼야
dy = [1,-1]#열
def in_range(x):
    return 0<=x<n
def bfs(now):
    q = deque()
    q.append(now)
    visited = [0] * n
    visited[now]=True
    while q:
        next = q.popleft()
        plus_x = next + arr[next]
        minus_x = next - arr[next]
        if in_range(plus_x) and visited[plus_x]==0:
            q.append(plus_x)
            visited[plus_x] = True
        if in_range(minus_x) and visited[minus_x]==0:
            q.append(minus_x)
            visited[minus_x] = True
    return visited

print(sum(bfs(start)))