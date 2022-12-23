n = int(input())
dp = [0] * (1000001)

dp[1] = 1

# for i in range(1, -1000001, -1):
#     if dp[i] > 0 and dp[i - 1] > 0:
#         dp[i - 2] = dp[i] % 1000000000 - dp[i - 1] % 1000000000
#     elif dp[i-1] < 0:
#         dp[i - 2] = dp[i] % 1000000000 - (-(abs(dp[i - 1]) % 1000000000))
#     elif dp[i]<0:
#         dp[i - 2] = -(abs(dp[i]) % 1000000000) - dp[i - 1] % 1000000000
#
#
# for i in range(2, 1000001):
#     # dp[i] = dp[i-1]%1000000000 + dp[i-2]%1000000000
#     if dp[i - 1] > 0 and dp[i - 2] > 0:
#         dp[i] = dp[i - 1] % 1000000000 + dp[i - 2] % 1000000000
#     elif dp[i - 2] <0 :
#         dp[i] = dp[i - 1] % 1000000000 + -(abs(dp[i - 2]) % 1000000000)
#     elif dp[i-1]<0:
#         dp[i] = -(abs(dp[i - 1]) % 1000000000) + dp[i - 2] % 1000000000

for i in range(2,1000001):
    dp[i] = (dp[i-1]+dp[i-2])%1000000000

if n < 0 and -n%2 == 0:
    res = -1
elif n == 0:
    res = 0
else:
    res = 1

print(res)

if n < 0 :
    print((dp[-n])%1000000000)
else:
    print((dp[n])%1000000000)