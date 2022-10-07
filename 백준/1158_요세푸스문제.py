
]from collections import deque
n,k=map(int,input().split())
q=deque()
arr=[]
a=[i for i in range(1,n+1,1)]
for i in a:
    q.append(i)
while True:
    for i in range(k-1):
        q.append(q.popleft())
    arr.append(q.popleft())
    if len(q)==0:
        break
#print("<",', '.join(map(str,arr)),">",sep='')

print([i for i in arr])
