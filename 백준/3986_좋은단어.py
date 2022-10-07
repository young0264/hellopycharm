from collections import deque

n = int(input())
ans = 0
for _ in range(n):
    s = deque(input())
    box = []
    while len(s):
        if not len(box) or s[0]!=box[-1]:
            x = s.popleft()
            box.append(x)
        elif box[-1]==s[0]:
            box.pop()
            s.popleft()
    if not len(box):
        ans+=1
print(ans)



