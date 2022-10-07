import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

arr = list(map(int,input().split()))
cnt = 0
res = []
def dfs(depth):
    global cnt
    if depth == 10:
        flag = 0
        for i in range(10):
            if res[i] == arr[i]:
                flag += 1
        if flag >=5 :
            cnt += 1
        return
    for j in range(1,6):
        if depth>=2 and res[depth-2] == res[depth-1] == j :
            continue
        res.append(j)
        dfs(depth+1)
        res.pop()


dfs(0)
print(cnt)