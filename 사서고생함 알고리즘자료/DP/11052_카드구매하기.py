n=int(input()) #4
p=[0]+list(map(int,input().split())) # 1,5,6,7 : 1~4번호의 카드의 가치들
dp=[0 for _ in range(10001)] # n+1만큼의 0의배열 만들기
#dp[i]=p[j]+dp[i-j]

for i in range(1,n+1):
    for j in range(1,i+1):
        dp[i]= max(dp[i],p[j]+dp[i-j])

print(dp[n])

