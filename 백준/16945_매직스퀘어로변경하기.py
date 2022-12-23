import sys
arr = []
for _ in range(3):
    a = list(map(int,input().split()))
    arr.extend(a)

num = [i for i in range(1,10)]
answer = sys.maxsize

def check(brr):
    res = 0
    for i in range(9):
        res += abs(arr[i]-brr[i])
    return res

def dfs(box,cnt):
    global answer
    if cnt == 9:
        res = check(box)
        answer = min(answer,res)

        return
    for i in range(1,10):
        if i not in box:
            dfs(box+[i],cnt+1)

dfs([],0)
print(answer)