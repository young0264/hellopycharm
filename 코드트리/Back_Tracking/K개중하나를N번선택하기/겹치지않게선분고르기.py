n = int(input())
#arr = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(n)]
print(arr)
line_cnt = 0
line_max = 0
for i in arr:
    x1 = i[0]
    x2 = i[1]

def dfs():
    global line_cnt,line_max
    if