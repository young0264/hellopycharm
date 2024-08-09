
# cnt = 0
# while True:
#     ans = 0
#     cnt+=1
#     L, P, V = map(int, input().split())
#     if L == 0 and P == 0 and V == 0:
#         break
#     mok = V // P
#     na = V % P
#     ans += mok * L
#     if na <= L:
#         ans += na
#     else:
#         ans += L
#
#
#     print("Case", str(cnt)+":", ans)
import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    arr = []
    for i in range(n):
        a, b = map(int,input().split())
        arr.append([a,b])
    arr = sorted(arr, key=lambda x: x[0])

    now = arr[0][1]
    answer = 1
    for i in range(1, n):
        if arr[i][1] < now:
            answer += 1
            now = arr[i][1]
    print(answer)

