from collections import deque
#이분그래프 판별 : 깊이에 따른 + - 상태체크
## 같은 level의 색은 모두 같아야하고, 방문하는 지점의 색깔은 현재색깔과 달라야함
t = int(input())
for _ in range(t):
    v,e = map(int,input().split())
    graph = [[] for _ in range(v+1)]
    visited =[0]*(v+1)

    for i in range(e):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    que = deque()
    flag = 1
    for z in range(1,v+1):
        if not visited[z]:
            visited[z] = 1
            que.append(z)
    # que.append(1)
    # visited[1] = 1
            if flag:
                while que:
                    dx = que.popleft()
                    for nx in graph[dx]:
                        if not visited[nx]:
                            visited[nx] = -visited[dx]
                            que.append(nx)
                        else:
                            if visited[dx] == visited[nx]:
                                flag = 0
                                break

    if not flag :
        print('NO')
    else: print('YES')

