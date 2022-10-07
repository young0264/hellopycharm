import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n , m , start = map(int,input().rstrip().split())
arr = [[] for _ in range(n+1)]
#visited=[False for _ in range(n+1)]
res = [-1 for _ in range(n)]
#a,*b = map()
for i in range(m):
    a , b = map(int,input().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(x,depth):
    res[x-1] = depth
    for i in sorted(arr[x]):
        if res[i-1] == -1:
            dfs(i,depth+1)

dfs(start,0)
print(*res,sep='\n')
#for i in res:
 #   print(i)

