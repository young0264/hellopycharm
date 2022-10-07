#a,b배로 이동가능,, n*a ,, n*b
from collections import deque
a, b, start, finish = map(int,input().split())
visited = [0 for _ in range(100001)]
def dist(now,i):    #0~9
    global a,b
    arr = [now+1,now-1,now*a,-now*a,now*b,-now*b,now+a,now-a,now+b,now-b]
    return arr[i]

def bfs(start):
    global finish
    que = deque()
    que.append(start)
    visited[start]=1
    while que:
        node = que.popleft()
        for i in range(10):
            next = dist(node,i)
            if 0<=next<100001 and not visited[next]:
                visited[next] = visited[node]+1
                que.append(next)
                if next == finish:
                    return
bfs(start)
print(max(visited)-1)

