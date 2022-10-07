n = int(input())
arr = [-1] * (n + 1)
answer = 0
for _ in range(n):
    a, b = map(int, input().split())
    if arr[a] == -1:
        arr[a] = b
    elif arr[a] != b :
        answer += 1
        arr[a] = b
print(answer)


