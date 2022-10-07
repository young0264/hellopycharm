from collections import deque

t=int(input())
for i in range(t):
    m,n=map(int,input().split())
    q=deque(map(int,input().split()))
    index=[0 for _ in range(m)] #0은뭐지
    cnt=0
    index[n]=1
    while q :
        if max(q) == q[0]:
            if index[0]==1:
                break
            else :
                q.popleft()
                index.pop(0)
                cnt+=1
        else:
            q.append(q.popleft())
            index.append(index.pop(0))
    print(cnt+1)

