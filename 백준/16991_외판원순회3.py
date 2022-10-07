import math
import sys
input = sys.stdin.readline
MAX_INT = sys.maxsize
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
selected_arr = []
def dist(s,e):
    s1,s2 = s
    e1,e2 = e
    value= math.sqrt((e1-s1)**2+(e2-s2)**2)
    return value
def dfs(box):
    if len(box) == 4:
        selected_arr.append(box)
        return
    for i in range(4):
        if arr[i] not in box:
            dfs(box+[arr[i]])
dfs([])
#print(selected_arr)
min_ans = MAX_INT
for combi in selected_arr:
    res=0
    now = combi[0]
    for i in range(1,len(combi)):
        res += dist(now,combi[i])
        now = combi[i]
        #print(res)
    res+=dist(now,combi[0])
    min_ans = min(min_ans,res)
print(min_ans)