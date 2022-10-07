n = int(input())
arr = []
for i in range(n):
    arr.append(input())
l = len(arr[0])
ans = ''
for i in range(l):
    alphabet = arr[0][i]
    for j in range(n):
        flag = 0
        if arr[j][i] != alphabet:
            ans += '?'
            flag = 1
            break
    if not flag:
        ans += alphabet
print(ans)