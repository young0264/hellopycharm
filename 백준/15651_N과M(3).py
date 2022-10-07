N , K = map(int,input().split())

result=[]

def dfs(box):
    if len(box) == K:
        result.append(box)
        return
    for i in range(1,N+1):
        dfs(box + [i])

dfs([])
#print(result)
for i in result:
    print(*i)