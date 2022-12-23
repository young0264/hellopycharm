n = int(input())
answer = 0
if n==0:
    print(1)
    exit(0)
dp = [0]*(n+1)
# def fibo(n):
#     global answer
#     if n<2:
#         answer = (answer+ 1)%1000000007
#         return n
#     answer =(answer + 1)%1000000007
#     return fibo(n-1)+fibo(n-2)
# fibo(m)
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    dp[i] = 1+dp[i-1]+dp[i-2]

print(dp[n]%1000000007)
