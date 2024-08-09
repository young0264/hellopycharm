from collections import deque
n,k,m = map(int,input().split())

que = deque(range(1,n+1))
cnt = 0
while que: #0이면 오른쪽, 1이면 왼쪽
    if cnt//m % 2 == 0:
        for i in range(k-1):
            que.append(que.popleft())
    else:
        for i in range(k):
            que.appendleft(que.pop())
    cnt += 1
    print(que.popleft())






#
# now = k
# cnt = 0
# answer = [k]
# c = 1
# for i in range(n-1):
#     while True:
#         if now==3:
#             c+=1
#             print(c)
#         if not visited[now]:
#             if cnt == k:
#                 answer.append(now)
#                 visited[now] = 1
#                 cnt = 0
#                 if now + 1 > n:
#                     now = 1
#                 else:
#                     now = (now+1)%n
#                 break
#             else:
#                 cnt += 1
#                 now = (now+1)%n
#         else:
#             now = (now+1)%n
# print(answer)
# print(1%3)
