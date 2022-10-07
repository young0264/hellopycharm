from collections import deque
n,k = map(int,input().split())
q = deque(range(1,n+1)) #구현해보기
result=[]
#for _ in range(n):
while q:
    for i in range(k-1):
        q.append(q.popleft())
    result.append(q.popleft())
#print('<{}>'.format(result))
print('<{}>'.format(', '.join(map(str ,result))))