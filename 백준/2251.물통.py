#bfs로 파고든다는 아이디어를 떠올리는게 나는 너무 어려웠따.

from collections import deque
a,b,c = map(int,input().split())    #a행,bd열로
visited = [[0]*(b+1) for _ in range(a+1)]
q = deque()
res = []
def move(x,y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x,y))
def bfs():
    q.append((0,0))
    while q:
        x,y = q.popleft()
        z = c - (x+y)
        if x == 0 :
            res.append(z)

        # a->c, a->b, b->c, b->a, c->a, c->b// a,b,c는 기본값

        water = min(x,c-z)
        if not visited[x-water][y]:
            visited[x - water][y] = True
            q.append((x-water,y))

        water = min(x,b-y)
        move(x-water,y+water)

        water = min(y,c-z)
        move(x,y-water)

        water = min(y,a-x)
        move(x+water,y-water)

        water = min(z,a-x)
        move(x+water,y)

        water = min(z,b-y)
        move(x,y+water)

bfs()
res = set(res)
res= sorted(res)
print(*res)