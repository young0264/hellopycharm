import sys
from collections import deque
n=int(input())
q=deque()

for i in range(n):
    l=sys.stdin.readline().split()

    if l[0]=='push':
        q.append(l[1])

    elif l[0]=='pop':
        if len(q)!=0:
            print(q.popleft())
        else :
            print(-1)
    elif l[0]=='size':
        print(len(q))
    elif l[0] =='empty':
        if len(q)==0:
            print(1) 
        else: print(0)
    elif l[0] =='front':
        if len(q)!=0:
            print(q[0])
        else : #0이면
            print(-1)
    else:
        if len(q)!=0 :
            print(q[-1]) 
        else: 
            print(-1)