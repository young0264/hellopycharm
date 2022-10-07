from collections import deque
n,k = map(int,input().split())
arr = list(map(int,input().split()))
lion_pos = deque()
left,right = -1,0
cnt = 0
ans_arr =[]

for i in range(n):
    if arr[i]==1:
        lion_pos.append(i)
        cnt += 1
        right = i
    if cnt == k:
        cnt -=1
        left=lion_pos.popleft()
        ans_arr.append(right-left+1)

if not lion_pos:
    print(-1)

else:print(min(ans_arr))


