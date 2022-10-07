import sys
input = sys.stdin.readline
n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
a_arr=[]
b_arr=[]
def dfs(start,box):#1부터시작
    if len(box) == n//2:
        ano_box = []
        for i in range(1,n+1):
            if i not in box:
                ano_box.append(i)
        a_arr.append(box)
        b_arr.append(ano_box)
        return
    for i in range(start,n+1):
        dfs(i+1,box+[i])
dfs(1,[])
ans = sys.maxsize

def f(arr): #각조합의 배열과 0을 넣어주면 그에대한 합을출력
    res = 0
    for i in arr:#123 -> 12,13,23
        for j in arr:
            if not i == j:
                #print('arr=',arr)
                #print('i,j',i,j)
                res += graph[i-1][j-1]
    return res

for t in range(len(a_arr)):#조합의가지수들
    #print(len(a_arr))
    #print(a_arr)
    a = f(a_arr[t])
    b = f(b_arr[t])
    ans = min(ans,abs(a-b))
print(ans)
######222222
#import sys
#from itertools import combinations as cb
#N = int(sys.stdin.readline()) // 2
#M = 2*N
#stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
#newstat = [sum(i) + sum(j) for i, j in zip(stat, zip(*stat))]
#allstat = sum(newstat) // 2
#
#mins = 65535
#for l in cb(newstat[:-1], N):
#    mins = min(mins, abs(allstat - sum(l)))
#print(mins)
#######333333
#def solve(idx, cnt, diff):
#    global res
#    if cnt == n//2:
#        res = min(res, abs(diff))
#        return
#    if idx == n:
#        return
#    solve(idx+1, cnt+1, diff-r[idx]-c[idx])
#    solve(idx+1, cnt, diff)
#n = int(input())
#s = [[0]*n for _ in range(n)]
#r = [0]*n
#c = [0]*n
#t = 0
#for i in range(n):
#    s[i] = list(map(int, input().split()))
#    for j in range(n):
#        t += s[i][j]
#        r[i] += s[i][j]
#        c[j] += s[i][j]
#res = 987654321
#solve(1, 1, t-r[0]-c[0])
#print(res)