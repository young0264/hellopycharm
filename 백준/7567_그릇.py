arr = list(input())
cnt=10
for i in range(1,len(arr)):
    if arr[i-1] == arr[i]:
        cnt += 5
    else:
        cnt += 10
print(cnt)