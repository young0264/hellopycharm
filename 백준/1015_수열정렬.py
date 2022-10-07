n = int(input())
A = list(map(int,input().split()))

arr = sorted(A)
ans = []

for i in range(n):
    for j in range(n):
        if A[i]==arr[j]:
            ans.append(j)
            arr[j] = -1
            break
print(*ans)