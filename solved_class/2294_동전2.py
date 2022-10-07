n, k = map(int,input().split())
dp=[0]*10001
arr=[]
for _ in range(n):
    arr.append(int(input()))
for i in range(k+1):
    a=[]
                #i가 0일떄,1일때2,3,4,5,6,7,8,
                    #l이 1일때 5일때 12........
    for l in arr :
        if i >= l and dp[i-l]!=-1:
            a.append(dp[i-l]) #공백의 a배열에 최소한의 필요한 동전개수가 입력되어있어
                            #근데왜append로 집어넣지

    if not a :
        dp[i]=-1
    else :
        dp[i]=min(a)+1

print(dp[k])



