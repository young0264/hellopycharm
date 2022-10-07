# 0이면 중복합 끝
#else
n=int(input())
arr=list(map(int,input().split()))
cnt=0
res = []
for i in arr:
    if i==0:
        cnt = 0
    else:
        cnt+=1
        res.append(cnt)
print(sum(res))