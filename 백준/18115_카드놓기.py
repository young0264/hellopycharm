from collections import deque
n = int(input())
arr = list(map(int, input().split()))
brr = deque(i for i in range(1,n+1))
crr = []
pre_answer = [0]*n
answer = []

for i in arr:
    tmp = 0
    if i == 1:
        crr.append(brr.popleft())
    elif i == 2:
        tmp = brr.popleft()
        crr.append(brr.popleft())
        brr.appendleft(tmp)
    elif i ==3:
        crr.append(brr.pop())
x = [0]+list(reversed([i for i in range(1,n+1)]))
value = 1
for i in range(n):
    pre_answer[crr[i]-1] = value
    value += 1

for i in pre_answer:
    answer.append(x[i])
print(*answer)