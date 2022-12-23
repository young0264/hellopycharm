a = input()
b = input()
answer = 0

lengthA = len(a)
lengthB = len(b)
# dp = [[0]*len(a) for _ in range(len(b))] #방법1 메모리 N*M
#방법1
# for i in range(lengthA):
#     if a[i]==b[0]:
        # dp[0][i] = 1
# for i in range(lengthB):
#     if a[0] == b[i]:
        # dp[i][0] = 1
# for i in range(1,lengthB):
#     for j in range(1,lengthA):
#         if b[i] == a[j]:
            # dp[i][j] = dp[i-1][j-1] + 1
            # answer = max(answer, dp[i][j])

#방법2 메모리 N방법
pre = [0]*lengthB
for i in range(lengthB):
    if a[0] == b[i]:
        pre[i] = 1
for i in range(1,lengthA):
    arr = [0]*lengthB
    max_value = 0
    if a[i] == b[0]:
        arr[0] = 1
    for j in range(1,lengthB):
        if a[i] == b[j]:
            arr[j]= pre[j-1]+1
            max_value = max(max_value,arr[j])
    answer = max(answer,max_value)
    pre = arr[:]
print(answer)




##직전의 배열만 활용하기