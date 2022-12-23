n = int(input())
dp = [0]*(n+1)

# 1:상근, 2:창영

now = 1
for i in range(n,-1,-1):
    # print(dp)
    if i-1 >= 0 and dp[i-1] != 1:
        dp[i-1] = now
    if i-3 >= 0 and dp[i-3] != 3:
        dp[i-1] = now
    if now == 1:
        now = 2
    else:
        now = 1
    if dp[0]:
        break
if dp[0] == 2:
    print('SK')
else:
    print('CY')