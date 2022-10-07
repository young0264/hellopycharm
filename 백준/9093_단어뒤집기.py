n = int(input())
for _ in range(n):
    arr = input().split()
    ans = []
    for i in arr:
        ans.append(i[::-1])
    print(' '.join(ans))