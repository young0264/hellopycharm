#조합을 dfs로 구현
n , k = map(int,input().split())
arr=[]
def dfs(start, value):
    if len(value) == k:
        arr.append(value)
        return
    for i in range(1,n+1):
        if i not in value:  ##this
            dfs(i+1, value + [i])

dfs(1,[])   #value는 배열
for i in arr:
    print(*i)