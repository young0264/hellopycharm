'''
뒤에 들어올 수 arr[i]가 arr[stack[-1]]보다 크면 stack[-1]=idx에 해당하는 위치의 answer[idx]에 현재값 arr[i]를 저장

앞서 입력된 수보다는 작은수들이 들어오기 때문에 현재의 arr[i]값을 기준으로 while stack을 통한 answer 값을 보장할 수 있다.
'''

n = int(input())
arr = list(map(int,input().split()))
stack = [0]
answer = [-1]*n

for i in range(1,n):
    while stack:
        if arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            answer[idx] = arr[i]
        else:
            break
    stack.append(i)

print(*answer)





# if max(arr)==arr[0]:
#     ans.append(-1)
# else:
#     answer = 0
#     idx = 0
#     for i in range(1,n):
#         if arr[i] > arr[0]:
#             if answer < arr[i]:
#                 answer = max(answer,arr[i])
#                 idx = i
#                 break
#     ans.append(answer)
# # print(stack)
# # print(ans)
# for i in range(1,n):
#     while stack:
#         if arr[i] > arr[stack[-1]]:
#             stack.pop()
#             ans.append(arr[i])
#         else:
#             break
#     stack.append(i)
# ans.append(-1)
# # print(stack)
# length = len(stack)
# for i in range(length-1):
#     ans.append(-1)
# for i in ans:
#     print(i, end=' ')
