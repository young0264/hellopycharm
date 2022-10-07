#조합을 dfs로 구현
import sys
sys.setrecursionlimit(10**6)
n , k = map(int,input().split())
arr=[]
def dfs(start, value):
    if len(value) == k:
        arr.append(value)
        return
    for i in range(start,n+1):
        dfs(i, value + [i])


dfs(1,[])   #value는 배열
#print(sorted(arr))
for i in arr:
    print(*i)
