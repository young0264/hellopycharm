from collections import deque

t = int(input())
q = deque()
for i in range(t):
    n = int(input())
    for j in range(n):
        a,b=input().split()
        #q.sort()
        if a=='I':
            q.append(int(b))
        elif a=='D' and b=='1':
            sorted(q).pop()
        elif a=='D' and b=='-1':
            sorted(q).popleft()
        elif len(q)==0 and a=='D':
            continue
    if len(q) ==0:
        print('EMPTY')

    else :
        print(max(q),min(q))
