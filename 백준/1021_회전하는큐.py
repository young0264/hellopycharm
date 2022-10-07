from collections import deque
arr=deque()
n, m =map(int, input().split())
for i in range(1,n+1):
    arr.append(i)
x= list(map(int, input().split()))
cnt=0
for i in x:
    if arr.index(i) <= len(arr)//2 :#왼쪾
        while arr[0] != i:
            arr.append(arr.popleft())
            cnt+=1
        arr.popleft()

    elif arr.index(i) > len(arr)//2 :#오른쪾
        while arr[0] != i:
            arr.appendleft(arr.pop())
            cnt+=1
        arr.popleft()

print(cnt)

#while arr[0] != i:
#    arr.append(Arr.popleft())
#   cnt+=1
#arr.popleft()
#while문 간단하게 표현