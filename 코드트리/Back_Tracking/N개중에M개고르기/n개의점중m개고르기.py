import math
n,m = map(int,input().split())
spot = [list(map(int,input().split())) for _ in range(n)]
combi = []
def dist(a,b):  #두점사이의 거리구하기
    a1,a2 = a
    b1,b2 = b
    d = (b1-a1)**2 +(b2-a2)**2
    return d

def dfs(start,box):
    if len(box)==m:
        combi.append(box)
        return
    for i in range(start,n):
        dfs(i+1,box+[spot[i]])
dfs(0,[])
res = []
for t in range(len(combi)):
    d = []
    for i in range(m):
        for j in range(m):
            d.append(dist(combi[t][i],combi[t][j]))
    res.append(max(d))
print(min(res))