from collections import deque
#arr1,2다 해줘야돼. arr1 [0]의 값때매
n = int(input())
arr = deque(map(int,input().split()))
arr2 = deque(i for i in range(1,n+1))
spare = []
for i in arr:
    spare.append(i)
res = []
for _ in range(n-1):
    now = arr[0]
    #ans.append(spare.index(now)+1)
    if now > 0:
        arr.popleft()
        res.append(arr2.popleft())
        for i in range(now-1):
            arr.append(arr.popleft())
            arr2.append(arr2.popleft())
    elif now < 0:
        arr.popleft()
        res.append(arr2.popleft())
        for i in range(now*-1):
            arr.appendleft(arr.pop())
            arr2.appendleft(arr2.pop())

#ans.append(spare.index(arr[0])+1)
x = res+[arr2[0]]
print(*x)